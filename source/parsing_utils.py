import logging
import pathlib
import time
from rogue_aps_utils import rogue_ap_add_band

from aireos_dicts_classes import advanced_config_parsing_dict, ipv6_config_parsing_dict, radius_config_parsing_dict, \
    ap_group_parsing_dict, band_24_parsing_dict, band_5_parsing_dict, cleanair_5g_parsing_dict, \
    cleanair_24g_parsing_dict, system_info_parsing_dict, redundancy_mode_parsing_dict, dhcp_server_parsing_dict, \
    nearby_aps_parsing_dict, ap_config_parsing_dict, ap_rf_parsing_dict, network_config_parsing_dict, \
    ssid_config_parsing_dict, interface_config_parsing_dict, interface_group_parsing_dict, switch_config_parsing_dict, \
    mobility_config_parsing_dict, rf_profile_parsing_dict, main_parsing_dict_aireos, NamedList, Band24_Config, \
    Band5_Config, Rf_Profile, Ap_Config, Radius_Accounting_Server, Mobility_Group_Member, Port, Rogue_Ap, System_Config, \
    Redundancy_Config, Mobility_Config, Network_Config, Dhcp_Server, Cleanair_24G_Config, Cleanair_5G_Config, \
    Switch_Config, Radius_Config, Ipv6_Config, Advanced_Config, Ap_Group_Wlan, Ap_Group_Wlans, Ap_Group, Nearby_Ap, \
    Nearby_Aps, Ap_Rf_Config, Dynamic_Interface, Interface_Group, Ssid_Config, Radius_Authentication_Server, Wlc_Config, \
    test_parsing_dicts_aireos

from ewlc_dicts_classes import ewlc_client_stats_parsing_dict, ewlc_http_server_parsing_dict, \
    ewlc_multicast_parsing_dict, ewlc_mobility_parsing_dict, ewlc_advanced_eap_parsing_dict, ewlc_rf_tag_parsing_dict, \
    ewlc_site_tag_parsing_dict, ewlc_policy_tag_parsing_dict, ewlc_rogue_ap_parsing_dict, \
    ewlc_flex_profile_parsing_dict, ewlc_ap_profile_parsing_dict, ewlc_policy_profile_parsing_dict, \
    ewlc_ssid_parsing_dict, ewlc_ap_rf_24_parsing_dict, ewlc_ap_rf_5_parsing_dict, ewlc_ap_config_parsing_dict, \
    ewlc_ap_slots_parsing_dict, ewlc_nearby_aps_parsing_dict, main_parsing_dict_ewlc, Ewlc_Client_Stats, \
    Ewlc_Https_Server, Ewlc_Advanced_Eap, Ewlc_Rf_Tag, Ewlc_Site_Tag, Ewlc_Policy_Tag, Ewlc_Wlan_Policy_Mapping, \
    Ewlc_Rlan_Policy_Mapping, Ewlc_Rogue_Ap_All, Ewlc_Rogue_Ap, Ewlc_Flex_Vlan_Mapping, Ewlc_Flex_Profile, \
    Ewlc_Ap_Join_Profile, Ewlc_Policy_Profile, Ewlc_Ssid_Config, Ewlc_Nearby_Ap, Ewlc_Nearby_Aps, Ewlc_Ap_Rf_24_Config, \
    Ewlc_Ap_Rf_5_Config, Ewlc_Ap_Config, Ewlc_Ap_Slot_Config, Ewlc_Mobility_All, Ewlc_Mobility_Member, Ewlc_Multicast, \
    Wlc_Ios_Xe_Config, test_parsing_dicts_ewlc

main_parsing_dict = {'AireOS': {}, '9800': {}}
main_parsing_dict['9800'] = main_parsing_dict_ewlc
main_parsing_dict['AireOS'] = main_parsing_dict_aireos

namedlist_startword_dict = {'AireOS':{
                                'WLAN Configuration': 'WLAN Identifier',
                                'Interface Configuration': 'Interface Name',
                                'Interface Group Configuration': 'Interface Group Name',  # divider sentence for list elements within config section
                                'Total Number of AP Groups': 'Site Name',
                                'AP Airewave Director Configuration': 'Number Of Slots',
                                'AP Config': 'Cisco AP Identifier',
                                'DHCP Info': 'DHCP Server IP Address',
                                'Airewave Director Configuration': 'Number Of Slots',
                                'Number of RF Profiles': 'RF Profile name..',  # RF profile - not clear from name
                                'System Information': None,  # For non-list config sections
                                'Probe request filtering..': None,
                                'RADIUS Configuration': None,
                                'WLC IPv6 Summary': None,
                                'Mobility Configuration': None,  # For non-list config sections
                                'Switch Configuration': None,  # For non-list config sections
                                'Network Information': None,  # For non-list config sections
                                'Redundancy Information': None,  # For non-list config sections
                                '802.11a Configuration': None,  # For non-list config sections
                                '802.11b Configuration': None,  # For non-list config sections
                                '802.11b CleanAir Configuration': None,  # For non-list config sections
                                '802.11a CleanAir Configuration': None,  # For non-list config sections
},
                            '9800':{
                                '--- show ap config general ---': 'Cisco AP Name',
                                '--- show ap config slots ---': 'Attributes for Slot',
                                '--- show ap auto-rf dot11 5ghz ---': 'Number of Slots',
                                '--- show ap auto-rf dot11 24ghz ---': 'Number of Slots',
                                '--- show wlan all ---': 'WLAN Profile Name',
                                '--- show wireless profile policy all ---': 'Policy Profile Name',
                                '--- show ap profile all-profiles ---': 'AP Profile Name',
                                '--- show wireless profile flex  all ---': 'Flex Profile Name',
                                '--- show wireless tag policy all ---': 'Policy Tag Name',
                                '--- show wireless tag site all ---': 'Site Tag Name',
                                '--- show wireless tag rf all ---': 'Tag Name',
                                '----- show ap auto-rf dot11 24ghz -----': 'Number of Slots',  # Nearby APs
                                '--- show wireless wps rogue ap summary ---': None,
                                '--- show wireless stats client detail ---': None,
                                '--- show advanced eap ---': None,
                                '--- show wireless mobility summary ---': None,
                                '--- show wireless multicast ---': None,
                                '--- show ip http server status ---': None,
                            }}

def file_to_string(filename):
    config_string = []
    try:
        f = open(filename, 'r', encoding="utf8", errors='ignore')
        previous_line = ''
        for line in f:
            line_str = line.rstrip()
            if len(line_str) > 5:  # Remove empty strings
                if 'More or (q)uit' in line_str:
                    pass
                elif line.startswith('.'): #Line break in between points (bad session log from MGTS)
                    config_string.pop()
                    config_string.append(previous_line+line_str)
                elif '....' in line and not '....' in previous_line and (len(line) - len(line.lstrip())) < previous_leading_spaces:#Line break in keyword
                    config_string.append(previous_line + line_str)
                else:
                    config_string.append(line_str)
            previous_line = line_str
            previous_leading_spaces = len(line) - len(line.lstrip())
        #Find platform by specific config lines
        for line in config_string:
            if 'Cisco IOS XE Software' in line:
                platform = '9800'
                break
            if 'System Inventory' in line:
                platform = 'AireOS'
                break
        print('Number of NON-EMPTY lines in config file ', len(config_string))
        print('Platform is ',platform)
        logging.debug('Number of NON-EMPTY lines in config file ' + str(filename) + str(len(config_string)))
        logging.debug('Platform is ' + platform)

        f.close()
    except:
        print('File error, please check the file name and folder are correct!')
        logging.debug('File error' + str(filename))
        return None, 'empty'
    return config_string, platform


def parse_wlan_ap_group_section(config_section, object):
    #Function parses AireOS AP group table
    config_sub_section = find_config_section(config_section, 'WLAN ID', '*AP3600 with 802.11ac')
    for line in config_sub_section:
        if 'ble' in line and len(line.split()) > 3:
            item = object.wlans.get_one_item()
            splitted_line = line.split()  # ' ')#by space
            # WLAN ID          Interface          Network Admission Control          Radio Policy        OpenDnsProfile
            # -------          -----------        --------------------------         ------------         --------------
            # 507             igr_guest_users      Disabled                          None                        None
            # 509             igr_employee_users   Disabled                          None                        None
            item.wlan_id = splitted_line[0].strip()
            item.interface = splitted_line[1].strip()
            item.nac = splitted_line[2].strip()
            item.radio_policy = splitted_line[3].strip()
            try:
                item.open_dns_profile = splitted_line[4].strip()
                # open dns profile in AP group started to appear in 8.5
            except:
                pass
            item.update_name()
            object.wlans.append(item)  # !!!
    # object.update_name()
    return object


def parse_nearby_aps_section(config_section, object):
    # Function parses AireOS Nearby APs section
    for line in config_section:
        if 'Slot ID' in line:
            object.ap_slot = line.split()[-1]
        if 'AP Name' in line:
            object.ap_name = line.split()[-1]
        if line.count(':') == 5 and 'dBm' in line:
            item = object.get_one_item()
            splitted_line = line.split()  # ' ')#by space
            # AP a0:93:51:38:9e:40 slot 0..................  -84 dBm on   1  20MHz (10.112.25.129)  WA-8NSK-ABK-001-2SRV (8.3.150)
            # AP a0:93:51:38:a9:0f slot 1..................  -90 dBm on  64  20MHz (10.112.25.129)  WA-8ABK-TRSV-001-2004 (8.3.150)
            # AP 3c:ce:73:f9:3e:40 slot 0..................  -40 dBm on   1 (0a:e2:89:42:01:f4)
            item.mac_address = splitted_line[1]
            item.rssi = splitted_line[4]
            item.channel = splitted_line[7]
            for piece in splitted_line:
                if 'MHz' in piece:
                    item.bandwidth = piece
            item.update_name()
            object.append(item)
    object.update_name()
    return object

def parse_nearby_aps_section_ewlc(config_section, object):
    # Function parses AireOS Nearby APs section
    for line in config_section:
        if 'Slot ID' in line:
            object.ap_slot = line.split()[-1]
        if 'AP Name' in line:
            object.ap_name = line.split()[-1]
        if 'MHz)' in line and 'slot' in line and 'dBm' in line:
            item = object.get_one_item()
            splitted_line = line.split()  # ' ')#by space
            #   Nearby APs
            #     AP 78bc.1a12.602f slot 1                     :  -50 dBm on (132, 40 MHz) (192.168.176.241) (CHECK that base BSSID is ending with F for 5 GHz)
            #     AP 78bc.1a12.620f slot 1                     :  -54 dBm on ( 64, 40 MHz) (192.168.176.241)
            #     AP b026.80ed.27cf slot 1                     :  -58 dBm on (149, 40 MHz) (192.168.176.241)
            #     AP 28ac.9ea6.fa0f slot 1                     :  -70 dBm on ( 56, 40 MHz) (192.168.176.241)
            #    AP 70db.98f5.c440 slot 0                     :  -61 dBm on (  6, 20 MHz) (192.168.176.241)
            #    AP a093.514e.32f0 slot 0                     :  -68 dBm on ( 11, 20 MHz) (192.168.176.241)
            item.mac_address = splitted_line[1].strip()
            item.rssi = splitted_line[5]
            item.bandwidth = splitted_line[10]
            item.rf_leader = splitted_line[-1]
            item.channel = line.split('(')[1].split(',')[0].strip()
            item.update_name()
            object.append(item)

    object.update_name()
    return object


def parse_mobility_group_members(config_section, object):
    item = object.get_one_item()
    if len(config_section.split()) > 4 and config_section.count('.') == 6:
        # Controllers configured in the Mobility Group
        # MAC Address        IP Address                                       Group Name                        Multicast IP                                     Status
        # 6c:20:56:6c:20:56  10.10.100.193                                     RFG                              0.0.0.0                                          Up
        splitted_line = config_section.split()
        item.mac_address = splitted_line[0].strip()
        item.ip_address = splitted_line[1].strip()
        item.mobility_group_name = splitted_line[2].strip()
        item.multicast_ip = splitted_line[3].strip()
        states = splitted_line[4:]  # "Control and Data Path Down'
        state = ''
        for piece in states: state = state + piece
        item.state = state
        item.update_name()
    return item


def parse_radius_auth_servers(config_section, object):
    item = object.get_one_item()
    if len(config_section.split()) > 7 and config_section.count('ble') >= 2:
        # Idx  Type  Server Address    Port    State     Tout  MgmtTout  RFC3576  IPSec - state/Profile Name/RadiusRegionString
        # ---  ----  ----------------  ------  --------  ----  --------  -------  -------------------------------------------------------
        # 1  *       10.48.71.92       1812    Enabled   5     5         Disabled  Disabled - /none
        # 2  *       10.48.71.90       1812    Enabled   5     5         Enabled   Disabled - none/none
        # 3  * N     10.34.244.207     1812    Enabled   2     2         Enabled   Disabled - /none
        # Idx  Type  Server Address    Port    State     Tout  MgmtTout  RFC3576  IPSec - AuthMode/Phase1/Group/Lifetime/Auth/Encr/Region
        # ---  ----  ----------------  ------  --------  ----  --------  -------  -------------------------------------------------------
        # 10   N     172.16.85.100     1812    Enabled   2     2         Enabled   Disabled - none/unknown/group-0/0 none/none/none
        for piece in config_section.split():
            if ('N' in piece or 'M' in piece) and not ('N/A' in piece):
                item.type = piece
        config_section = config_section.replace('*', ' ')
        config_section = config_section.replace('N', ' ')
        config_section = config_section.replace('M', ' ')
        splitted_line = config_section.split()
        item.id = splitted_line[0].strip()
        item.ip_address = splitted_line[1].strip()
        item.port = splitted_line[2].strip()
        item.state = splitted_line[3].strip()
        item.timeout = splitted_line[4].strip()
        item.mgmt_timeout = splitted_line[5].strip()
        item.rfc3576 = splitted_line[6].strip()
        item.ipsec = splitted_line[7].strip()
        item.update_name()
    return item


def parse_port_summary_section(config_section, object):
    item = object.get_one_item()
    if len(config_section.split()) > 8 and 'ble' in config_section:
        # item = object.get_one_item()
        # splitted_line = config_section.split()#' ')#by space
        # AP a0:93:51:38:9e:40 slot 0..................  -84 dBm on   1  20MHz (10.112.25.129)  WA-8NSK-ABK-001-2SRV (8.3.150)
        # Port Summary
        #           STP   Admin   Physical   Physical   Link   Link
        # Pr  Type   Stat   Mode     Mode      Status   Status  Trap     POE    SFPType
        # -- ------- ---- ------- ---------- ---------- ------ ------- ------- ----------
        # 1  Normal  Forw Enable  Auto       1000 Full  Up     Enable  N/A     1000BaseSX
        # 2  Normal  Forw Enable  Auto       1000 Full  Up     Enable  N/A     1000BaseSX
        # 1  Normal  Forw Enable  Auto       10000 Full Up     Enable  N/A
        item.number = config_section[0:2].strip()
        item.type = config_section[3:9]
        item.stp_state = config_section[11:15]
        item.admin_mode = config_section[16:23]
        item.phy_mode = config_section[24:34]
        item.phy_status = config_section[35:45]
        item.link_status = config_section[46:52]
        item.link_trap = config_section[53:60]
        item.poe = config_section[61:68]
        try:
            item.sfp_type = config_section[69:79]
        except:
            item.sfp_type = None
        item.update_name()
    return item


def parse_rogue_ap_section(line, software_version, item_type2):
    if software_version.startswith('8.3') or software_version.startswith('8.5') or software_version.startswith('8.8'):
        splitted_line = line.split()
        if splitted_line[0].count(':') == 5 and len(
                splitted_line) > 3:  # MAC address as starting line and all necessary elements exist
            # 00:0c:42:f9:c9:59 Unclassified Contained            0    0
            # fe:3f:db:d0:a9:e7 Unclassified Alert                3    0       58:bf:ea:ba:9a:f0 -68    6                 70:db:98:2e:bd:d0 -69    6
            # fe:3f:db:d0:d6:d1 Unclassified Alert                1    0       a4:56:30:5c:3b:30 -43    6
            setattr(item_type2, 'mac_address', splitted_line[0])
            setattr(item_type2, 'classification', splitted_line[1])
            setattr(item_type2, 'state', splitted_line[2])
            setattr(item_type2, 'detecting_aps', splitted_line[3])
            setattr(item_type2, 'rogue_clients_number', splitted_line[4])
            if len(splitted_line) == 8:
                setattr(item_type2, 'highest_rssi_ap', splitted_line[5])
                setattr(item_type2, 'highest_rssi_value', splitted_line[6])
                setattr(item_type2, 'channel', splitted_line[7])
            if len(splitted_line) == 11:
                setattr(item_type2, 'highest_rssi_ap', splitted_line[5])
                setattr(item_type2, 'highest_rssi_value', splitted_line[6])
                setattr(item_type2, 'channel', splitted_line[7])
                setattr(item_type2, 'second_rssi_ap', splitted_line[8])
                setattr(item_type2, 'second_rssi_value', splitted_line[9])
            #Adding frequency band as attribute by channel number
            if int(splitted_line[7].strip('()').split(',')[0]) > 13:
                band = '5GHz'
            else:
                band = '2.4GHz'
            setattr(item_type2, 'band', band)

    if software_version.startswith('8.0'):
        splitted_line = line.split()
        if splitted_line[0].count(':') == 5 and len(
                splitted_line) > 5:  # MAC address as starting line and all necessary elements exist
            # MAC Address        Classification     # APs # Clients Last Heard
            # -----------------  ------------------ ----- --------- -----------------------
            # 00:0d:88:9b:66:66  Unclassified       4     0         Sun Jul  7 00:04:37 2019
            # 00:0e:8f:06:a7:f2  Unclassified       0     0         Not Heard
            setattr(item_type2, 'mac_address', splitted_line[0])
            setattr(item_type2, 'classification', splitted_line[1])
            setattr(item_type2, 'detecting_aps', splitted_line[2])
            setattr(item_type2, 'rogue_clients_number', splitted_line[3])
    return item_type2


def parse_wlc_config_from_string(config, platform, printout=False):
    if printout: print('Parsing WLC config')
    # Sections order in list for AireOS
    # 1 - Switch config
    # 2 - Network config
    # 2.5 - RF profiles
    # 3 - AP general config
    # 4 - AP RF operational data
    # 5 - WLAN config
    # 6 - Interface config
    # 7 - DHCP server config (operational data)
    # 8 - Nearby APs operational data
    # 9 - Clean Air 2.4 GHz config
    # 10 - Clean Air 5 GHz config
    # 11 - Interface groups config
    # 12 - AP Group config
    # 13 - Mobility config
    # 14 - RADIUS config
    # 15 - IPv6 config
    # 16 - Advanced config (EAP, ANQP parameters etc.)
    section_start_word = {'AireOS':[],'9800':[]}
    section_stop_word = {'AireOS': [], '9800': []}
    section_start_word['AireOS'] = ['Switch Configuration',
                               'Network Information',
                               'Number of RF Profiles',
                               'AP Config',
                               'AP Airewave Director Configuration',
                               'WLAN Configuration',
                               'Interface Configuration',
                               'DHCP Info',
                               'Airewave Director Configuration',
                               'Redundancy Information',
                               'System Information',
                               '802.11a Configuration',
                               '802.11b Configuration',
                               '802.11b CleanAir Configuration',
                               '802.11a CleanAir Configuration',
                               'Interface Group Configuration',
                               'Total Number of AP Groups',
                               'Mobility Configuration',
                               'RADIUS Configuration',
                               'WLC IPv6 Summary',
                               'Probe request filtering..']
    section_stop_word['AireOS'] = ['Network Information',
                              # Always should be not in the last line of interesting config section
                              'Port Summary',
                              'AP Config',
                              'AP Airewave Director Configuration',
                              '802.11a Configuration',
                              'Policy Configuration',
                              'Interface Group Configuration',
                              'Exclusion List',
                              '802.11a Configuration',
                              'AP Bundle Information',
                              'Redundancy Information',
                              '802.11a Advanced Configuration',
                              '802.11b Advanced Configuration',
                              'RF Density Optimization Configurations',
                              'RF Density Optimization Configurations',
                              'WLAN Configuration',
                              'Number of RF Profiles',
                              'Controllers configured in the Mobility Group',
                              'Authentication Servers',
                              'mDNS Service Summary',
                              'Location Configuration']
    section_start_word['9800'] = ['--- show ap config general ---',
                                  '--- show ap config slots ---',
                                  '--- show ap auto-rf dot11 24ghz ---',
                                  '--- show ap auto-rf dot11 5ghz ---',
                                  '--- show wlan all ---',
                                  '--- show wireless profile policy all ---',
                                  '--- show ap profile all-profiles ---',
                                  '--- show wireless profile flex  all ---',
                                  '--- show wireless wps rogue ap summary ---',
                                  '--- show wireless tag policy all ---',
                                  '--- show wireless tag site all ---',
                                  '--- show wireless tag rf all ---',
                                  '--- show advanced eap ---',
                                  '--- show wireless mobility summary ---',
                                  '--- show wireless multicast ---',
                                  '--- show ip http server status ---',
                                  '--- show wireless stats client detail ---',
                                  '----- show ap auto-rf dot11 24ghz -----', #Nearby Aps
                                  ]

    section_stop_word['9800'] = ['--- show ap config slots ---',
                                 '--- show ap image ---',
                                 '--- show ap auto-rf dot11 5ghz ---',
                                 '--- show ap dot11 24ghz channel ---',
                                 '--- show wlan summary ---',
                                 '--- show wireless profile flex',
                                 '--- show wireless profile airtime-fairness summary ---',
                                 '--- show wireless profile mesh all ---',
                                 '--- show wireless wps rogue client summary ---',
                                 '--- show wireless tag rf summary ---',
                                 '--- show wireless tag policy all ---',
                                 '--- show wireless tag site all ---',
                                 '--- show wireless wgb summary ---',
                                 '--- show wireless summary ---',
                                 '--- show wireless multicast group summary ---',
                                 '--- show ip http server session-module ---',
                                 '--- show wireless client steering ---',
                                 '----- show ap dot11 24ghz channel -----',  # Nearby Aps
                                 ]
    # Find hostname - REQUIRED attribute
    collection_date = 'None'  # Necessary to add values for these attributes for empty config files
    dhcp_proxy = 'None'
    hostname = ''
    software_version = ''
    if platform == 'AireOS':
        for line in config:
            if 'System Name...' in line:
                hostname = line.split('. ')[-1]
                break
        # Find software version - REQUIRED attribute
        for line in config:
            if 'Product Version.................' in line:
                software_version = line.split('. ')[-1]
                break
        # Find collection date - REQUIRED attribute since v.072
        for line in config:
            if 'Time........................................' in line:
                collection_date = line.split('. ')[-1]
                break
            elif 'Current Time:' in line:
                collection_date = line.split('-')[0].split('Current Time:')[1]
            else:
                collection_date = 'None'  # Make it empty for older versions like 8.0.140 where no "System Time Information" exists
        # Find global DHCP proxy behavior
        for line in config:
            if 'DHCP Proxy Behaviour:' in line:
                dhcp_proxy = line.split()[-1]
                break
            else:
                dhcp_proxy = 'None'  # Make it empty for configs where no info exists
        timestamp = time.asctime(time.localtime())
        timeadd = timestamp.replace(":", "")
        test_wlc_config = Wlc_Config(hostname, timeadd, software_version, collection_date)
        test_wlc_config.dhcp_proxy = dhcp_proxy
    else:
        for line in find_config_section(config,'show clock','show version'):
            if line.count(':') > 1:
                collection_date = line.strip()
                break
        for line in find_config_section(config,'show version','show running-config'):
            if 'uptime is' in line:
                hostname = line.split(' uptime ')[0]
            if 'Cisco IOS XE Software, Version' in line:
                software_version = line.split('Version ')[-1]
            if 'Installation mode is' in line:
                install_mode = line.split('is ')[-1]
            if 'processor' in line and 'memory' in line:
                subplatform = line.split(' ')[1].strip()
        #Add support for 9800 platform core attributes
        timestamp = time.asctime(time.localtime())
        timeadd = timestamp.replace(":", "")
        test_wlc_config = Wlc_Ios_Xe_Config(hostname, timeadd, software_version, collection_date, install_mode, subplatform)
    test_wlc_config.platform = platform

    # First FOR loop to handle all objects with parsing dictionaries
    for index, start_word in enumerate(section_start_word[platform]):
        logging.debug('Enumerating the list of start words ' + start_word)
        config_object, item_type = get_object(main_parsing_dict[platform][start_word], platform)
        logging.debug('The object is ' + str((type(config_object))))
        logging.debug('Is it named list?' + str(isinstance(config_object,NamedList)))
        config_section = find_config_section(config, start_word, section_stop_word[platform][index],
                                             isinstance(config_object, NamedList), namedlist_startword_dict[platform][
                                                 start_word])  # last argument is True or False for list
        if config_section is not None and len(config_section) > 0:
            if isinstance(config_section[0],list):
            # If config section has subsections (Means that we need Named List) - Parse for every object in list
                for item in config_section:  # Item here is equal to config subsection
                    config_item_object, parsed_strings, parse_errors, errors_list = parse_section(platform, item,
                                                                                                  main_parsing_dict[platform][start_word],
                                                                                                  item_type)
                    config_item_object.update_name()
                    if 'Nearby' in config_item_object.objname: #again special procedure for parsing nearby APs
                        test_wlc_config.add_subclass(config_item_object)
                    else:
                        if config_item_object.name is not None:  # If item is empty then we should not add it to the list
                            config_object.append(config_item_object)
                            logging.debug('New item is parsed and appended to NamedList ' + str(type(config_item_object)))
                            logging.debug(str(type(config_object)))
                    config_object2, item_type = get_object(
                        main_parsing_dict[platform][start_word], platform)  # This is very important step to renew item_type!!! ;)
            else:  # Parse only once
                config_object, parsed_strings, parse_errors, errors_list = parse_section(platform, config_section,
                                                                                         main_parsing_dict[platform][start_word],
                                                                                         config_object)
            logging.debug(str(type(config_object)))
            test_wlc_config.add_subclass(config_object)
    if platform == 'AireOS':
        # Second FOR loop to handle all Named List-type objects
        # Sections order:
        # 1- Rogue APs
        # 2 - Ports
        # 3 - Mobility group members
        # 4 - RADIUS authentication servers
        # 5 - RADIUS accounting servers
        listsection_start_words = ['Total Rogues classified', 'Port Summary',
                                   'Controllers configured in the Mobility Group', 'Authentication Servers',
                                   'Accounting Servers']
        listsection_stop_words = ['Rogue AP RLDP Configuration', 'AP Summary', 'Mobility Hash Configuration',
                                  'Accounting Servers', 'Displays RADIUS queue summary']
        for index, start_word in enumerate(listsection_start_words):
            logging.debug('Enumerating the list of start words for LISTS' + start_word)
            config_object, item_type = get_object(start_word, platform)
            config_section = find_config_section(config, start_word, listsection_stop_words[index])
            # every line is list item but 1) it should start with special symbols AND 2) number of fields depends on object type
            if config_section is not None:
                for line in config_section:
                    if config_object.item_name == 'Rogue_AP':
                        config_object2, item_type2 = get_object(start_word, platform)
                        item_type2 = parse_rogue_ap_section(line, test_wlc_config.software_version, item_type2)
                        item_type2.update_name()
                        if item_type2.name is not None:
                            config_object.append(item_type2)
                    if config_object.item_name == 'Port':
                        config_object2, item_type2 = get_object(start_word, platform)
                        item_type2 = parse_port_summary_section(line, item_type2)
                        if item_type2.name is not None:
                            config_object.append(item_type2)
                    if config_object.item_name == 'Mobility group member':
                        config_object2, item_type2 = get_object(start_word, platform)
                        item_type2 = parse_mobility_group_members(line, item_type2)
                        if item_type2.name is not None:
                            config_object.append(item_type2)
                    if config_object.item_name == 'Radius authentication server' or config_object.item_name == 'Radius accounting server':
                        config_object2, item_type2 = get_object(start_word, platform)
                        item_type2 = parse_radius_auth_servers(line, item_type2)
                        if item_type2.name is not None:
                            config_object.append(item_type2)
            test_wlc_config.add_subclass(config_object)
        # This part will add AP names to AP groups
        for ap_group in test_wlc_config.ap_groups:
            test_wlc_config.ap_groups[ap_group.name].ap_names = [ap.name for ap in test_wlc_config.ap_configs if
                                                                 ap.cisco_ap_group_name == ap_group.name]
    if platform == '9800' and len(test_wlc_config.ap_slots)>0: # This part will add AP names to AP slot configs in 9800 (post processing of parsed WLC config
        for ap_slot in test_wlc_config.ap_slots:
            try: #if ap_configs is empty, then ap slots will be referenced by bssid, else by ap name
                test_wlc_config.ap_slots[ap_slot.name].ap_name = [ap.name for ap in test_wlc_config.ap_configs if ap.cisco_ap_identifier == ap_slot.station_configuration_bssid][0] #First (and only) element in list
                test_wlc_config.ap_slots[ap_slot.name].update_name()
                logging.debug('AP slots names for 9800 updated')
            except:
                pass
        rogue_ap_add_band(test_wlc_config) #This part will add frequency band for every rogue AP
        logging.debug('Rogue AP frequency bands for 9800 updated')
    return test_wlc_config


def parse_file(filename):
    wlcs = {}  # Dictionary with wlc configs parsed at one time, key = hostname, value = WLC config object
    wlcs_raw_data, platform = file_to_string(filename)
    if platform == 'empty': #if there is file error
        return None
    logging.debug('Parsed platform is ' + platform)
    wlc_config_separator = {'AireOS':'System Information','9800':'--- show clock ---'}
    config_sections = separate_wlc_config(wlcs_raw_data, wlc_config_separator[platform])
    if isinstance(config_sections[0],
                  list):  # If config section has subsections (Means that we need Named List) - Parse for every object in list
        for item in config_sections:  # Item here is equal to config subsection
            config = parse_wlc_config_from_string(item, platform, True)
            wlcs[config.hostname] = config
    else:
        config = parse_wlc_config_from_string(config_sections, platform)
        wlcs[config.hostname] = config
    print('Following WLCs were parsed from file: ', [key for key in wlcs.keys()])
    print('Reach wlc config object by referencing device name as dictionary key. For example, wlc_archive["WLC1"]')
    logging.debug('Following WLCs were parsed from file: '+ str(wlcs.keys()))
    return wlcs


# Read all WLC config files from folder (good for time-series, requires pathlib)
def read_folder(folder_name):
    filenames_list = []
    print('The following files are found in this folder ', folder_name, ':')
    logging.debug('The following files are found in this folder ' + folder_name + ':')
    for p in pathlib.Path(folder_name).iterdir():
        if p.is_file():
            print(p)
            logging.debug(str(p))
            filenames_list.append(p)
    archive = {}
    index = 0
    for filename in filenames_list:
        wlc = parse_file(filename)
        archive[index] = wlc
        index += 1
    print('Successfully parsed ', len(archive), ' files from folder')
    logging.debug('Successfully parsed ' + str(len(archive)) + ' files from folder')
    return archive

def dict_key_with_max_value(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def parse_table(config_section, named_list, namedlist_item_class):
    logging.debug('parsing tables function is called for section ' + config_section[0])
    logging.debug('named list is ' + str(named_list))
    logging.debug('named list item class is ' + str(namedlist_item_class))
    logging.debug('Length of config section is ' + str(len(config_section)))
    table_separator_found = False
    separator_length = 0
    for index,line in enumerate(config_section):
        #logging.debug(str(index) + line)
        if '-----------------------------------------' in line: #table separator
            table_separator_found = True
            separator_length = len(line)
            for steps_back in range(1,3): #go back up to 2 lines to find table column names
                if len(config_section[index - steps_back]) > 5: #in range(len(line) - 5,len(line) + 5): #line should be about the same, +-5 chars
                    table_column_names = [item.strip() for item in list(filter(None,config_section[index-steps_back].split('  '))) if len(item)>1] #split by double space and remove empty items
                    attribute_names = ([attribute for attribute in dir(namedlist_item_class()) if not '__' in attribute and not attribute in ['name', 'objname','show', 'type', 'update_name', 'grep']])
                    logging.debug('Table column names are ' + str(table_column_names))
                    logging.debug('Attribute names names are ' + str(attribute_names))
                    index_attribute_dict ={}
                    for attribute_name in attribute_names:
                        occurences_dict = {}
                        for index,column_name in enumerate(table_column_names):
                            occurences = 0
                            all_words = [word.lower() for word in column_name.split()]
                            if len([word.lower() for word in column_name.split('-')]) > 1: #split by '-' char
                                all_words = all_words + [word.lower() for word in column_name.split('-')]
                            for word in all_words:
                                clean_word = ''.join([i for i in word if i.isalpha()]) #remove all non-chars like #APs
                                if clean_word in attribute_name:
                                    occurences += 1
                                else:
                                    occurences -= 1 #fine for additional words, for example just "rssi" vs "highest rssi ap"
                            occurences_dict[index] = occurences
                        index_attribute_dict[dict_key_with_max_value(occurences_dict)] = attribute_name
                    logging.debug(str(index_attribute_dict))
                    break
        if table_separator_found and not '-----------------------' in line:
            values_list = [item.strip() for item in list(filter(None,line.strip().split('  '))) if len(item)>0]
            if len(values_list) > 0: #non-empty line in table
                item = namedlist_item_class()
                for index, value in enumerate(values_list):
                    try:
                        setattr(item,index_attribute_dict[index],value)
                    except:
                        pass
                #logging.debug('Item with attributes set ' + str(item))
                item.update_name()
                if item.name != 'Unknown': #append only non-empty items to the list of results
                    named_list.append(item)
    if len(named_list) == 0:
        named_list = NamedList('empty - no data', namedlist_item_class())
    return named_list

def get_object(parsing_dict, platform):
    logging.debug('Function get_object is called')
    if platform == '9800':
        if 'AP IPv6 TCP MSS Adjust' in parsing_dict:
            return NamedList('AP Configs', 'Ap_Config'), Ewlc_Ap_Config()  # Need an item for every Named List
        if 'RX SOP threshold' in parsing_dict:
            return NamedList('AP slots','AP slot config'), Ewlc_Ap_Slot_Config()# Need an item for every Named List
        if  'unique_ap_rf_5ghz_key' in parsing_dict:
            return NamedList('AP RF 5GHz Data', 'AP RF 5GHz slot data'), Ewlc_Ap_Rf_5_Config()
        if  'unique_ap_rf_24ghz_key' in parsing_dict:
            return NamedList('AP RF 2.4GHz Data', 'AP RF 2.4GHz slot data'), Ewlc_Ap_Rf_24_Config()
        if 'unique_ssid_config_key' in parsing_dict:
            return NamedList('SSIDs', 'SSID Config'), Ewlc_Ssid_Config()
        if 'unique_policy_profile_config_key' in parsing_dict:
            return NamedList('Policy profiles', 'Policy profile'), Ewlc_Policy_Profile()
        if 'unique_ap_join_profile_config_key' in parsing_dict:
            return NamedList('AP join profiles', 'AP join profile'), Ewlc_Ap_Join_Profile()
        if 'unique_ap_join_profile_config_key' in parsing_dict:
            return NamedList('AP join profiles', 'AP join profile'), Ewlc_Ap_Join_Profile()
        if 'unique_flex_profile_config_key' in parsing_dict:
            return NamedList('Flex profiles', 'Flex Profile'), Ewlc_Flex_Profile()
        if 'unique_policy_tag_parsing_key' in parsing_dict:
            return NamedList('Policy TAGs', 'Policy TAG'), Ewlc_Policy_Tag()
        if 'unique_site_tag_parsing_key' in parsing_dict:
            return NamedList('Site TAGs', 'Site TAG'), Ewlc_Site_Tag()
        if 'unique_rf_tag_parsing_key' in parsing_dict:
            return NamedList('RF TAGs', 'RF TAG'), Ewlc_Rf_Tag()
        if 'unique_eap_timers_parsing_key' in  parsing_dict:
            return Ewlc_Advanced_Eap(), None
        if 'unique_rogue_ap_parsing_key' in  parsing_dict:
            return Ewlc_Rogue_Ap_All(), None
        if 'unique_mobility_parsing_key' in  parsing_dict:
            return Ewlc_Mobility_All(), None
        if 'unique_multicast_parsing_key' in  parsing_dict:
            return Ewlc_Multicast(), None
        if 'unique_https_server_parsing_key' in parsing_dict:
            return Ewlc_Https_Server(), None
        if 'unique_client_stats_parsing_key' in parsing_dict:
            return Ewlc_Client_Stats(), None
        if 'EWLC Nearby AP' in parsing_dict:
            return Ewlc_Nearby_Aps('Nearby_Aps', 'Nearby_Ap'), Ewlc_Nearby_Aps('Nearby_Aps',
                                                                     'Nearby_Ap')  # Item is the same as list because we need to add list of nearby aps to every ap
    if platform == 'AireOS':
        if 'Cisco AP Identifier' in parsing_dict:
            return NamedList('AP Configs', 'Ap_Config'), Ap_Config()  # Need an item for every Named List
        if 'Number of AP Groups using the Interface Group' in parsing_dict:
            return NamedList('Interface Groups', 'Interface_Group'), Interface_Group()
        if 'RF Profile name' in parsing_dict:
            return NamedList('RF profiles', 'Rf_Profile'), Rf_Profile()  # Need an item for every Named List
        if 'Client Traffic QinQ Enable' in parsing_dict:
            return NamedList('AP Groups', 'Ap_Group'), Ap_Group()  # Need an item for every Named List
        if 'Nearby AP' in parsing_dict:
            return Nearby_Aps('Nearby_Aps', 'Nearby_Ap'), Nearby_Aps('Nearby_Aps',
                                                                     'Nearby_Ap')  # Item is the same as list because we need to add list of nearby aps to every ap
        if 'Total Rogues classified' in parsing_dict:
            return NamedList('Rogue APs', 'Rogue_AP'), Rogue_Ap()  # Need an item for every Named List
        if 'Port Summary' in parsing_dict:
            return NamedList('Ports', 'Port'), Port()  # Need an item for every Named List
        if 'Controllers configured in the Mobility Group' in parsing_dict:
            return NamedList('Mobility group members', 'Mobility group member'), Mobility_Group_Member()
        if 'Authentication Servers' in parsing_dict:
            return NamedList('Radius authentication servers',
                             'Radius authentication server'), Radius_Authentication_Server()
        if 'Accounting Servers' in parsing_dict:
            return NamedList('Radius accounting servers', 'Radius accounting server'), Radius_Accounting_Server()
        if 'WLAN Identifier' in parsing_dict:
            return NamedList('SSIDs', 'Ssid_Config'), Ssid_Config()  # Need an item for every Named List
        if '3G VLAN' in parsing_dict:
            return NamedList('Dynamic Interfaces',
                             'Dynamic_Interface'), Dynamic_Interface()  # Need an item for every Named List
        if 'Load Profile' in parsing_dict:
            return NamedList('AP RF Configs', 'Ap_Rf_Config'), Ap_Rf_Config()  # Need an item for every Named List
        if 'DHCP REQUEST Count:' in parsing_dict:
            return NamedList('DHCP servers', 'Dhcp_Server'), Dhcp_Server()
        if 'RA Throttling allow at-least' in parsing_dict:
            return Ipv6_Config(), None
        if 'Auth Call Station Id Type' in parsing_dict:
            return Radius_Config(), None  # None should be added as second variable for every non-list object
        if 'Internal Temperature' in parsing_dict:
            return System_Config(), None  # None should be added as second variable for every non-list object
        if 'EAP Max-Login Ignore Identity Response' in parsing_dict:
            return Advanced_Config(), None  # None should be added as second variable for every non-list object
        if '802.11 FH' in parsing_dict and 'Bluetooth Link' in parsing_dict:
            return Cleanair_24G_Config(), None  # None should be added as second variable for every non-list object
        if 'SuperAG' in parsing_dict and not '802.11 FH' in parsing_dict:
            return Cleanair_5G_Config(), None  # None should be added as second variable for every non-list object
        if 'Redundancy Port IP Address' in parsing_dict:
            return Redundancy_Config(), None  # None should be added as second variable for every non-list object
        if 'Mobility Protocol Port' in parsing_dict:
            return Mobility_Config(), None  # None should be added as second variable for every non-list object
        if '802.3x Flow Control Mode' in parsing_dict:
            return Switch_Config(), None  # None should be added as second variable for every non-list object
        if 'RF-Network Name' in parsing_dict:
            return Network_Config(), None  # None should be added as second variable for every non-list object
        if '802.11a High Band' in parsing_dict:
            return Band5_Config(), None  # None should be added as second variable for every non-list object
        if '802.11b/g 5.5M Rate' in parsing_dict:
            return Band24_Config(), None  # None should be added as second variable for every non-list object
        else:
            raise Exception('Unrecognized object type')


def get_config_part(config, start_word, stop_word, printout=False):
    if printout: print('getting config section for ', start_word, stop_word)
    logging.debug('getting config section for ' + start_word + stop_word)
    config_section = []
    within_section_flag = 0
    for line in config:
        if start_word in line:  # to exclude no section in rogue ap section # and len(line) == len(start_word): #To exclude false positives for "WLAN Configuration Information"
            config_section.append(line)
            within_section_flag = 1
        if within_section_flag == 1:
            config_section.append(line)
        if stop_word in line and within_section_flag == 1:
            config_section.pop()  # remove last string
            return config_section
        if stop_word in line and within_section_flag == 0:
            print('WARNING : Stop word before start word: ', stop_word, start_word)
            logging.debug('ERROR : Stop word before start word' + stop_word + start_word)
            return []
    return config_section


def find_config_section(config, start_word, stop_word, isnamedlist=False, section_breaker=''):
    if isnamedlist == True:
        config_section = get_config_part(config, start_word, stop_word)  # first get part of config
        # Then separate this part by list start word
        inside_section_flag = 0
        piece = []
        config_sections_list = []
        if config_section is not None:
            for line in config_section:
                if isinstance(line, str):
                    if inside_section_flag == 1:
                        piece.append(line)
                    if section_breaker in line and len(
                            piece) > 0 and inside_section_flag == 1:  # Following section breaker case
                        inside_section_flag = 1
                        # Special case for handling double AP identifier started in 8.5 for AP-COS
                        if 'Attributes for Slot  1' in piece and not 'Attributes for Slot  0' in piece:
                            config_sections_list[-1] = config_sections_list[-1] + piece
                        else:
                            config_sections_list.append(piece)
                        piece = []
                    if section_breaker in line and len(piece) == 0:  # First section breaker case
                        inside_section_flag = 1
                        piece.append(line)
                    if not section_breaker in line and len(piece) == 0:
                        inside_section_flag = 0
        # Special case for handling double AP identifier started in 8.5 for AP-COS
        if 'Attributes for Slot  1' in piece and not 'Attributes for Slot  0' in piece:
            config_sections_list[-1] = config_sections_list[-1] + piece
        else:
            config_sections_list.append(
                piece)  # when end of section is reached, we do not expect the section breaker word
        return config_sections_list
    else:
        config_section = get_config_part(config, start_word, stop_word)  # get this part of config and return it
    return config_section


def separate_wlc_config(config, section_breaker):
    logging.debug('Separating config section for items with ' + section_breaker)
    inside_section_flag = 0
    piece = []
    config_sections_list = []
    for line in config:
        if inside_section_flag == 1:
            piece.append(line)
        if section_breaker in line and len(piece) > 0 and inside_section_flag == 1:  # Following section breaker case
            inside_section_flag = 1
            config_sections_list.append(piece)
            piece = []
        if section_breaker in line and len(piece) == 0:  # First section breaker case
            inside_section_flag = 1
            piece.append(line)
        if not section_breaker in line and len(piece) == 0:
            inside_section_flag = 0

    config_sections_list.append(piece)  # when end of section is reached, we do not expect the section breaker word
    return config_sections_list


def parse_section(platform, config_section, parsing_dict, object, printout=False):
    if printout: print('Section parsing for ', type(object), ' , platform is ',platform)
    if printout: print('Length of config section is ', len(config_section))
    logging.debug('Section parsing for ' + str(type(object)) + ' , platform is ' + platform)
    logging.debug('Length of config section is ' + str(len(config_section)))
    parsed_strings = 0
    parse_errors = 0
    errors_list = []  # List of strings to keep parsing errors
    # For empty config sections - return object with None values
    if len(config_section) == 0:
        return object, parsed_strings, parse_errors, errors_list
    if 'Nearby AP' in parsing_dict:  # Nearby APs is very special kind of config section and needs exclusion
        object = parse_nearby_aps_section(config_section, object)
        return object, parsed_strings, parse_errors, errors_list
    if 'EWLC Nearby AP' in parsing_dict:  # Nearby APs even in ewlc is very special kind of config section and needs exclusion
        object = parse_nearby_aps_section_ewlc(config_section, object)
        return object, parsed_strings, parse_errors, errors_list
    for line_str in config_section: #Last line is not needed
        if 'Interfaces Contained in this group' in line_str:  # special case for interfaces in interface group
            object.interfaces = find_config_section(config_section, 'Interfaces Contained in this group',
                                                    'Interface marked with')[2:]
        if 'WLAN ID' in line_str and 'Network Admission Control' in line_str and 'Radio Policy' in line_str:
            object = parse_wlan_ap_group_section(config_section, object)
        if platform == '9800' and 'Attributes for Slot' in line_str and isinstance(object,Ewlc_Ap_Slot_Config): #There are no valid identifiers for slot id in 9800 "show ap config slots" section and this exception is needed
            if object.slot_id is None: #Need to update only if slot_id was not updated yet (otherwise it may re-write by parsing last string of next slot)
                object.slot_id = line_str.split()[-1]
        if len(line_str) > 5 and '..' in line_str and platform == 'AireOS':
            attr = line_str.lstrip().split('..')[0].rstrip()
            point_splitted_line = line_str.split('..')
            if point_splitted_line[-1].startswith('.'):
                point_splitted_line = point_splitted_line[-1].split('. ')
            value = point_splitted_line[-1].strip()
            if (('ip ' in attr) or ('IP ' in attr)) and line_str.split()[-1].count('.'):  # special case for IP address
                value = line_str.split()[-1].strip()
            if len(value) > 0:
                try:
                    if len(value) > 0 and point_splitted_line[-1] == '.':
                        setattr(object, parsing_dict[attr], 'Empty')
                    elif len(value) > 0:
                        if getattr(object, parsing_dict[
                            attr]) == None:  # Check if this attribute was already parsed (not parsed == None value)
                            setattr(object, parsing_dict[attr], value)
                        else:
                            for j in range(1, 5):  # if this attribute was already parsed, check attribute names + digit
                                try:
                                    if getattr(object, parsing_dict[attr + str(j)]) == None:
                                        setattr(object, parsing_dict[attr + str(j)], value)
                                        break
                                except:
                                    errors_list.append(['No key found ', attr + str(j),
                                                        point_splitted_line[-1].strip().lstrip(
                                                            '.').lstrip()])
                                    break

                    parsed_strings += 1
                except Exception as e:
                    parse_errors += 1
                    if hasattr(e, 'message'):
                        logging.debug('Object attribute is not set - Error 3, attribute name is '+ attr + str(e.message))
                    else:
                        logging.debug('Object attribute is not set - Error 4, attribute name is '+ attr + str(e))
                    errors_list.append(['Other error ', attr, point_splitted_line[-1]])
        if len(line_str) > 5 and ':' in line_str and platform == '9800':
            attr = line_str.lstrip().split(':')[0].rstrip()
            point_splitted_line = line_str.split(':')
            value = point_splitted_line[-1].strip()
            if (('ip ' in attr) or ('IP ' in attr)) and line_str.split()[-1].count('.'):  # special case for IP address
                value = line_str.split()[-1].strip()
            try:
                if isinstance(parsing_dict[attr],dict):
                    if 'dummy' in parsing_dict[attr]['end_table_string']:
                        result = parse_table(get_config_part(config_section, attr, parsing_dict[attr]['end_table_string']), NamedList(parsing_dict[attr]['list_name'],parsing_dict[attr]['item_name']), parsing_dict[attr]['item_class_name'])
                    else:
                        result = parse_table(get_config_part(config_section, attr, parsing_dict[attr]['end_table_string']), NamedList(parsing_dict[attr]['list_name'],parsing_dict[attr]['item_name']), parsing_dict[attr]['item_class_name'])
                    logging.debug('Table parsed &&&& with result:' + str(result))
                    setattr(object, parsing_dict[attr]['attribute_name'],
                            result)
            except:
                pass
            if len(value) > 0 and attr in parsing_dict.keys():
                if isinstance(parsing_dict[attr],str):
                    try:
                        if len(value) > 0 and point_splitted_line[-1] == '.':  # Nechetnoe chislo tochek - not needed for 9800
                            setattr(object, parsing_dict[attr], 'Empty')
                        elif len(value) > 0:
                            #logging.debug('Attribute is ' + attr)
                            if getattr(object, parsing_dict[attr]) == None:  # Check if this attribute was already parsed (not parsed == None value)
                                setattr(object, parsing_dict[attr], value)
                                #logging.debug('%%%% SET attribute ' + attr + ' to ' + value)
                            else:
                                for j in range(1, 5):  # if this attribute was already parsed, check attribute names + digit
                                    try:
                                        if getattr(object, parsing_dict[attr + str(j)]) == None:
                                            setattr(object, parsing_dict[attr + str(j)], value)
                                            break
                                    except:
                                        errors_list.append(['No key found ', attr + str(j),
                                                            point_splitted_line[-1].strip().lstrip(
                                                                '.').lstrip()])
                                        break

                        parsed_strings += 1
                    except Exception as e:
                        parse_errors += 1
                        if hasattr(e, 'message'):
                            logging.debug('Error 1' + str(e.message))
                        else:
                            logging.debug('Error 2' + str(e))
                        errors_list.append(['Other error ', attr, point_splitted_line[-1]])
    if printout: print('Number of parsing errors = ', parse_errors)
    if printout: print('Number of parsed strings = ', parsed_strings)
    logging.debug('Number of parsing errors = ' + str(parse_errors))
    logging.debug('Number of parsed strings = ' + str(parsed_strings))
    logging.debug('errors_list is ')
    return object, parsed_strings, parse_errors, errors_list