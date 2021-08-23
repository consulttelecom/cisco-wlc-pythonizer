# Channel utilization functions
import numpy as np
import matplotlib.pyplot as plt
import logging

def utilization_statistics(wlc_config, printout=False):
    # This funstion returns takes as input wlc_config object and returns average channel utilization per band
    logging.debug('Function utilization_statistics is called')
    util24 = []
    util5 = []
    if wlc_config.platform == 'AireOS':
        if len(wlc_config.ap_rf) > 0:
            for ap_slot in wlc_config.ap_rf:
                if ap_slot.load_profile_channel_utilization != None:
                    if 'slot1' in ap_slot.name:
                        util5.append(int(ap_slot.load_profile_channel_utilization[:-1]))
                    if 'slot0' in ap_slot.name:
                        util24.append(int(ap_slot.load_profile_channel_utilization[:-1]))
    else:
        if len(wlc_config.ap_rf_24) > 0:
            for ap_slot in wlc_config.ap_rf_24:
                if ap_slot.load_information_channel_utilization != None:
                    util24.append(int(ap_slot.load_information_channel_utilization[:-1]))
        if len(wlc_config.ap_rf_5) > 0:
            for ap_slot in wlc_config.ap_rf_5:
                if ap_slot.load_information_channel_utilization != None:
                    util5.append(int(ap_slot.load_information_channel_utilization[:-1]))
    average24 = sum(util24) / len(util24)
    average5 = sum(util5) / len(util5)
    max24 = max(util24)
    max5 = max(util5)
    min24 = min(util24)
    min5 = min(util5)
    if printout:
        print('Channel utilization 5GHz band for device', wlc_config.hostname)
        print('Average: ',average5, 'Min: ', min5, 'Max: ',max5)
        print('Channel utilization 2.4GHz band for device', wlc_config.hostname)
        print('Average: ',average24, 'Min: ', min24, 'Max: ', max24)
    return average24, min24, max24, average5, min5, max5



def bad_utilization_aps(wlc_config, utilization_diff_threshold, site_name=''):
    # This function takes ONE WLC config object and returns dictionary of AP name:utilization values
    # where channel utilization - (RX util + TX util) > threshold
    logging.debug('Function bad_utilization_aps is called')
    result = {}
    if wlc_config.platform == 'AireOS':
        for ap_radio in wlc_config.ap_rf:
            if site_name in ap_radio.name:
                channel_util = int(ap_radio.load_profile_channel_utilization[:-1])
                tx_util = int(ap_radio.load_profile_transmit_utilization[:-1])
                rx_util = int(ap_radio.load_profile_receive_utilization[:-1])
                if channel_util - tx_util - rx_util > utilization_diff_threshold:
                    result[ap_radio.name] = [channel_util, tx_util, rx_util]
    else:
        for ap_radio in wlc_config.ap_rf_24:
            if site_name in ap_radio.name:
                channel_util = int(ap_radio.load_information_channel_utilization[:-1])
                tx_util = int(ap_radio.load_information_transmit_utilization[:-1])
                rx_util = int(ap_radio.load_information_receive_utilization[:-1])
                if channel_util - tx_util - rx_util > utilization_diff_threshold:
                    result[ap_radio.name] = [channel_util, tx_util, rx_util]
        for ap_radio in wlc_config.ap_rf_5:
            if site_name in ap_radio.name:
                channel_util = int(ap_radio.load_information_channel_utilization[:-1])
                tx_util = int(ap_radio.load_information_transmit_utilization[:-1])
                rx_util = int(ap_radio.load_information_receive_utilization[:-1])
                if channel_util - tx_util - rx_util > utilization_diff_threshold:
                    result[ap_radio.name] = [channel_util, tx_util, rx_util]
    return result


def channel_utilization(archive):
    # This function takes the archive of wlc_configs in time and returns channel_utilization dictionary[wlc][band][ap_slot](list of channel util in time)
    logging.debug('Function channel_utilization is called')
    channel_utilization_changes = {}
    for config_time_slice in archive.keys():
        for device in archive[config_time_slice].keys():
            if device not in channel_utilization_changes:
                channel_utilization_changes[device] = {}
                channel_utilization_changes[device] = {}
                channel_utilization_changes[device]['5G'] = {}
                channel_utilization_changes[device]['2.4G'] = {}
            if archive[config_time_slice][device].platform == 'AireOS':
                for ap_slot in archive[config_time_slice][device].ap_rf:
                    if 'slot1' in ap_slot.name and ap_slot.name not in channel_utilization_changes[device]['5G']:
                        channel_utilization_changes[device]['5G'][ap_slot.name] = []
                    if 'slot0' in ap_slot.name and ap_slot.name not in channel_utilization_changes[device]['2.4G']:
                        channel_utilization_changes[device]['2.4G'][ap_slot.name] = []
                    if ap_slot.load_profile_channel_utilization != None:
                        if 'slot1' in ap_slot.name:
                            channel_utilization_changes[device]['5G'][ap_slot.name].append(
                                int(ap_slot.load_profile_channel_utilization[:-1]))
                        if 'slot0' in ap_slot.name:
                            channel_utilization_changes[device]['2.4G'][ap_slot.name].append(
                                int(ap_slot.load_profile_channel_utilization[:-1]))
            if archive[config_time_slice][device].platform == '9800':
                for ap_slot in archive[config_time_slice][device].ap_rf_5:
                    if 'slot1' in ap_slot.name and ap_slot.name not in channel_utilization_changes[device]['5G']:
                        channel_utilization_changes[device]['5G'][ap_slot.name] = []
                    if ap_slot.load_information_channel_utilization != None:
                        channel_utilization_changes[device]['5G'][ap_slot.name].append(
                            int(ap_slot.load_information_channel_utilization[:-1]))
                for ap_slot in archive[config_time_slice][device].ap_rf_24:
                    if 'slot0' in ap_slot.name and ap_slot.name not in channel_utilization_changes[device]['2.4G']:
                        channel_utilization_changes[device]['2.4G'][ap_slot.name] = []
                    if ap_slot.load_information_channel_utilization != None:
                        channel_utilization_changes[device]['2.4G'][ap_slot.name].append(
                            int(ap_slot.load_information_channel_utilization[:-1]))
    return channel_utilization_changes


def channel_utilization_visual(archive):
    # This function takes the archive of wlc_configs in time and returns channel_utilization dictionary[wlc][band][ap_slot](list of channel util in time)
    logging.debug('Function channel_utilization_visual is called')
    channel_utilization_changes = channel_utilization(archive)
    #When some AP added\removed from configs in archive, they will have the number of values < than max and can cause TypeError: Image data of dtype object cannot be converted to float
    max_number_of_values = 0
    for device in channel_utilization_changes.keys():
        for slot in channel_utilization_changes[device]['2.4G'].keys():
            max_number_of_values = max(len(channel_utilization_changes[device]['2.4G'][slot]), max_number_of_values)
    for device in channel_utilization_changes.keys():
        util_24_list = []
        util_5_list = []
        label_names2 = []
        label_names5 = []

        for slot in channel_utilization_changes[device]['2.4G'].keys():
            label_names2.append(slot)
            if len (channel_utilization_changes[device]['2.4G'][slot]) < max_number_of_values:
                util_24_list.append(channel_utilization_changes[device]['2.4G'][slot] + [100]*(max_number_of_values - len(channel_utilization_changes[device]['2.4G'][slot])))
            else:
                util_24_list.append(channel_utilization_changes[device]['2.4G'][slot])
        for slot in channel_utilization_changes[device]['5G'].keys():
            label_names5.append(slot)
            if len(channel_utilization_changes[device]['5G'][slot]) < max_number_of_values:
                util_5_list.append(channel_utilization_changes[device]['5G'][slot] + [100] * (
                            max_number_of_values - len(channel_utilization_changes[device]['5G'][slot])))
            else:
                util_5_list.append(channel_utilization_changes[device]['5G'][slot])



    # prepare arrays for visualization

    util2 = np.array(util_24_list)
    util5 = np.array(util_5_list)
    fig, axs = plt.subplots(1, 2, figsize=(12, 8))  # constrained_layout=True,
    fig.suptitle('Channel utilization over time', fontsize=16)
    axs[0].set_yticks(np.arange(len(util_24_list)))
    plt.yticks(fontsize=8)
    axs[0].set_yticklabels(label_names2, fontsize=8)
    axs[0].set_title('2.4 GHz')
    axs[1].set_yticks(np.arange(len(util_5_list)))
    axs[1].set_title('5 GHz')
    axs[1].set_yticklabels(label_names5, fontsize=8)
    im = axs[0].imshow(util2, cmap='Reds', vmin=0, vmax=100)
    im = axs[1].imshow(util5, cmap='Reds', vmin=0, vmax=100)
    # heatmap2 = plt.pcolor(util2)
    # heatmap5 = plt.pcolor(util5)
    # fig.colorbar([0,100], ax = axs[0])
    # fig.colorbar([0,100], ax = axs[1])
    fig.colorbar(im, ax=axs[:], shrink=0.6)
    # fig.colorbar(im)
    return channel_utilization_changes


def utilization_time(archive, site_name='', average_util2_threshold=0, average_util5_threshold=0):
    # Slight modification of function channel_utilization_visual(), added the site name for filtering APs by the name of site they installed
    # This function takes the archive of wlc_configs in time
    # and returns channel_utilization dictionary[wlc][band][ap_slot](list of channel util in time)
    logging.debug('Function utilization_time is called')
    channel_utilization_changes = channel_utilization(archive)
    #When some AP added\removed from configs in archive, they will have the number of values < than max and can cause TypeError: Image data of dtype object cannot be converted to float
    max_number_of_values = 0
    for device in channel_utilization_changes.keys():
        for slot in channel_utilization_changes[device]['2.4G'].keys():
            max_number_of_values = max(len(channel_utilization_changes[device]['2.4G'][slot]), max_number_of_values)
    for device in channel_utilization_changes.keys():
        util_24_list = []
        util_5_list = []
        label_names2 = []
        label_names5 = []

        for slot in channel_utilization_changes[device]['2.4G'].keys():
            if site_name in slot and sum(channel_utilization_changes[device]['2.4G'][slot]) / len(
                    channel_utilization_changes[device]['2.4G'][slot]) >= average_util2_threshold:
                label_names2.append(slot)
                if len(channel_utilization_changes[device]['2.4G'][slot]) < max_number_of_values:
                    util_24_list.append(channel_utilization_changes[device]['2.4G'][slot] + [100] * (
                                max_number_of_values - len(channel_utilization_changes[device]['2.4G'][slot])))
                else:
                    util_24_list.append(channel_utilization_changes[device]['2.4G'][slot])
        for slot in channel_utilization_changes[device]['5G'].keys():
            if site_name in slot and sum(channel_utilization_changes[device]['5G'][slot]) / len(
                    channel_utilization_changes[device]['5G'][slot]) >= average_util5_threshold:
                label_names5.append(slot)
                if len(channel_utilization_changes[device]['5G'][slot]) < max_number_of_values:
                    util_5_list.append(channel_utilization_changes[device]['5G'][slot] + [100] * (
                            max_number_of_values - len(channel_utilization_changes[device]['5G'][slot])))
                else:
                    util_5_list.append(channel_utilization_changes[device]['5G'][slot])
    # prepare arrays for visualization

    util2 = np.array(util_24_list)
    util5 = np.array(util_5_list)
    fig, axs = plt.subplots(1, 2, figsize=(12, 8))  # constrained_layout=True,
    # fig.tight_layout()
    fig.suptitle('Channel utilization over time', fontsize=16)
    axs[0].set_yticks(np.arange(len(util_24_list)))
    plt.yticks(fontsize=8)
    axs[0].set_yticklabels(label_names2, fontsize=6)
    axs[0].set_title('2.4 GHz')
    axs[1].set_yticks(np.arange(len(util_5_list)))
    axs[1].set_title('5 GHz')
    axs[1].set_yticklabels(label_names5, fontsize=6)
    im = axs[0].imshow(util2, cmap='Reds', vmin=0, vmax=100)
    im = axs[1].imshow(util5, cmap='Reds', vmin=0, vmax=100)
    # heatmap2 = plt.pcolor(util2)
    # heatmap5 = plt.pcolor(util5)
    # fig.colorbar([0,100], ax = axs[0])
    # fig.colorbar([0,100], ax = axs[1])
    fig.colorbar(im, ax=axs[:], shrink=0.6)
    # fig.colorbar(im)
    return channel_utilization_changes


# Nice matplotlib function for visualization
def scatter_histogram(a, b, title, x_label, y_label):
    x = np.array(a)
    y = np.array(b)
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.2]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    # start with a rectangular Figure
    plt.figure(figsize=(8, 8))
    plt.suptitle(title, fontsize=16)

    ax_scatter = plt.axes(rect_scatter)
    ax_scatter.tick_params(direction='in', top=True, right=True)
    ax_histx = plt.axes(rect_histx)
    ax_histx.tick_params(direction='in', labelbottom=False)
    ax_histy = plt.axes(rect_histy)
    ax_histy.tick_params(direction='in', labelleft=False)

    # the scatter plot:
    ax_scatter.set_xlabel(x_label, fontsize=10)
    ax_scatter.set_ylabel(y_label, fontsize=10)
    # plt.ylabel('y_label', fontsize=8)
    ax_scatter.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    lim_x = np.ceil(np.abs([x]).max() / binwidth) * binwidth
    lim_y = np.ceil(np.abs([y]).max() / binwidth) * binwidth
    ax_scatter.set_xlim((0, lim_x))
    ax_scatter.set_ylim((0, lim_y + 1))  # +1 to prevent axis numbers in the same place of diagram

    bins_x = np.arange(0, lim_x + binwidth, binwidth)
    bins_y = np.arange(0, lim_y + binwidth, binwidth)
    ax_histx.hist(x, bins=bins_x)
    ax_histy.hist(y, bins=bins_y, orientation='horizontal')

    ax_histx.set_xlim(ax_scatter.get_xlim())
    ax_histy.set_ylim(ax_scatter.get_ylim())

    plt.show()


def utilization_clients_scatterplot(wlc_config):
    # Function that draws scatterplot for (Utilization vs NUMBER OF CLIENTS) for every AP in wlc_config
    logging.debug('Function utilization_clients_scatterplot is called')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
        b = [int(ap.load_profile_attached_clients[:-7]) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_24]
        b = [int(ap.load_information_attached_clients[:-7]) for ap in wlc_config.ap_rf_24]
    scatter_histogram(a, b, '2.4 GHz channel utilization vs Number of clients', 'Channel utilization',
                      'Number of clients')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
        b = [int(ap.load_profile_attached_clients[:-7]) for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_5]
        b = [int(ap.load_information_attached_clients[:-7]) for ap in wlc_config.ap_rf_5]
    scatter_histogram(a, b, '5 GHz channel utilization vs Number of clients', 'Channel utilization',
                      'Number of clients')
    return None


def utilization_nearby_aps_scatterplot(wlc_config):
    # Function that draws scatterplot for (Utilization vs NUMBER OF NEARBY APs) for every AP in wlc_config
    logging.debug('Function utilization_nearby_aps_scatterplot is called')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
        b = [len(ap.nearby_aps) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_24]
        b = [len(ap.nearby_aps) for ap in wlc_config.ap_rf_24]
    scatter_histogram(a, b, '2.4 GHz channel utilization vs Number of nearby APs', 'Channel utilization',
                          'Number of nearby APs')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
        b = [len(ap.nearby_aps)  for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_5]
        b = [len(ap.nearby_aps) for ap in wlc_config.ap_rf_5]
    scatter_histogram(a, b, '5 GHz channel utilization vs Number of nearby APs', 'Channel utilization',
                          'Number of nearby APs')
    return None


def utilization_same_channel_nearby_aps_scatterplot(wlc_config):
    # Function that draws scatterplot for (Utilization vs NUMBER OF NEARBY APs on the SAME channel) for every AP in archive
    logging.debug('Function utilization_same_channel_nearby_aps_scatterplot is called')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
        b = [len(nearby_aps_same_channel(ap)) for ap in
             wlc_config.ap_rf if 'slot0' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_24]
        b = [len(nearby_aps_same_channel(ap)) for ap in
             wlc_config.ap_rf_24]
    scatter_histogram(a, b, '2.4 GHz channel utilization vs Number of nearby APs', 'Channel utilization',
                      'Number of nearby APs (on the same channel)')
    if wlc_config.platform == 'AireOS':
        a = [int(ap.load_profile_channel_utilization[:-1]) for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
        b = [len(nearby_aps_same_channel(ap)) for ap in
             wlc_config.ap_rf if 'slot1' in ap.name]
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_5]
        b = [len(nearby_aps_same_channel(ap)) for ap in
             wlc_config.ap_rf_5]

    scatter_histogram(a, b, '5 GHz channel utilization vs Number of nearby APs', 'Channel utilization',
                      'Number of nearby APs (one the same channel')
    return None


def utilization_rogue_aps_scatterplot(wlc_config):
    # Function that draws scatterplot for (Utilization vs NUMBER OF ROGUE APs) for every AP in ONE WLC config
    logging.debug('Function utilization_rogue_aps_scatterplot is called')
    a = []  # AP 2.4 GHz channel utilization
    b = []  # Number of rogue APs reported by this AP
    if wlc_config.platform == 'AireOS':
        for ap in wlc_config.ap_configs:
            bssid = wlc_config.ap_configs[ap.name].slot_0_bssid
            if ap.name + '_slot0' in [ap.name for ap in
                                      wlc_config.ap_rf]:  # Sometimes AP name in AP general config does not correspond to AP name if AP RF config
                a.append(int(wlc_config.ap_rf[ap.name + '_slot0'].load_profile_channel_utilization[:-1]))
                b.append(len([rogue.name for rogue in wlc_config.rogue_aps if
                              (rogue.highest_rssi_ap == bssid or rogue.second_rssi_ap == bssid) and '2.4' in rogue.band]))
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_24]
        for ap in [slot for slot in wlc_config.ap_slots if 'slot0' in slot.name]:
            bssid = ap.station_configuration_bssid
            b.append(len([rogue.name for rogue in wlc_config.rogue_aps.rogue_aps_list if
                          (rogue.highest_rssi_ap == bssid) and '2.4' in rogue.band]))
    scatter_histogram(a, b, 'Channel utilization in 2.4GHz band vs number of rogues', 'Utilization',
                      '# of rogues heard by AP')
    a = []  # AP 5 GHz channel utilization
    b = []  # Number of rogue AP reported by this AP
    if wlc_config.platform == 'AireOS':
        for ap in wlc_config.ap_configs:
            bssid = wlc_config.ap_configs[ap.name].slot_0_bssid
            if ap.name + '_slot1' in [ap.name for ap in
                                      wlc_config.ap_rf]:  # Sometimes AP name in AP general config does not correspond to AP name if AP RF config
                a.append(int(wlc_config.ap_rf[ap.name + '_slot1'].load_profile_channel_utilization[:-1]))
                b.append(len([rogue.name for rogue in wlc_config.rogue_aps if
                              rogue.highest_rssi_ap == bssid or rogue.second_rssi_ap == bssid and '5' in rogue.band]))
    else:
        a = [int(ap.load_information_channel_utilization[:-1]) for ap in wlc_config.ap_rf_5]
        for ap in [slot for slot in wlc_config.ap_slots if 'slot1' in slot.name]:
            bssid = ap.station_configuration_bssid
            b.append(len([rogue.name for rogue in wlc_config.rogue_aps.rogue_aps_list if
                          (rogue.highest_rssi_ap == bssid) and '5' in rogue.band]))
    scatter_histogram(a, b, 'Channel utilization in 5GHz band vs number of rogues', 'Utilization',
                      '# of rogues heard by AP')
    return None

# Nearby APs useful functions
def nearby_aps_same_channel(ap_rf):
    # returns the number of Nearby APs on the same channel for AireOS and 9800 platform
    return [nearbyap.mac_address for nearbyap in ap_rf.nearby_aps if
            ap_rf.channel_assignment_information_recommended_best_channel == nearbyap.channel]