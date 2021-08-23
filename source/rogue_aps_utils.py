import matplotlib.pyplot as plt
from collections import Counter
from ewlc_dicts_classes import Wlc_Ios_Xe_Config
from aireos_dicts_classes import Wlc_Config
from manuf import manuf

# Get manufacturers from the list of MAC addresses via oui
def manufacturer(mac_address_list):
    p = manuf.MacParser()
    manufacturer_list = []
    for usermacaddress in mac_address_list:
        manufacturer_list.append((p.get_manuf(usermacaddress)))
    manufacturer_list = [man for man in manufacturer_list if man is not None]  # Excludes MAC with None
    counts = Counter(manufacturer_list)
    return manufacturer_list, counts

# Rogue APs useful functions
def rogue_ap_rssi(wlc_config, rssi_threshold):
    # Function that returns list of rogue APs filtered by highest RSSI value
    if isinstance(wlc_config, Wlc_Config):
        if '8.3' in wlc_config.software_version or '8.5' in wlc_config.software_version or '8.8' in wlc_config.software_version:
            rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps if
                         rogue_ap.highest_rssi_value != None]  # Rogue AP in "Contained" or "ContainedPending" status do not have RSSI value
            return [rogue_ap for rogue_ap in rogue_aps if int(rogue_ap.highest_rssi_value) > rssi_threshold]
        else:
            print('Not supported in this software version')
            return None
    elif isinstance(wlc_config, Wlc_Ios_Xe_Config):
        rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps.rogue_aps_list if
                         rogue_ap.rssi_value != None]  # Rogue AP in "Contained" or "ContainedPending" status do not have RSSI value
        return [rogue_ap for rogue_ap in rogue_aps if int(rogue_ap.rssi_value) > rssi_threshold]
    else:
        print('This function works only with WLC config objects')
        return None

def rogue_ap_add_band(wlc_config):
    #Function adds frequency band attribute to Ewlc_Rogue_Ap class instance
    for rogue_ap in wlc_config.rogue_aps.rogue_aps_list:
        if not rogue_ap.channel is None:
            if int(rogue_ap.channel) > 13:
                rogue_ap.band = '5GHz'
            else:
                rogue_ap.band = '2.4GHz'


def print_rogues_per_ap(wlc_config, threshold = 0):
    ap_rogues_list = []
    for ap in wlc_config.ap_configs:
        bssid = wlc_config.ap_configs[ap.name].slot_0_bssid
        if ap.name + '_slot1' in [ap.name for ap in
                                  wlc_config.ap_rf]:  # Sometimes AP name in AP general config does not correspond to AP name if AP RF config
            rogues_list = [rogue.name for rogue in wlc_config.rogue_aps if
                          rogue.highest_rssi_ap == bssid or rogue.second_rssi_ap == bssid]
            ap_rogues_list.append([ap.name, len(rogues_list),rogues_list])
    ap_rogues_list.sort(key=lambda x: x[1],reverse=True)
    for ap in ap_rogues_list:
        if ap[1] >= threshold:
            print(ap)


def rogue_ap_rssi_histogram(wlc_config,bands=['2.4GHz','5GHz']):
    # Function that draws histogram of rogue AP RSSI distribution
    if isinstance(wlc_config, Wlc_Config):
        if int(wlc_config.software_version.split('.')[1]) >= 3:  # Check second digit in SW version
            rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps if
                         rogue_ap.highest_rssi_value != None and rogue_ap.detecting_aps != None and rogue_ap.band in bands]
            rssi_levels_list = [-int(rogue_ap.highest_rssi_value) for rogue_ap in rogue_aps if
                                int(rogue_ap.highest_rssi_value) > -80]
            plt.figure(figsize=(8, 8))
            plt.title('Rogue AP RSSI histogram ' + str(bands))
            plt.hist(rssi_levels_list, bins=14)
            return rssi_levels_list
        else:

            print('Non supported WLC software version')
            return None
    else:
        print('This feature is supported for WLC config objects only')
        return None


def rogue_ap_summary(wlc_config):
    if isinstance(wlc_config, Wlc_Config) or isinstance(wlc_config, Wlc_Ios_Xe_Config):
        if wlc_config.platform == 'AireOS' and ('8.0' in wlc_config.software_version or '8.1' in wlc_config.software_version or '8.2' in wlc_config.software_version):
            print('Not supported in this software version because there are no RSSI values')
            return None, None
        else: # '8.3' in wlc_config.software_version or '8.5' in wlc_config.software_version or '8.8' in wlc_config.software_version:
            print('Rogue AP summary for ', wlc_config.hostname, ':')
            if wlc_config.platform == 'AireOS':
                rogue_ap_number = len(wlc_config.rogue_aps)
            else:
                rogue_ap_number = len(wlc_config.rogue_aps.rogue_aps_list)
            print('The overall number of rogue APs :', rogue_ap_number)
            # Filter rogue AP list for AP with values in rssi and # of detecting APs
            if wlc_config.platform == 'AireOS':
                rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps if
                             rogue_ap.highest_rssi_value != None and rogue_ap.detecting_aps != None]
            else:
                rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps.rogue_aps_list if
                             rogue_ap.rssi_value != None and rogue_ap.detecting_aps != None]
            for rssi in range(-10, -100, -10):
                print('The number of rogue AP with highest RSSI ', rssi, ' dBm = ',
                      len(rogue_ap_rssi(wlc_config, rssi)))
            print('Split per frequency band: ')
            if wlc_config.platform == 'AireOS':
                print('2.4GHz: ',len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in wlc_config.rogue_aps if rogue_ap.band == '2.4GHz']))
                print(' 5 GHz: ',len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in wlc_config.rogue_aps if rogue_ap.band == '5GHz']))
            else:
                print('2.4GHz: ', len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in wlc_config.rogue_aps.rogue_aps_list if
                                       rogue_ap.band == '2.4GHz']))
                print(' 5 GHz: ', len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in  wlc_config.rogue_aps.rogue_aps_list if
                                       rogue_ap.band == '5GHz']))
            print('Currently hardcoded values for impact are: RSSI > -50 dBm and number of detecting APs > 3')
            if wlc_config.platform == 'AireOS':
                rogue_ap_list = [rogueap.name for rogueap in rogue_aps if
                                 int(rogueap.highest_rssi_value) > -50 and int(rogueap.detecting_aps) > 3]
                impacted_ap_mac_list = [rogueap.highest_rssi_ap for rogueap in rogue_aps if
                                        int(rogueap.highest_rssi_value) > -50 and int(rogueap.detecting_aps) > 3]
            else:
                rogue_ap_list = [rogueap.name for rogueap in rogue_aps if
                                 int(rogueap.rssi_value) > -50 and int(rogueap.detecting_aps) > 3]
                impacted_ap_mac_list = [rogueap.highest_rssi_ap for rogueap in rogue_aps if
                                        int(rogueap.rssi_value) > -50 and int(rogueap.detecting_aps) > 3]
            print('The most impacting rogue APs in this environment: ')
            for ap in rogue_ap_list:
                print(ap)
            print('The impacted APs in this environment: ')
            if wlc_config.platform == 'AireOS':
                impacted_ap_name_list = [ap.cisco_ap_name for ap in wlc_config.ap_configs if
                                         ap.slot_0_bssid in impacted_ap_mac_list]
                for ap in impacted_ap_name_list:
                    print(ap, '2.4 GHz utilization: ', wlc_config.ap_rf[ap + '_slot0'].load_profile_channel_utilization, ', 5 GHz utilization: ', wlc_config.ap_rf[ap + '_slot1'].load_profile_channel_utilization)
            else:
                impacted_ap_name_list = [ap.ap_name for ap in wlc_config.ap_slots if
                                         ap.station_configuration_bssid in impacted_ap_mac_list]
                for ap in impacted_ap_name_list:
                    print(ap, '2.4 GHz utilization: ', wlc_config.ap_rf_24[ap + '_slot0'].load_information_channel_utilization, ', 5 GHz utilization: ', wlc_config.ap_rf_5[ap + '_slot1'].load_information_channel_utilization)
            manufacturer_list, manufacturer_counter = manufacturer([rogue_ap.name for rogue_ap in rogue_aps])
            print('Most common manufacturers of rogue APs are: ', manufacturer_counter.most_common(5))
            print('Top-10 rogue APs by clients number: ')
            print(sorted([(int(ap.rogue_clients_number), ap.name) for ap in rogue_aps if
                          int(ap.rogue_clients_number) > 0],
                         reverse=True)[:10])
            return None, None  # rogue_ap_list,impacted_ap_list
    else:
        print('This function works only with WLC config objects')
        return None, None
    return None, None


def rogue_ap_summary_site(wlc_config, printout=False, rssi_threshold=-50, detecting_aps=3, rogue_clients=0,
                          site_name='', bands = ['2.4GHz','5GHz']):
    # Slightly changed function rogue_ap_summary.
    # Adds filtering per site (site_name in AP name in impacted ap list)
    # Adds RSSI threshold and number of detecting APs as input parameter (default values are -50 dBm and 3)
    if isinstance(wlc_config, Wlc_Config):
        if '8.3' in wlc_config.software_version or '8.5' in wlc_config.software_version or '8.8' in wlc_config.software_version:
            if printout:
                print('Rogue AP summary for ', wlc_config.hostname, ' and site ', site_name, ':')
                print('Filter for possible impact: RSSI >= ',rssi_threshold, ', number of detecting APs >= ',detecting_aps,', number of rogue clients >= ', rogue_clients, ', band ', bands)

            # Filter rogue AP list for AP with not None values in rssi and # of detecting APs
            rogue_aps = [rogue_ap for rogue_ap in wlc_config.rogue_aps if
                         rogue_ap.highest_rssi_value != None and rogue_ap.detecting_aps != None and rogue_ap.rogue_clients_number != None and rogue_ap.band in bands]
            # Filter lists by defined thresholds
            impacted_ap_mac_list = [rogueap.highest_rssi_ap for rogueap in rogue_aps if
                                    (int(rogueap.highest_rssi_value) >= rssi_threshold and int(
                                        rogueap.detecting_aps) >= detecting_aps and int(
                                        rogueap.rogue_clients_number) >= rogue_clients)]
            #Add also 2nd highest RSSI AP
            for ap_mac in [rogueap.second_rssi_ap for rogueap in rogue_aps if
                                    (int(rogueap.highest_rssi_value) >= rssi_threshold and int(
                                        rogueap.detecting_aps) >= detecting_aps and int(
                                        rogueap.rogue_clients_number) >= rogue_clients)]:
                impacted_ap_mac_list.append(ap_mac)

            impacted_ap_name_list = [ap.cisco_ap_name for ap in wlc_config.ap_configs if
                                     (ap.slot_0_bssid in impacted_ap_mac_list)]
            # Filter lists by site name
            site_impacted_ap_name_list = [ap.cisco_ap_name for ap in wlc_config.ap_configs if
                                          (ap.slot_0_bssid in impacted_ap_mac_list and site_name in ap.cisco_ap_name)]
            site_impacted_ap_mac_list = [ap.slot_0_bssid for ap in wlc_config.ap_configs if
                                         (ap.slot_0_bssid in impacted_ap_mac_list and site_name in ap.cisco_ap_name)]
            site_impacted_ap_dict = dict([(ap.slot_0_bssid, ap.cisco_ap_name) for ap in wlc_config.ap_configs if
                                          (ap.slot_0_bssid in impacted_ap_mac_list and site_name in ap.cisco_ap_name)])
            site_rogue_ap_list = [rogueap.name for rogueap in rogue_aps if
                                  (int(rogueap.highest_rssi_value) >= rssi_threshold and int(
                                      rogueap.detecting_aps) >= detecting_aps and
                                   int(rogueap.rogue_clients_number) >= rogue_clients and
                                   (rogueap.highest_rssi_ap in site_impacted_ap_mac_list or rogueap.second_rssi_ap in site_impacted_ap_mac_list))]

            site_rogue_impact_ap_list = [(rogueap.name, rogueap.highest_rssi_ap) for rogueap in rogue_aps if
                                         (int(rogueap.highest_rssi_value) >= rssi_threshold and int(
                                             rogueap.detecting_aps) >= detecting_aps and
                                          int(rogueap.rogue_clients_number) >= rogue_clients and
                                          (rogueap.highest_rssi_ap in site_impacted_ap_mac_list or rogueap.second_rssi_ap in site_impacted_ap_mac_list))]
            site_impacted_ap_utilization2_dict = {}
            site_impacted_ap_utilization5_dict = {}
            if printout: print('The number of rogue APs impacting this site: ', len(site_rogue_ap_list))
            if printout: print('Split per frequency band: ')
            if printout: print('2.4GHz: ',len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in wlc_config.rogue_aps if rogue_ap.band == '2.4GHz' and rogue_ap.name in site_rogue_ap_list]))
            if printout: print(' 5 GHz: ',len([(rogue_ap.name, rogue_ap.channel) for rogue_ap in wlc_config.rogue_aps if rogue_ap.band == '5GHz' and rogue_ap.name in site_rogue_ap_list]))
            if printout: print('The rogue APs at this site that filtered for impact threshold values: ')
            if printout:
                for ap in site_rogue_ap_list:
                    our_ap_names = [our_ap.cisco_ap_name for our_ap in wlc_config.ap_configs if our_ap.slot_0_bssid == wlc_config.rogue_aps[ap].highest_rssi_ap or our_ap.slot_0_bssid == wlc_config.rogue_aps[ap].second_rssi_ap]
                    print('BSSID: ', ap, ' band: ',wlc_config.rogue_aps[ap].band, ' channel: ',wlc_config.rogue_aps[ap].channel,', our highest RSSI APs: ',our_ap_names)

            if printout: print('The (possibly) impacted APs at this site: ')
            for ap in site_impacted_ap_name_list:
                if printout: print(ap, '2.4 GHz channel: ',wlc_config.ap_rf[ap + '_slot0'].channel_assignment_information_recommended_best_channel,', utilization: ', wlc_config.ap_rf[ap + '_slot0'].load_profile_channel_utilization,
                                   ', 5 GHz channel: ', wlc_config.ap_rf[ap + '_slot1'].channel_assignment_information_recommended_best_channel,', utilization: ', wlc_config.ap_rf[ap + '_slot1'].load_profile_channel_utilization)
                site_impacted_ap_utilization2_dict[ap] = int(
                    wlc_config.ap_rf[ap + '_slot0'].load_profile_channel_utilization[:-1])
                site_impacted_ap_utilization5_dict[ap] = int(
                    wlc_config.ap_rf[ap + '_slot1'].load_profile_channel_utilization[:-1])
            manufacturer_list, manufacturer_counter = manufacturer([rogue_ap for rogue_ap in site_rogue_ap_list])
            if printout: print('Most common manufacturers of rogue APs are: ', manufacturer_counter.most_common(5))
            if printout: print('Top-10 rogue APs by clients number: ')
            if printout: print(sorted([(int(ap.rogue_clients_number), ap.name) for ap in wlc_config.rogue_aps if
                                       (int(ap.rogue_clients_number) > 0 and ap.name in site_rogue_ap_list and ap.band in bands)],
                                      reverse=True)[:10])
            if printout:
                for rogue_mac, ap_mac in site_rogue_impact_ap_list:
                    try:
                        ap_name = site_impacted_ap_dict[ap_mac]
                        print(rogue_mac, site_impacted_ap_dict[ap_mac], site_impacted_ap_utilization2_dict[ap_name],
                              site_impacted_ap_utilization5_dict[ap_name])
                    except:
                        pass
            return site_rogue_impact_ap_list, site_impacted_ap_dict, site_impacted_ap_utilization2_dict, site_impacted_ap_utilization5_dict  # rogue_ap_list,impacted_ap_list
        else:
            print('Not supported in this software version because there are no RSSI values')
            return None, None
    else:
        print('This function works only with WLC config objects')
        return None, None
    return None, None


def rogue_ap_time(archive, rssi_threshold=-50, detecting_aps=3, rogue_clients=0, site_name=''):
    # This function is the most advanced rogue analysis in this script version :)
    # Takes as input archive of WLC configs taken in time and thresholds for impact
    # Returns ...
    impacted_ap_full_dict = {}
    rogue_ap = []
    rogue_impact_ap = []
    util2 = []
    util5 = []
    for item in archive.values():
        for wlc_config in item.values():
            site_rogue_impact_ap_list, impacted_ap_dict, impacted_ap_util2_dict, impacted_ap_util5_dict = rogue_ap_summary_site(
                wlc_config, False, rssi_threshold, detecting_aps, rogue_clients, site_name)
            for key, value in impacted_ap_dict.items():
                if key not in impacted_ap_full_dict:
                    impacted_ap_full_dict[key] = value
            rogue_impact_ap.append(site_rogue_impact_ap_list)
            util2.append(impacted_ap_util2_dict)
            util5.append(impacted_ap_util5_dict)
    # count_impacted_ap = Counter(x for sublist in impacted_ap for x in sublist)
    count_rogue_impact_ap = Counter(x for sublist in rogue_impact_ap for x in sublist)
    for (rogue_ap, impact_ap_mac), frequency in count_rogue_impact_ap.items():
        if int(frequency) >= 3:
            #find channel to display
            for item in archive.values():
                for wlc_config in item.values():
                    try:
                        rogue_channel = wlc_config.rogue_aps[rogue_ap].channel
                        ap_channels = [wlc_config.ap_rf[impacted_ap_full_dict[impact_ap_mac]+'_slot0'].channel_assignment_information_recommended_best_channel]
                        ap_channels.append(wlc_config.ap_rf[impacted_ap_full_dict[
                                                            impact_ap_mac] + '_slot1'].channel_assignment_information_recommended_best_channel)
                    except:
                        pass
            print('Rogue AP MAC address: ', rogue_ap, ' Frequency: ', frequency, ' Rogue AP channel: ',rogue_channel,' Impacted AP name: ',
                  impacted_ap_full_dict[impact_ap_mac],' AP channels: ',ap_channels)
            try:
                if len(manufacturer([rogue_ap])[0])>0:
                    print('Rogue AP vendor: ', manufacturer([rogue_ap])[0])
                else:
                    print('Rogue AP vendor is not found')

            except:
                print('Rogue AP vendor is not found')
            util = []
            for time_slice in util2:
                if impacted_ap_full_dict[impact_ap_mac] in time_slice:
                    util.append(time_slice[impacted_ap_full_dict[impact_ap_mac]])
            print('Average channel utilization 2.4 GHz = ', round(sum(util) / len(util), 2), end=' ')
            print('Channel utilization history 2.4 GHz:  ', util)
            util = []
            for time_slice in util5:
                if impacted_ap_full_dict[impact_ap_mac] in time_slice:
                    util.append(time_slice[impacted_ap_full_dict[impact_ap_mac]])
            print('Average channel utilization    5 GHz = ', round(sum(util) / len(util), 2), end=' ')
            print('Channel utilization history    5 GHz:  ', util)
            print('_____________________________________')
    return None


def number_of_rogue_aps(wlc_config, ap_name):
    if wlc_config.platform == 'AireOS':
        bssid = wlc_config.ap_configs[ap_name].slot_0_bssid
        return Counter([rogue.highest_rssi_ap for rogue in wlc_config.rogue_aps])[bssid] + \
               Counter([rogue.second_rssi_ap for rogue in wlc_config.rogue_aps])[bssid]
    if wlc_config.platform == '9800':
        bssid = wlc_config.ap_slots[ap_name + '_slot0'].station_configuration_bssid
        return Counter([rogue.highest_rssi_ap for rogue in wlc_config.rogue_aps.rogue_aps_list])[bssid]