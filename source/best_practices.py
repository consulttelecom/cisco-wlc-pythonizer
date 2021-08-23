from collections import Counter
# BEST PRACTICE Class section
class Best_Practice_Description():
    def __init__(self):
        self.id = None
        self.name = None
        self.author = None  # For example BU or AS or TAC or User CCO ID
        self.severity = None  # High\Medium\Low\Information only
        self.section = None  # Architecture\Performance\Security\Other
        self.approval_status = None  # Approved by WLNA subcommitee

    def __str__(self):
        return 'BP rule, id: ' + self.id + ', name: ' + self.name


def bp1(wlc_config):
    description = Best_Practice_Description()
    description.id = 1
    description.name = 'Telnet should be disabled in all APs'
    description.author = 'BU'
    description.severity = 'Medium'
    description.section = 'Security'
    description.platform = 'AireOS, 9800'
    list_names_of_non_compliant_items = [ap.name for ap in wlc_config.ap_configs if 'Enable' in ap.telnet_state]
    number_of_config_items = len([ap for ap in wlc_config.ap_configs])
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items


def bp2(wlc_config):
    description = Best_Practice_Description()
    description.id = 2
    description.name = 'Each SSID is mapped with unique interface in controller if no AAA override is enabled'
    description.author = 'Cisco CX'
    description.severity = 'Medium'
    description.section = 'Security'
    description.platform = 'AireOS'
    interface_list = []
    ssid_list = []
    list_names_of_non_compliant_items = []
    for ssid in wlc_config.ssid:
        if not 'Enable' in ssid.aaa_policy_override:
            if ssid.interface not in interface_list:
                interface_list.append(ssid.interface)
            else:
                list_names_of_non_compliant_items.append(ssid.network_name_ssid)
    number_of_config_items = len(wlc_config.ssid)
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items


def bp3(wlc_config):
    description = Best_Practice_Description()
    description.id = 3
    description.name = 'Local Client profiling using HTTP and DHCP is enabled unless RADIUS profiling is in use'
    description.author = 'Cisco CX'
    description.severity = 'Low'
    description.section = 'Architecture'
    description.platform = 'AireOS'
    list_names_of_non_compliant_items = [ssid.network_name_ssid for ssid in wlc_config.ssid if
                                         'Disable' in ssid.client_profiling_status_local_profiling and 'Disable' in ssid.client_profiling_status_radius_profiling]
    number_of_config_items = len(wlc_config.ssid)
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items


def bp4(wlc_config):
    description = Best_Practice_Description()
    description.id = 4
    description.name = 'Dynamic interface should not have IP address 0.0.0.0'
    description.author = 'Cisco CX'
    description.severity = 'Low'
    description.section = 'Architecture'
    description.platform = 'AireOS'
    list_names_of_non_compliant_items = [interface.name for interface in wlc_config.dynamic_interfaces if
                                         interface.ip_address == '0.0.0.0']
    number_of_config_items = len(wlc_config.dynamic_interfaces)
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items


def bp5(wlc_config):
    description = Best_Practice_Description()
    description.id = 5
    description.name = 'Primary and secondary DHCP server IP addresses are configured for WLC dynamic interfaces if DHCP Proxy is enabled'
    description.author = 'Cisco CX'
    description.severity = 'Medium'
    description.section = 'Architecture'
    description.platform = 'AireOS'
    if wlc_config.dhcp_proxy == 'enabled':
        list_names_of_non_compliant_items = [interface.name for interface in wlc_config.dynamic_interfaces
                                             if interface.dhcp_proxy_mode == 'Global' and
                                             (
                                                     interface.primary_dhcp_server is None or interface.secondary_dhcp_server is None)]
        list_names_of_non_compliant_items = [item for item in list_names_of_non_compliant_items
                                             if not any(s in item for s in ('redundancy', 'service'))]
    else:
        list_names_of_non_compliant_items = []
    number_of_config_items = len(wlc_config.dynamic_interfaces)
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items


def bp_9800_1(wlc_config):
    description = Best_Practice_Description()
    description.id = 1
    description.name = 'Number of AP per site tag'
    description.author = 'BU'
    description.severity = 'Medium'
    description.section = 'Security'
    description.platform = '9800'
    list_names_of_non_compliant_items = []
    if '40' in wlc_config.subplatform:
        max_number_ap_per_site_tag = 800
    elif '80' in wlc_config.subplatform or 'CL' in wlc_config.subplatform:
        max_number_ap_per_site_tag = 1600
    else:
        max_number_ap_per_site_tag = 30*10**10 #unbounded
    site_tags_list = [ap.site_tag_name for ap in wlc_config.ap_configs]
    count_per_site_tag = Counter(site_tags_list)
    for key,value in count_per_site_tag.items():
        if value >= max_number_ap_per_site_tag:
            list_names_of_non_compliant_items.append(key)
    number_of_config_items = len(count_per_site_tag)
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items

def bp_9800_2(wlc_config):
    description = Best_Practice_Description()
    description.id = 2
    description.name = 'HTTP should be disabled in WLC GUI'
    description.author = 'BU'
    description.severity = 'Medium'
    description.section = 'Architecture'
    description.platform = '9800'
    if 'Enable' in wlc_config.https_server.http_server_status:
        list_names_of_non_compliant_items = [wlc_config.hostname]
    else:
        list_names_of_non_compliant_items = []
    number_of_config_items = 1
    number_of_non_compliant_items = len(list_names_of_non_compliant_items)
    if number_of_config_items == number_of_non_compliant_items and number_of_config_items > 0:
        compliance_status = 'Non compliant      '
    elif number_of_non_compliant_items == 0 or number_of_config_items == 0:
        compliance_status = 'Compliant          '
    else:
        compliance_status = 'Partially compliant '
    if number_of_config_items > 0:
        compliance_rate = round((1 - number_of_non_compliant_items / float(number_of_config_items)) * 100)
    else:
        compliance_rate = 100
    return description, compliance_status, compliance_rate, list_names_of_non_compliant_items

def bp_check(wlc_config):
    # This function calls all best practices functions
    if wlc_config.platform == 'AireOS':
        bp_functions_list = [bp1, bp2, bp3, bp4, bp5]
    if wlc_config.platform == '9800':
        bp_functions_list = [bp1,bp_9800_1,bp_9800_2]

    print('Best practices compliance report')
    print('ID Status             Rate Name')
    for best_practice in bp_functions_list:
        description, compliance_status, compliance_rate, list_names_of_non_compliant_items = best_practice(wlc_config)
        print(description.id, compliance_status, compliance_rate, description.name)
    return None