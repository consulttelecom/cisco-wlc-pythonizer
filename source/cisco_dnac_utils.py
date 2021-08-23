# Cisco DNAC functions
# The following import is only needed for getting configs from Cisco DNA Center
import requests
import time
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

def create_url(path, controller_ip, port):
    """ Helper function to create a DNAC API endpoint URL
    """

    if "dna/" in path:
        return "https://%s:%s/%s" % (controller_ip, port, path)
    else:
        return "https://%s:%s/api/v1/%s" % (controller_ip, port, path)


def get_auth_token(controller_ip, username, password, port=443):
    """ Authenticates with controller and returns a token to be used in subsequent API calls
    """

    login_url = "https://{0}:{1}/api/system/v1/auth/token".format(controller_ip, port)
    try:
        result = requests.post(url=login_url, auth=HTTPBasicAuth(username, password), verify=False, timeout=20)
        result.raise_for_status()
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print('Timeout while connecting the specified IP address')
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        return None

    token = result.json()['Token']
    return {
        "controller_ip": controller_ip,
        "token": token
    }


def dnac_api_call(dnac, sequence_list):
    # The function to perform the sequence of API calls needed to get the expected result, for example WLC config file
    # [method, url, payload (optional)]
    # Example:
    # [['method':'get', 'url':'network-device', 'payload':None],['put',...]]

    for api_call in sequence_list:
        action_url = create_url(api_call['url'], dnac['controller_ip'], port=443)
        if api_call['method'] not in ['get', 'post', 'put', 'delete']:
            print('This method is not supported: ', api_call['method'])
        else:
            try:
                if api_call['method'] == 'get':
                    headers = {'x-auth-token': dnac['token']}
                    response = requests.get(action_url, headers=headers, verify=False)
                    response.raise_for_status()

                if api_call['method'] == 'post':
                    headers = {'x-auth-token': dnac['token'], "content-type": "application/json"}
                    response = requests.post(action_url, headers=headers, data=json.dumps(api_call['payload']),
                                             verify=False)
                    response.raise_for_status()

                if api_call['method'] == 'put':
                    headers = {'x-auth-token': dnac['token'], "Content-Type": "application/json"}
                    response = requests.put(action_url, headers=headers, data=api_call['payload'], verify=False)
                    response.raise_for_status()

                if api_call['method'] == 'delete':
                    headers = {'x-auth-token': dnac['token']}
                    response = requests.delete(deleteurl, headers=headers, verify=False)
                    response.raise_for_status()

            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            return response.json()  # Always returns response in JSON format


def dnac_get_wlc_configs(dnac_ip_address=None, username=None, password=None):
    # Interactive function to get WLC config files from DNAC API
    wlc_config_list = []
    command = 'show running-config'
    if dnac_ip_address is None or username is None or password is None:
        dnac_ip_address = input('Enter the IP address of DNAC, please: ')
        username = input('Your username, please: ')
        password = input('Your password, please: ')
    # STEP 1 - Login to DNA Center
    print('Contacting Cisco DNA Center with IP address: ', dnac_ip_address, ' for username: ', username)
    dnac = get_auth_token(dnac_ip_address, username, password)
    if dnac is None:
        return None
    # STEP 2 - Get UIIDS of WLCs
    response = dnac_api_call(dnac, [
        {'method': 'get', 'url': 'network-device?&reachabilityStatus=Reachable', 'payload': None}])
    uiids = []
    print('Following WLC devices are found and reachable: ')
    for device in response['response']:
        if device['family'] == 'Wireless Controller':
            print(device['hostname'])
            uiids.append(device['instanceUuid'])
    if len(uiids) == 0:
        print('Collection results are not successful: no WLCs found')
        return None
    print('Starting config collection...')  # print(uiids)
    # STEP 3 - Run command 'show running-config' on every WLC device - get task ids in taskid list
    taskids = []
    for uiid in uiids:
        payload = {
            'name': 'command-runner',
            'description': 'command-runner-network-poller',
            'timeout': 0,
            'deviceUuids': [uiid],
            'commands': [command]}
        response = dnac_api_call(dnac, [
            {'method': 'post', 'url': 'network-device-poller/cli/read-request', 'payload': payload}])
        taskids.append(response['response']['taskId'])
    if len(taskids) == 0:
        print('Collection results are not successful: empty task ids')
        return None
    print('Waiting for collection results ...')  # print(taskids)
    # STEP 4 - Poll the status of tasks by id - get file ids in file
    fileids = []
    for taskid in taskids:
        response['response']['progress'] = {}
        index = 0
        while not ('fileId' in response['response']['progress'] or index > 8):
            response = dnac_api_call(dnac, [{'method': 'get', 'url': 'task/' + taskid, 'payload': None}])
            # print(response['response']['progress'])
            time.sleep(1)
            index += 1
        if 'fileId' in response['response']['progress']:
            fileids.append(response['response']['progress'].split('":"')[1].split('"}')[
                               0])  # Returned as string by DNAC 1.2.8 if fixed - use response['response']['progress']['fileId']
    if len(fileids) == 0:
        print('Collection results are not successful: empty file ids')
        return None
    print('DNA Center collected configs, grabbing config files from it...')  # print(fileids)
    # STEP 5 - get files by file id
    responses = []
    for fileid in fileids:
        response = dnac_api_call(dnac, [{'method': 'get', 'url': 'file/' + fileid, 'payload': None}])
        # print(response['commandResponses'])
        try:
            if len(response[0]['commandResponses']['SUCCESS'][command]) > 0:
                wlc_config_list.append(response[0]['commandResponses']['SUCCESS'][command])
        except:
            pass
    if len(wlc_config_list) == 0:
        print('Collection results are not successful: empty config files')
        return None
    print('WLC config files are successfully collected')
    timestamp = time.asctime(time.localtime())
    timeadd = timestamp.replace(':', '')
    fileout = 'all_WLC_config-' + 'DNAC-' + dnac_ip_address + timeadd + '.txt'
    print(fileout)
    for config in wlc_config_list:
        with open(fileout, 'a') as config_file:
            config_file.write(config)
    print('Configs are written to file with name: ', fileout)
    print('Configs are sent to parser')
    wlc_configs_archive = parse_file(fileout)
    return wlc_configs_archive