import time
import paramiko
import getpass
import logging
from parsing_utils import parse_file

# WLC config collection functions section
def connect_to_wlc(wlc_ip_addr: str, wlcusername: str, wlcpassword: str, timer: int):  # returns SSH session object
    noconfig_flag = 0
    nodebug_flag = 0
    newline = "\n"
    ssh_pre = paramiko.SSHClient()
    ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_pre.connect(wlc_ip_addr, port=22, username=wlcusername, password=wlcpassword)
        time.sleep(timer)
    except IOError as error:
        print(error)
        print('ERROR: SSH connection to ', wlc_ip_addr, ' failed ')
        ssh_pre.close()
        return None, None, None

    ssh = ssh_pre.invoke_shell()
    ssh.send(newline)
    time.sleep(timer)
    # Need to check the platform
    out = ssh.recv(3000).decode('utf-8')
    if 'User:' in out:  # AireOS platform
        platform = 'AireOS'
        print('sending username...')
        ssh.send(wlcusername + newline)
        time.sleep(timer)
        print('sending pwd...')
        ssh.send(wlcpassword + newline)
        time.sleep(timer)
        out = ssh.recv(3000).decode('utf-8')
        if 'The authenticity of host' in out or 'Are you sure you want to continue connecting' in out:
            raise NoKeyForHost
        if 'User:' in out.split('\n')[-1]:
            print('ERROR: check username or password')
            raise BadUsernamePasswordWLC
        # Check debug and config commands
        if 'Incorrect usage' in exec_wlc_command(ssh, ['config paging disable'], 0.2, platform):
            noconfig_flag = 1
        if 'Insufficient' in exec_wlc_command(ssh, ['debug disable-all'], 0.2, platform):
            nodebug_flag = 1
    else:
        print('sending enable for 9800...')
        platform = '9800'
        ssh.send('enable' + newline)
        time.sleep(timer)
        out = ssh.recv(3000).decode('utf-8')
        if ') >' in out: #AireOS but new ssh implementation
            platform = 'AireOS'
            if 'Incorrect usage' in exec_wlc_command(ssh, ['config paging disable'], 0.2, platform):
                noconfig_flag = 1
            if 'Insufficient' in exec_wlc_command(ssh, ['debug disable-all'], 0.2, platform):
                nodebug_flag = 1
        print('sending pwd...')
        ssh.send(wlcpassword + newline)
        time.sleep(timer)
        out = ssh.recv(3000).decode('utf-8')
        exec_wlc_command(ssh, ['show version'], 0.2, platform)

    print('Connection to ', wlc_ip_addr, ' established')
    logging.debug('Connection to ' + wlc_ip_addr + ' established')

    return ssh, noconfig_flag, nodebug_flag, platform


def exec_wlc_command(ssh, commandlist, period, platform='AireOS'):
    # Executes a list of commands on WLC
    if 'AireOS' in platform:
        # Executes a list of commands on AireOS WLC
        until = ') >'
        newline = '\n'
        buffersize = 204800
        show = ''
        for line in commandlist:
            data = ''
            datasize = 0
            ssh.send(line)
            print('Command ', line, ' is sent')
            logging.debug('Command ' + line + ' is sent')
            time.sleep(period)
            while not data.rstrip().endswith(until):
                try:
                    chunk = ssh.recv(buffersize)

                    if "--More-- or (q)uit" or "Press Enter to continue..." or "abort" in chunk.decode(
                            'utf-8',
                            'ignore'):  # chunk.decode('utf-8').rstrip().endswith("--More-- or (q)uit") or \chunk.decode('utf-8').rstrip().endswith("Press Enter to continue...") or \"abort" in chunk.decode('utf-8'):

                        datasize = datasize + len(chunk)
                        ssh.send("\n")

                    if "more entries" in chunk.decode('utf-8', 'ignore'):  # "more entries? (y/n)"

                        datasize = datasize + len(chunk)
                        ssh.send("y\n")
                except:
                    ssh.send("\n")

                try:
                    data += chunk.decode('utf-8', 'ignore')
                    datasize = datasize + len(chunk)
                except:
                    print('wrong data chunk received', chunk)
                    logging.debug('wrong data chunk received')
            show = show + data
    else:
        # Executes a list of commands on 9800 WLC
        until = '#'
        newline = "\n"
        buffersize = 204800
        show = ''
        for line in commandlist:
            data = ''
            datasize = 0
            ssh.send(line)
            print('Command ', line, ' is sent')
            logging.debug('Command ' + line + ' is sent')
            time.sleep(period)
            while not data.rstrip().endswith(until):
                try:
                    chunk = ssh.recv(buffersize)

                    if "Press Enter to continue..." or "abort" in chunk.decode(
                            'utf-8',
                            'ignore'):
                        datasize = datasize + len(chunk)
                        ssh.send("\n")

                    if "--More--" in chunk.decode('utf-8', 'ignore'):
                        datasize = datasize + len(chunk)
                        ssh.send(" ")  # Space works better with 9800 in show tech wireless
                        time.sleep(0.1)

                    if "more entries" in chunk.decode('utf-8', 'ignore'):  # "more entries? (y/n)"
                        datasize = datasize + len(chunk)
                        ssh.send("y\n")
                except:
                    ssh.send("\n")

                try:
                    data += chunk.decode('utf-8', 'ignore')
                    datasize = datasize + len(chunk)
                except:
                    print('wrong data chunk received', chunk)
                    logging.debug('wrong data chunk received')
            show = show + data
    print('Output is collected')
    logging.debug('SSH Collection is completed')
    return show


def ssh_collect():
    # Function to collect WLC config via SSH
    print('Collecting config from WLC via SSH')
    ip_address = input('WLC IP address, please: ')
    username = input('Your username, please: ')
    password = getpass.getpass('Your password, please: ')
    wlcssh, noconfigflag, nodebugflag, platform = connect_to_wlc(ip_address, username, password, 3)
    if wlcssh is None:
        return None
    print('Please, hold on, getting config, this process can take some time...')
    if 'AireOS' in platform:
        print('Config flag is ', noconfigflag)
        print('Debug flag is ', nodebugflag)
        output = exec_wlc_command(wlcssh, ['show running-config', '\n'], 0.5, 'AireOS')
    else:
        output = exec_wlc_command(wlcssh, ['show tech-support wireless', '\n'], 0.5, '9800')
    wlcssh.close()
    timestamp = time.asctime(time.localtime())
    timeadd = timestamp.replace(':', '')
    fileout = 'WLC_config-' + 'IP ' + ip_address + timeadd + '.txt'
    with open(fileout, 'w') as config_file:
        config_file.write(output)
    print('Configs are written to file with name: ', fileout)
    print('Configs are sent to parser')
    wlc_config = parse_file(fileout)
    return wlc_config