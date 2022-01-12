import logging

#Common functions for customized objects
def show(object_instance):
    if hasattr(object_instance, 'objname') == False:
        print('ERROR: Show function should be used only for customized classes!!!')
        return None
    if isinstance(object_instance, NamedList):  # For NAMED LISTS
        for index, item in enumerate(object_instance):
            show(item)
    for attr, value in object_instance.__dict__.items():
        # print(type(value))
        if isinstance(value, NamedList):  # For NAMED LISTS
            for item in value:
                show(item)
        else:
            print(attr, value)


def grep(object_instance, keyword):
    # Function to find attributes and values in objects by keyword
    if hasattr(object_instance, 'objname') == False:
        print('ERROR: GREP function should be used only for customized classes!!!')
        return None
    if isinstance(object_instance, NamedList):  # For NAMED LISTS
        for index, item in enumerate(object_instance):
            grep(item, keyword)
    for attr, value in object_instance.__dict__.items():
        if isinstance(value, NamedList):  # For NAMED LISTS
            for item in value:
                grep(item, keyword)
        else:
            if keyword in attr:
                print(object_instance, attr, value)
            if hasattr(value, 'objname'):
                grep(value, keyword)
            if value is not None and hasattr(value, 'objname') == False:
                if keyword in value:
                    print(object_instance, attr, value)


#Customized classes descriptions section
class NamedList(list):  # Special class to refer to its name in object tree
    def __init__(self, list_name, item_name):
        self.objname = list_name
        self.item_name = item_name

    def __getitem__(self, name):
        x = NamedList(self.objname, self.item_name)  # Clone the same object type as called
        for item in self:
            if item.name == name:
                x.append(item)
        if len(x) == 1:  # if only one item should be returned - no need to return the list
            copied_list = x.copy()
            return copied_list.pop()  # Should do pop() only for list copy to make list unchanged
        elif len(x) == 0:
            if name is not None:
                print('WARNING! Zero elements with name ', name, ' was found ')
            return x
        else:
            print('WARNING! More than one element with name ', name,
                  ' was found. Use filter() to find necessary item by matching other attributes')
            return x

    def filter(self, attrname, required_value):
        x = NamedList(self.objname, self.item_name)  # Clone the same object type as called
        for item in self:
            try:
                real_value = getattr(item, attrname)
                if real_value == required_value:
                    x.append(item)

            except KeyError as e:
                print('No attribute with name ', attrname)
                return None
            except:
                print('Other error ')
                return None
        if len(x) == 1:  # if only one item should be returned - no need to return the list
            copied_list = x.copy()
            return copied_list.pop()  # Should do pop() only for list copy to make list unchanged
        else:
            return x

    def __str__(self):
        x = ''
        item_objname = ''
        length = len(self)
        if length == 0:
            return 'Named List of length ' + str(length) + ' with items ' + self.item_name
        for index, item in enumerate(self):
            x = x + ' ' + item.name + ', '
            item_objname = item.objname
        x = 'Named List of length ' + str(length) + ' with items ' + self.item_name + ':' + x
        return x[:-2]

    def __repr__(self):
        x = ''
        item_objname = ''
        length = len(self)
        if length == 0:
            return 'Named List of length ' + str(length) + ' with items ' + self.item_name
        for index, item in enumerate(self):
            x = x + ' ' + item.name + ', '
            item_objname = item.objname
        x = 'Named List of length ' + str(length) + ' with items ' + self.item_name + ':' + x
        return x[:-2]

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Band24_Config():
    def __init__(self, name=None):
        self.objname = '2.4GHz config'
        self.name = '2.4GHz config'
        self.type = 'config'  # defines if class contain operational or config data
        self.d_802_11b_network = None
        self.d_11gsupport = None
        self.d_11nsupport = None
        self.d_802_11b_g_operational_rates = None
        self.d_802_11b_g_operational_rates_802_11b_g_1m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_2m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_5_5m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_11m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_6m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_9m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_12m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_18m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_24m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_36m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_48m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_54m_rate = None
        self.d_802_11n_mcs_settings = None
        self.d_802_11n_mcs_settings_mcs_0 = None
        self.d_802_11n_mcs_settings_mcs_1 = None
        self.d_802_11n_mcs_settings_mcs_2 = None
        self.d_802_11n_mcs_settings_mcs_3 = None
        self.d_802_11n_mcs_settings_mcs_4 = None
        self.d_802_11n_mcs_settings_mcs_5 = None
        self.d_802_11n_mcs_settings_mcs_6 = None
        self.d_802_11n_mcs_settings_mcs_7 = None
        self.d_802_11n_mcs_settings_mcs_8 = None
        self.d_802_11n_mcs_settings_mcs_9 = None
        self.d_802_11n_mcs_settings_mcs_10 = None
        self.d_802_11n_mcs_settings_mcs_11 = None
        self.d_802_11n_mcs_settings_mcs_12 = None
        self.d_802_11n_mcs_settings_mcs_13 = None
        self.d_802_11n_mcs_settings_mcs_14 = None
        self.d_802_11n_mcs_settings_mcs_15 = None
        self.d_802_11n_mcs_settings_mcs_16 = None
        self.d_802_11n_mcs_settings_mcs_17 = None
        self.d_802_11n_mcs_settings_mcs_18 = None
        self.d_802_11n_mcs_settings_mcs_19 = None
        self.d_802_11n_mcs_settings_mcs_20 = None
        self.d_802_11n_mcs_settings_mcs_21 = None
        self.d_802_11n_mcs_settings_mcs_22 = None
        self.d_802_11n_mcs_settings_mcs_23 = None
        self.d_802_11n_mcs_settings_mcs_24 = None
        self.d_802_11n_mcs_settings_mcs_25 = None
        self.d_802_11n_mcs_settings_mcs_26 = None
        self.d_802_11n_mcs_settings_mcs_27 = None
        self.d_802_11n_mcs_settings_mcs_28 = None
        self.d_802_11n_mcs_settings_mcs_29 = None
        self.d_802_11n_mcs_settings_mcs_30 = None
        self.d_802_11n_mcs_settings_mcs_31 = None
        self.d_802_11n_status = None
        self.d_802_11n_status_a_mpdu_tx = None
        self.d_802_11n_status_a_mpdu_tx_priority_0 = None
        self.d_802_11n_status_a_mpdu_tx_priority_1 = None
        self.d_802_11n_status_a_mpdu_tx_priority_2 = None
        self.d_802_11n_status_a_mpdu_tx_priority_3 = None
        self.d_802_11n_status_a_mpdu_tx_priority_4 = None
        self.d_802_11n_status_a_mpdu_tx_priority_5 = None
        self.d_802_11n_status_a_mpdu_tx_priority_6 = None
        self.d_802_11n_status_a_mpdu_tx_priority_7 = None
        self.d_802_11n_status_a_mpdu_tx_aggregation_scheduler = None
        self.d_802_11n_status_a_mpdu_tx_aggregation_scheduler_realtime_timeout = None
        self.d_802_11n_status_a_mpdu_tx_aggregation_scheduler_non_realtime_timeout = None
        self.d_802_11n_status_a_msdu_tx = None
        self.d_802_11n_status_a_msdu_tx_priority_0 = None
        self.d_802_11n_status_a_msdu_tx_priority_1 = None
        self.d_802_11n_status_a_msdu_tx_priority_2 = None
        self.d_802_11n_status_a_msdu_tx_priority_3 = None
        self.d_802_11n_status_a_msdu_tx_priority_4 = None
        self.d_802_11n_status_a_msdu_tx_priority_5 = None
        self.d_802_11n_status_a_msdu_tx_priority_6 = None
        self.d_802_11n_status_a_msdu_tx_priority_7 = None
        self.d_802_11n_status_a_msdu_max_subframes = None
        self.d_802_11n_status_a_msdu_max_length = None
        self.d_802_11n_status_rifs_rx = None
        self.d_802_11n_status_guard_interval = None
        self.beacon_interval = None
        self.cf_pollable_mode = None
        self.cf_poll_request_mandatory = None
        self.cfp_period = None
        self.cfp_maximum_duration = None
        self.default_channel = None
        self.default_tx_power_level = None
        self.dtpc_status = None
        self.rssi_low_check = None
        self.rssi_threshold = None
        self.call_admission_limit = None
        self.g711_cu_quantum = None
        self.ed_threshold = None
        self.fragmentation_threshold = None
        self.pbcc_mandatory = None
        self.rts_threshold = None
        self.short_preamble_mandatory = None
        self.short_retry_limit = None
        self.legacy_tx_beamforming_setting = None
        self.traffic_stream_metrics_status = None
        self.expedited_bw_request_status = None
        self.world_mode = None
        self.faster_carrier_tracking_loop = None
        self.edca_profile_type = None
        self.voice_mac_optimization_status = None
        self.call_admission_control_cac_configuration = None
        self.call_admission_control_cac_configuration_voice_ac_admission_control_acm = None
        self.call_admission_control_cac_configuration_voice_stream_size = None
        self.call_admission_control_cac_configuration_voice_max_streams = None
        self.call_admission_control_cac_configuration_voice_max_rf_bandwidth = None
        self.call_admission_control_cac_configuration_voice_reserved_roaming_bandwidth = None
        self.call_admission_control_cac_configuration_voice_cac_method = None
        self.call_admission_control_cac_configuration_voice_tspec_inactivity_timeout = None
        self.cac_sip_voice_configuration = None
        self.cac_sip_voice_configuration_sip_based_cac = None
        self.cac_sip_voice_configuration_sip_codec_type = None
        self.cac_sip_voice_configuration_sip_call_bandwidth = None
        self.cac_sip_voice_configuration_sip_call_bandwidth_sample_size = None
        self.cac_sip_voice_configuration_video_ac_admission_control_acm = None
        self.cac_sip_voice_configuration_video_max_rf_bandwidth = None
        self.cac_sip_voice_configuration_video_reserved_roaming_bandwidth = None
        self.cac_sip_voice_configuration_video_load_based_cac_mode = None
        self.cac_sip_voice_configuration_video_cac_method = None
        self.cac_sip_video_configuration = None
        self.cac_sip_video_configuration_sip_based_cac = None
        self.cac_sip_video_configuration_best_effort_ac_admission_control_acm = None
        self.cac_sip_video_configuration_background_ac_admission_control_acm = None
        self.maximum_number_of_clients_per_ap = None
        self.l2roam_802_11bg_rf_parameters = None
        self.l2roam_802_11bg_rf_parameters_config_mode = None
        self.l2roam_802_11bg_rf_parameters_minimum_rssi = None
        self.l2roam_802_11bg_rf_parameters_roam_hysteresis = None
        self.l2roam_802_11bg_rf_parameters_scan_threshold = None
        self.l2roam_802_11bg_rf_parameters_transition_time = None

    def __str__(self):
        return '802.11b network config'

    def __repr__(self):
        return '802.11b network config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Band5_Config():
    def __init__(self, name=None):
        self.objname = '5GHz config'
        self.name = '5GHz config'
        self.type = 'config'  # defines if class contain operational or config data
        self.d_802_11a_network = None
        self.d_11acsupport = None
        self.d_11nsupport = None
        self.d_11nsupport_802_11a_low_band = None
        self.d_11nsupport_802_11a_mid_band = None
        self.d_11nsupport_802_11a_high_band = None
        self.d_802_11a_operational_rates = None
        self.d_802_11a_operational_rates_802_11a_6m_rate = None
        self.d_802_11a_operational_rates_802_11a_9m_rate = None
        self.d_802_11a_operational_rates_802_11a_12m_rate = None
        self.d_802_11a_operational_rates_802_11a_18m_rate = None
        self.d_802_11a_operational_rates_802_11a_24m_rate = None
        self.d_802_11a_operational_rates_802_11a_36m_rate = None
        self.d_802_11a_operational_rates_802_11a_48m_rate = None
        self.d_802_11a_operational_rates_802_11a_54m_rate = None
        self.d_802_11n_mcs_settings = None
        self.d_802_11n_mcs_settings_mcs_0 = None
        self.d_802_11n_mcs_settings_mcs_1 = None
        self.d_802_11n_mcs_settings_mcs_2 = None
        self.d_802_11n_mcs_settings_mcs_3 = None
        self.d_802_11n_mcs_settings_mcs_4 = None
        self.d_802_11n_mcs_settings_mcs_5 = None
        self.d_802_11n_mcs_settings_mcs_6 = None
        self.d_802_11n_mcs_settings_mcs_7 = None
        self.d_802_11n_mcs_settings_mcs_8 = None
        self.d_802_11n_mcs_settings_mcs_9 = None
        self.d_802_11n_mcs_settings_mcs_10 = None
        self.d_802_11n_mcs_settings_mcs_11 = None
        self.d_802_11n_mcs_settings_mcs_12 = None
        self.d_802_11n_mcs_settings_mcs_13 = None
        self.d_802_11n_mcs_settings_mcs_14 = None
        self.d_802_11n_mcs_settings_mcs_15 = None
        self.d_802_11n_mcs_settings_mcs_16 = None
        self.d_802_11n_mcs_settings_mcs_17 = None
        self.d_802_11n_mcs_settings_mcs_18 = None
        self.d_802_11n_mcs_settings_mcs_19 = None
        self.d_802_11n_mcs_settings_mcs_20 = None
        self.d_802_11n_mcs_settings_mcs_21 = None
        self.d_802_11n_mcs_settings_mcs_22 = None
        self.d_802_11n_mcs_settings_mcs_23 = None
        self.d_802_11n_mcs_settings_mcs_24 = None
        self.d_802_11n_mcs_settings_mcs_25 = None
        self.d_802_11n_mcs_settings_mcs_26 = None
        self.d_802_11n_mcs_settings_mcs_27 = None
        self.d_802_11n_mcs_settings_mcs_28 = None
        self.d_802_11n_mcs_settings_mcs_29 = None
        self.d_802_11n_mcs_settings_mcs_30 = None
        self.d_802_11n_mcs_settings_mcs_31 = None
        self.d_802_11ac_mcs_settings = None
        self.d_802_11ac_mcs_settings_nss_1_mcs_0_9 = None
        self.d_802_11ac_mcs_settings_nss_2_mcs_0_9 = None
        self.d_802_11ac_mcs_settings_nss_3_mcs_0_9 = None
        self.d_802_11ac_mcs_settings_nss_4_mcs_0_7 = None
        self.d_802_11ac_mcs_settings_nss_4_mcs_0_9 = None
        self.d_802_11n_status = None
        self.d_802_11n_status_a_mpdu_tx = None
        self.d_802_11n_status_a_mpdu_tx_priority_0 = None
        self.d_802_11n_status_a_mpdu_tx_priority_1 = None
        self.d_802_11n_status_a_mpdu_tx_priority_2 = None
        self.d_802_11n_status_a_mpdu_tx_priority_3 = None
        self.d_802_11n_status_a_mpdu_tx_priority_4 = None
        self.d_802_11n_status_a_mpdu_tx_priority_5 = None
        self.d_802_11n_status_a_mpdu_tx_priority_6 = None
        self.d_802_11n_status_a_mpdu_tx_priority_7 = None
        self.d_802_11n_status_a_mpdu_tx_aggregation_scheduler = None
        self.d_802_11n_status_a_mpdu_tx_frame_burst = None
        self.d_802_11n_status_a_mpdu_tx_frame_burst_realtime_timeout = None
        self.d_802_11n_status_a_mpdu_tx_frame_burst_non_realtime_timeout = None
        self.d_802_11n_status_a_msdu_tx = None
        self.d_802_11n_status_a_msdu_tx_priority_0 = None
        self.d_802_11n_status_a_msdu_tx_priority_1 = None
        self.d_802_11n_status_a_msdu_tx_priority_2 = None
        self.d_802_11n_status_a_msdu_tx_priority_3 = None
        self.d_802_11n_status_a_msdu_tx_priority_4 = None
        self.d_802_11n_status_a_msdu_tx_priority_5 = None
        self.d_802_11n_status_a_msdu_tx_priority_6 = None
        self.d_802_11n_status_a_msdu_tx_priority_7 = None
        self.d_802_11n_status_a_msdu_max_subframes = None
        self.d_802_11n_status_a_msdu_max_length = None
        self.d_802_11n_status_rifs_rx = None
        self.d_802_11n_status_guard_interval = None
        self.beacon_interval = None
        self.cf_pollable_mandatory = None
        self.cf_poll_request_mandatory = None
        self.cfp_period = None
        self.cfp_maximum_duration = None
        self.default_channel = None
        self.default_tx_power_level = None
        self.dtpc_status = None
        self.fragmentation_threshold = None
        self.rssi_low_check = None
        self.rssi_threshold = None
        self.ti_threshold = None
        self.legacy_tx_beamforming_setting = None
        self.traffic_stream_metrics_status = None
        self.expedited_bw_request_status = None
        self.world_mode = None
        self.dfs_peakdetect = None
        self.edca_profile_type = None
        self.voice_mac_optimization_status = None
        self.call_admission_control_cac_configuration = None
        self.voice_ac = None
        self.voice_ac_voice_ac_admission_control_acm = None
        self.voice_ac_voice_stream_size = None
        self.voice_ac_voice_max_streams = None
        self.voice_ac_voice_max_rf_bandwidth = None
        self.voice_ac_voice_reserved_roaming_bandwidth = None
        self.voice_ac_voice_cac_method = None
        self.voice_ac_voice_tspec_inactivity_timeout = None
        self.cac_sip_voice_configuration = None
        self.cac_sip_voice_configuration_sip_based_cac = None
        self.cac_sip_voice_configuration_sip_codec_type = None
        self.cac_sip_voice_configuration_sip_call_bandwidth = None
        self.cac_sip_voice_configuration_sip_call_bandwith_sample_size = None
        self.video_ac = None
        self.video_ac_video_ac_admission_control_acm = None
        self.video_ac_video_max_rf_bandwidth = None
        self.video_ac_video_reserved_roaming_bandwidth = None
        self.video_ac_video_load_based_cac_mode = None
        self.video_ac_video_cac_method = None
        self.cac_sip_video_configuration = None
        self.cac_sip_video_configuration_sip_based_cac = None
        self.cac_sip_video_configuration_best_effort_ac_admission_control_acm = None
        self.cac_sip_video_configuration_background_ac_admission_control_acm = None
        self.maximum_number_of_clients_per_ap_radio = None
        self.l2roam_802_11a_rf_parameters = None
        self.l2roam_802_11a_rf_parameters_config_mode = None
        self.l2roam_802_11a_rf_parameters_minimum_rssi = None
        self.l2roam_802_11a_rf_parameters_roam_hysteresis = None
        self.l2roam_802_11a_rf_parameters_scan_threshold = None
        self.l2roam_802_11a_rf_parameters_transition_time = None
        self.d_802_11h_configuration = None
        self.power_constraint = None
        self.channel_switch = None
        self.channel_mode = None
        self.smart_dfs = None

    def __str__(self):
        return '802.11a network config'

    def __repr__(self):
        return '802.11a network config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Rf_Profile():
    def __init__(self, name=None):
        self.objname = 'RF profile'
        self.name = None
        self.type = 'config'
        self.rf_profile_name = None
        self.description = None
        self.ap_group_name = None
        self.radio_policy = None
        self.d_11n_client_only = None
        self.transmit_power_threshold_v1 = None
        self.transmit_power_threshold_v2 = None
        self.min_transmit_power = None
        self.max_transmit_power = None
        self.d_802_11b_g_operational_rates = None
        self.d_802_11b_g_operational_rates_802_11b_g_1m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_2m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_5_5m_rate = None
        self.d_802_11b_g_operational_rates_802_11b_g_11m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_6m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_9m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_12m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_18m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_24m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_36m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_48m_rate = None
        self.d_802_11b_g_operational_rates_802_11g_54m_rate = None
        self.d_802_11a_operational_rates = None
        self.d_802_11a_operational_rates_802_11a_6m_rate = None
        self.d_802_11a_operational_rates_802_11a_9m_rate = None
        self.d_802_11a_operational_rates_802_11a_12m_rate = None
        self.d_802_11a_operational_rates_802_11a_18m_rate = None
        self.d_802_11a_operational_rates_802_11a_24m_rate = None
        self.d_802_11a_operational_rates_802_11a_36m_rate = None
        self.d_802_11a_operational_rates_802_11a_48m_rate = None
        self.d_802_11a_operational_rates_802_11a_54m_rate = None
        self.trap_threshold = None
        self.trap_threshold_clients = None
        self.trap_threshold_interference = None
        self.trap_threshold_noise = None
        self.trap_threshold_utilization = None
        self.multicast_data_rate = None
        self.rx_sop_threshold = None
        self.cca_threshold = None
        self.slot_admin_state = None
        self.client_aware_fra = None
        self.client_aware_fra_state = None
        self.client_aware_fra_client_select_utilization_threshold = None
        self.client_aware_fra_client_reset_utilization_threshold = None
        self.band_select = None
        self.band_select_probe_response = None
        self.band_select_cycle_count = None
        self.band_select_cycle_threshold = None
        self.band_select_expire_suppression = None
        self.band_select_expire_dual_band = None
        self.band_select_client_rssi = None
        self.band_select_client_mid_rssi = None
        self.load_balancing = None
        self.load_balancing_denial = None
        self.load_balancing_window = None
        self.coverage_data = None
        self.coverage_data_data = None
        self.coverage_data_voice = None
        self.coverage_data_minimum_client_level = None
        self.coverage_data_exception_level = None
        self.dca_channel_list = None
        self.dca_bandwidth = None
        self.dca_foreign_ap_contribution = None
        self.d_802_11n_mcs_rates = None
        self.d_802_11n_mcs_rates_mcs_00_rate = None
        self.d_802_11n_mcs_rates_mcs_01_rate = None
        self.d_802_11n_mcs_rates_mcs_02_rate = None
        self.d_802_11n_mcs_rates_mcs_03_rate = None
        self.d_802_11n_mcs_rates_mcs_04_rate = None
        self.d_802_11n_mcs_rates_mcs_05_rate = None
        self.d_802_11n_mcs_rates_mcs_06_rate = None
        self.d_802_11n_mcs_rates_mcs_07_rate = None
        self.d_802_11n_mcs_rates_mcs_08_rate = None
        self.d_802_11n_mcs_rates_mcs_09_rate = None
        self.d_802_11n_mcs_rates_mcs_10_rate = None
        self.d_802_11n_mcs_rates_mcs_11_rate = None
        self.d_802_11n_mcs_rates_mcs_12_rate = None
        self.d_802_11n_mcs_rates_mcs_13_rate = None
        self.d_802_11n_mcs_rates_mcs_14_rate = None
        self.d_802_11n_mcs_rates_mcs_15_rate = None
        self.d_802_11n_mcs_rates_mcs_16_rate = None
        self.d_802_11n_mcs_rates_mcs_17_rate = None
        self.d_802_11n_mcs_rates_mcs_18_rate = None
        self.d_802_11n_mcs_rates_mcs_19_rate = None
        self.d_802_11n_mcs_rates_mcs_20_rate = None
        self.d_802_11n_mcs_rates_mcs_21_rate = None
        self.d_802_11n_mcs_rates_mcs_22_rate = None
        self.d_802_11n_mcs_rates_mcs_23_rate = None
        self.d_802_11n_mcs_rates_mcs_24_rate = None
        self.d_802_11n_mcs_rates_mcs_25_rate = None
        self.d_802_11n_mcs_rates_mcs_26_rate = None
        self.d_802_11n_mcs_rates_mcs_27_rate = None
        self.d_802_11n_mcs_rates_mcs_28_rate = None
        self.d_802_11n_mcs_rates_mcs_29_rate = None
        self.d_802_11n_mcs_rates_mcs_30_rate = None
        self.d_802_11n_mcs_rates_mcs_31_rate = None
        self.client_network_preference = None

    def update_name(self):
        self.name = self.rf_profile_name

    def __str__(self):
        return 'RF profile ' + self.name

    def __repr__(self):
        return 'RF profile ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ap_Config():
    def __init__(self, name=None):
        self.objname = 'AP Config'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.cisco_ap_identifier = None
        self.cisco_ap_name = None
        self.country_code = None
        self.regulatory_domain_allowed_by_country = None
        self.ap_country_code = None
        self.wireless_logging_state = None
        self.ap_regulatory_domain = None
        self.switch_port_number = None
        self.mac_address = None
        self.ip_address_configuration = None
        self.ip_address = None
        self.ip_netmask = None
        self.gateway_ip_addr = None
        self.nat_external_ip_address = None
        self.capwap_path_mtu = None
        self.dhcp_release_override = None
        self.telnet_state = None
        self.ssh_state = None
        self.cisco_ap_location = None
        self.cisco_ap_floor_label = None
        self.cisco_ap_group_name = None
        self.primary_cisco_switch_name = None
        self.primary_cisco_switch_ip_address = None
        self.secondary_cisco_switch_name = None
        self.secondary_cisco_switch_ip_address = None
        self.tertiary_cisco_switch_name = None
        self.tertiary_cisco_switch_ip_address = None
        self.administrative_state = None
        self.operation_state = None
        self.mirroring_mode = None
        self.ap_mode = None
        self.public_safety = None
        self.atf_mode = None
        self.ap_submode = None
        self.rogue_detection = None
        self.remote_ap_debug = None
        self.logging_trap_severity_level = None
        self.logging_syslog_facility = None
        self.s_w_version = None
        self.boot_version = None
        self.mini_ios_version = None
        self.stats_reporting_period = None
        self.stats_collection_mode = None
        self.radio_core_mode = None
        self.slub_debug_mode = None
        self.led_state = None
        self.poe_pre_standard_switch = None
        self.poe_power_injector_mac_addr = None
        self.power_type_mode = None
        self.number_of_slots = None
        self.ap_model = None
        self.ap_image = None
        self.ios_version = None
        self.reset_button = None
        self.ap_serial_number = None
        self.ap_certificate_type = None
        self.ap_lag_status = None
        self.ap_user_mode = None
        self.ap_user_name = None
        self.ap_dot1x_user_mode = None
        self.ap_dot1x_user_name = None
        self.cisco_ap_system_logging_host = None
        self.ap_core_dump_config = None
        self.ap_up_time = None
        self.ap_lwapp_up_time = None
        self.join_date_and_time = None
        self.join_taken_time = None
        self.slot_0 = None
        self.slot_0_radio_type = None
        self.slot_0_administrative_state = None
        self.slot_0_operation_state = None
        self.slot_0_mesh_radio_role = None
        self.slot_0_radio_role = None
        self.slot_0_radio_subtype = None
        self.slot_0_radio_role_assignment_method = None
        self.slot_0_radio_role_band = None
        self.slot_0_phy_dsss_parameters_current_cca_mode = None
        self.slot_0_phy_dsss_parameters_ed_threshold = None
        self.slot_0_operation_rate_set_6000_kilo_bits = None
        self.slot_0_operation_rate_set_9000_kilo_bits = None
        self.slot_0_operation_rate_set_5500_kilo_bits = None
        self.slot_0_operation_rate_set_1000_kilo_bits = None
        self.slot_0_operation_rate_set_2000_kilo_bits = None
        self.slot_0_cellid = None
        self.slot_0_station_configuration = None
        self.slot_0_configuration = None
        self.slot_0_number_of_wlans = None
        self.slot_0_medium_occupancy_limit = None
        self.slot_0_cfp_period = None
        self.slot_0_cfp_maxduration = None
        self.slot_0_bssid = None
        self.slot_0_operation_rate_set = None
        self.slot_0_operation_rate_set_11000_kilo_bits = None
        self.slot_0_operation_rate_set_12000_kilo_bits = None
        self.slot_0_operation_rate_set_18000_kilo_bits = None
        self.slot_0_operation_rate_set_24000_kilo_bits = None
        self.slot_0_operation_rate_set_36000_kilo_bits = None
        self.slot_0_operation_rate_set_48000_kilo_bits = None
        self.slot_0_operation_rate_set_54000_kilo_bits = None
        self.slot_0_mcs_set = None
        self.slot_0_mcs_set_mcs_0 = None
        self.slot_0_mcs_set_mcs_1 = None
        self.slot_0_mcs_set_mcs_2 = None
        self.slot_0_mcs_set_mcs_3 = None
        self.slot_0_mcs_set_mcs_4 = None
        self.slot_0_mcs_set_mcs_5 = None
        self.slot_0_mcs_set_mcs_6 = None
        self.slot_0_mcs_set_mcs_7 = None
        self.slot_0_mcs_set_mcs_8 = None
        self.slot_0_mcs_set_mcs_9 = None
        self.slot_0_mcs_set_mcs_10 = None
        self.slot_0_mcs_set_mcs_11 = None
        self.slot_0_mcs_set_mcs_12 = None
        self.slot_0_mcs_set_mcs_13 = None
        self.slot_0_mcs_set_mcs_14 = None
        self.slot_0_mcs_set_mcs_15 = None
        self.slot_0_mcs_set_mcs_16 = None
        self.slot_0_mcs_set_mcs_17 = None
        self.slot_0_mcs_set_mcs_18 = None
        self.slot_0_mcs_set_mcs_19 = None
        self.slot_0_mcs_set_mcs_20 = None
        self.slot_0_mcs_set_mcs_21 = None
        self.slot_0_mcs_set_mcs_22 = None
        self.slot_0_mcs_set_mcs_23 = None
        self.slot_0_mcs_set_mcs_24 = None
        self.slot_0_mcs_set_mcs_25 = None
        self.slot_0_mcs_set_mcs_26 = None
        self.slot_0_mcs_set_mcs_27 = None
        self.slot_0_mcs_set_mcs_28 = None
        self.slot_0_mcs_set_mcs_29 = None
        self.slot_0_mcs_set_mcs_30 = None
        self.slot_0_mcs_set_mcs_31 = None
        self.slot_0_802_11ac_mcs_set = None
        self.slot_0_802_11ac_mcs_set_nss_1_mcs_0_9 = None
        self.slot_0_802_11ac_mcs_set_nss_2_mcs_0_9 = None
        self.slot_0_802_11ac_mcs_set_nss_3_mcs_0_9 = None
        self.slot_0_802_11ac_mcs_set_nss_4_mcs_0_7 = None
        self.slot_0_phy_dsss_parameters = None
        self.slot_0_containment_count_rogue_bssid = None
        self.slot_0_containment_count_rogue_bssid_containment_type = None
        self.slot_0_containment_count_rogue_bssid_channel_count = None
        self.slot_0_beacon_period = None
        self.slot_0_fragmentation_threshold = None
        self.slot_0_multi_domain_capability_implemented = None
        self.slot_0_multi_domain_capability_enabled = None
        self.slot_0_country_string = None
        self.slot_0_multi_domain_capability = None
        self.slot_0_multi_domain_capability_configuration = None
        self.slot_0_multi_domain_capability_first_chan_num = None
        self.slot_0_multi_domain_capability_number_of_channels = None
        self.slot_0_mac_operation_parameters = None
        self.slot_0_mac_operation_parameters_configuration = None
        self.slot_0_mac_operation_parameters_fragmentation_threshold = None
        self.slot_0_mac_operation_parameters_packet_retry_limit = None
        self.slot_0_tx_power = None
        self.slot_0_tx_power_num_of_supported_power_levels = None
        self.slot_0_tx_power_tx_power_level_1 = None
        self.slot_0_tx_power_tx_power_level_2 = None
        self.slot_0_tx_power_tx_power_level_3 = None
        self.slot_0_tx_power_tx_power_level_4 = None
        self.slot_0_tx_power_tx_power_level_5 = None
        self.slot_0_tx_power_tx_power_level_6 = None
        self.slot_0_tx_power_tx_power_level_7 = None
        self.slot_0_tx_power_tx_power_level_8 = None
        self.slot_0_tx_power_tx_power_configuration = None
        self.slot_0_tx_power_current_tx_power_level = None
        self.slot_0_tx_power_tx_power_assigned_by = None
        self.slot_0_phy_ofdm_parameters = None
        self.slot_0_phy_ofdm_parameters_configuration = None
        self.slot_0_phy_ofdm_parameters_current_channel = None
        self.slot_0_phy_ofdm_parameters_channel_assigned_by = None
        self.slot_0_phy_ofdm_parameters_extension_channel = None
        self.slot_0_phy_ofdm_parameters_channel_width = None
        self.slot_0_phy_ofdm_parameters_allowed_channel_list = None
        self.slot_0_phy_ofdm_parameters_allowed_channel_list_ = None
        self.slot_0_phy_ofdm_parameters_ti_threshold = None
        self.slot_0_phy_ofdm_parameters_dca_channel_list = None
        self.slot_0_phy_ofdm_parameters_legacy_tx_beamforming_configuration = None
        self.slot_0_phy_ofdm_parameters_legacy_tx_beamforming = None
        self.slot_0_phy_ofdm_parameters_antenna_type = None
        self.slot_0_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units = None
        self.slot_0_phy_ofdm_parameters_diversity = None
        self.slot_0_phy_ofdm_parameters_802_11n_antennas = None
        self.slot_0_phy_ofdm_parameters_802_11n_antennas_a = None
        self.slot_0_phy_ofdm_parameters_802_11n_antennas_b = None
        self.slot_0_phy_ofdm_parameters_802_11n_antennas_c = None
        self.slot_0_phy_ofdm_parameters_802_11n_antennas_d = None
        self.slot_0_performance_profile_parameters = None
        self.slot_0_performance_profile_parameters_configuration = None
        self.slot_0_performance_profile_parameters_interference_threshold = None
        self.slot_0_performance_profile_parameters_noise_threshold = None
        self.slot_0_performance_profile_parameters_rf_utilization_threshold = None
        self.slot_0_performance_profile_parameters_data_rate_threshold = None
        self.slot_0_performance_profile_parameters_client_threshold = None
        self.slot_0_performance_profile_parameters_coverage_snr_threshold = None
        self.slot_0_performance_profile_parameters_coverage_exception_level = None
        self.slot_0_performance_profile_parameters_client_minimum_exception_level = None
        self.slot_0_rogue_containment_information = None
        self.slot_0_containment_count = None
        self.slot_0_cleanair_management_information = None
        self.slot_0_cleanair_management_information_cleanair_capable = None
        self.slot_0_cleanair_management_information_cleanair_management_administration_st = None
        self.slot_0_cleanair_management_information_cleanair_management_operation_state = None
        self.slot_0_cleanair_management_information_rapid_update_mode = None
        self.slot_0_cleanair_management_information_spectrum_expert_connection = None
        self.slot_0_cleanair_management_information_spectrum_expert_connection_cleanair_nsi_key = None
        self.slot_0_cleanair_management_information_spectrum_expert_connection_spectrum_expert_connections_counter = None
        self.slot_0_cleanair_management_information_cleanair_sensor_state = None
        self.slot_0_radio_extended_configurations = None
        self.slot_0_radio_extended_configurations_beacon_period = None
        self.slot_0_radio_extended_configurations_beacon_range = None
        self.slot_0_radio_extended_configurations_multicast_buffer = None
        self.slot_0_radio_extended_configurations_multicast_data_rate = None
        self.slot_0_radio_extended_configurations_rx_sop_threshold = None
        self.slot_0_radio_extended_configurations_cca_threshold = None
        self.slot_1 = None
        self.slot_1_radio_type = None
        self.slot_1_radio_subband = None
        self.slot_1_administrative_state = None
        self.slot_1_operation_state = None
        self.slot_1_mesh_radio_role = None
        self.slot_1_radio_role = None
        self.slot_1_cellid = None
        self.slot_1_station_configuration = None
        self.slot_1_configuration = None
        self.slot_1_number_of_wlans = None
        self.slot_1_medium_occupancy_limit = None
        self.slot_1_cfp_period = None
        self.slot_1_cfp_maxduration = None
        self.slot_1_bssid = None
        self.slot_1_operation_rate_set = None
        self.slot_1_operation_rate_set_6000_kilo_bits = None
        self.slot_1_operation_rate_set_9000_kilo_bits = None
        self.slot_1_operation_rate_set_12000_kilo_bits = None
        self.slot_1_operation_rate_set_18000_kilo_bits = None
        self.slot_1_operation_rate_set_24000_kilo_bits = None
        self.slot_1_operation_rate_set_36000_kilo_bits = None
        self.slot_1_operation_rate_set_48000_kilo_bits = None
        self.slot_1_operation_rate_set_54000_kilo_bits = None
        self.slot_1_mcs_set = None
        self.slot_1_mcs_set_mcs_0 = None
        self.slot_1_mcs_set_mcs_3 = None
        self.slot_1_mcs_set_mcs_4 = None
        self.slot_1_mcs_set_mcs_5 = None
        self.slot_1_mcs_set_mcs_6 = None
        self.slot_1_mcs_set_mcs_7 = None
        self.slot_1_mcs_set_mcs_8 = None
        self.slot_1_mcs_set_mcs_9 = None
        self.slot_1_mcs_set_mcs_10 = None
        self.slot_1_mcs_set_mcs_11 = None
        self.slot_1_mcs_set_mcs_12 = None
        self.slot_1_mcs_set_mcs_13 = None
        self.slot_1_mcs_set_mcs_14 = None
        self.slot_1_mcs_set_mcs_15 = None
        self.slot_1_mcs_set_mcs_16 = None
        self.slot_1_mcs_set_mcs_17 = None
        self.slot_1_mcs_set_mcs_18 = None
        self.slot_1_mcs_set_mcs_19 = None
        self.slot_1_mcs_set_mcs_20 = None
        self.slot_1_mcs_set_mcs_21 = None
        self.slot_1_mcs_set_mcs_22 = None
        self.slot_1_mcs_set_mcs_23 = None
        self.slot_1_mcs_set_mcs_24 = None
        self.slot_1_mcs_set_mcs_25 = None
        self.slot_1_mcs_set_mcs_26 = None
        self.slot_1_mcs_set_mcs_27 = None
        self.slot_1_mcs_set_mcs_28 = None
        self.slot_1_mcs_set_mcs_29 = None
        self.slot_1_mcs_set_mcs_30 = None
        self.slot_1_mcs_set_mcs_31 = None
        self.slot_1_802_11ac_mcs_set = None
        self.slot_1_802_11ac_mcs_set_nss_1_mcs_0_9 = None
        self.slot_1_802_11ac_mcs_set_nss_2_mcs_0_9 = None
        self.slot_1_802_11ac_mcs_set_nss_3_mcs_0_9 = None
        self.slot_1_802_11ac_mcs_set_nss_4_mcs_0_9 = None
        self.slot_1_802_11ac_mcs_set_nss_4_mcs_0_7 = None
        self.slot_1_beacon_period = None
        self.slot_1_fragmentation_threshold = None
        self.slot_1_multi_domain_capability_implemented = None
        self.slot_1_multi_domain_capability_enabled = None
        self.slot_1_country_string = None
        self.slot_1_multi_domain_capability = None
        self.slot_1_multi_domain_capability_configuration = None
        self.slot_1_multi_domain_capability_first_chan_num = None
        self.slot_1_multi_domain_capability_number_of_channels = None
        self.slot_1_mac_operation_parameters = None
        self.slot_1_mac_operation_parameters_configuration = None
        self.slot_1_mac_operation_parameters_fragmentation_threshold = None
        self.slot_1_mac_operation_parameters_packet_retry_limit = None
        self.slot_1_tx_power = None
        self.slot_1_tx_power_num_of_supported_power_levels = None
        self.slot_1_tx_power_tx_power_level_1 = None
        self.slot_1_tx_power_tx_power_level_2 = None
        self.slot_1_tx_power_tx_power_level_3 = None
        self.slot_1_tx_power_tx_power_level_4 = None
        self.slot_1_tx_power_tx_power_level_5 = None
        self.slot_1_tx_power_tx_power_level_6 = None
        self.slot_1_tx_power_tx_power_level_7 = None
        self.slot_1_tx_power_tx_power_level_8 = None
        self.slot_1_tx_power_tx_power_configuration = None
        self.slot_1_tx_power_current_tx_power_level = None
        self.slot_1_tx_power_tx_power_assigned_by = None
        self.slot_1_phy_ofdm_parameters = None
        self.slot_1_phy_ofdm_parameters_configuration = None
        self.slot_1_phy_ofdm_parameters_current_channel = None
        self.slot_1_phy_ofdm_parameters_channel_assigned_by = None
        self.slot_1_phy_ofdm_parameters_extension_channel = None
        self.slot_1_phy_ofdm_parameters_channel_width = None
        self.slot_1_phy_ofdm_parameters_allowed_channel_list = None
        self.slot_1_phy_ofdm_parameters_allowed_channel_list_ = None
        self.slot_1_phy_ofdm_parameters_ti_threshold = None
        self.slot_1_phy_ofdm_parameters_dca_channel_list = None
        self.slot_1_phy_ofdm_parameters_legacy_tx_beamforming_configuration = None
        self.slot_1_phy_ofdm_parameters_legacy_tx_beamforming = None
        self.slot_1_phy_ofdm_parameters_antenna_type = None
        self.slot_1_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units = None
        self.slot_1_phy_ofdm_parameters_diversity = None
        self.slot_1_phy_ofdm_parameters_802_11n_antennas = None
        self.slot_1_phy_ofdm_parameters_802_11n_antennas_a = None
        self.slot_1_phy_ofdm_parameters_802_11n_antennas_b = None
        self.slot_1_phy_ofdm_parameters_802_11n_antennas_c = None
        self.slot_1_phy_ofdm_parameters_802_11n_antennas_d = None
        self.slot_1_performance_profile_parameters = None
        self.slot_1_performance_profile_parameters_interference_threshold = None
        self.slot_1_performance_profile_parameters_noise_threshold = None
        self.slot_1_performance_profile_parameters_rf_utilization_threshold = None
        self.slot_1_performance_profile_parameters_data_rate_threshold = None
        self.slot_1_performance_profile_parameters_client_threshold = None
        self.slot_1_performance_profile_parameters_coverage_snr_threshold = None
        self.slot_1_performance_profile_parameters_coverage_exception_level = None
        self.slot_1_performance_profile_parameters_client_minimum_exception_level = None
        self.slot_1_rogue_containment_information = None
        self.slot_1_containment_count = None
        self.slot_1_cleanair_management_information = None
        self.slot_1_cleanair_management_information_cleanair_capable = None
        self.slot_1_cleanair_management_information_cleanair_management_administration_st = None
        self.slot_1_cleanair_management_information_cleanair_management_operation_state = None
        self.slot_1_cleanair_management_information_rapid_update_mode = None
        self.slot_1_cleanair_management_information_spectrum_expert_connection = None
        self.slot_1_cleanair_management_information_spectrum_expert_connection_cleanair_nsi_key = None
        self.slot_1_cleanair_management_information_spectrum_expert_connection_spectrum_expert_connections_counter = None
        self.slot_1_cleanair_management_information_cleanair_sensor_state = None
        self.slot_1_radio_extended_configurations = None
        self.slot_1_radio_extended_configurations_beacon_period = None
        self.slot_1_radio_extended_configurations_beacon_range = None
        self.slot_1_radio_extended_configurations_multicast_buffer = None
        self.slot_1_radio_extended_configurations_multicast_data_rate = None
        self.slot_1_radio_extended_configurations_rx_sop_threshold = None
        self.slot_1_radio_extended_configurations_cca_threshold = None

    def update_name(self):
        self.name = self.cisco_ap_name

    def __str__(self):
        return 'AP config for ' + self.name

    def __repr__(self):
        return 'AP config for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Radius_Authentication_Server():
    def __init__(self, name=None):
        self.objname = 'RADIUS Authentication server'
        self.name = None
        self.type = None
        self.id = None
        self.ip_address = None
        self.port = None
        self.state = None
        self.timeout = None
        self.mgmt_timeout = None
        self.rfc3576 = None
        self.ipsec = None

    def update_name(self):
        self.name = self.id

    def get_one_item(self):
        return Radius_Authentication_Server()

    def __str__(self):
        return 'RADIUS AUTH server ' + self.name

    def __repr__(self):
        return 'RADIUS AUTH server ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Radius_Accounting_Server():
    def __init__(self, name=None):
        self.objname = 'RADIUS Accounting server'
        self.name = None
        self.type = None
        self.id = None
        self.ip_address = None
        self.port = None
        self.state = None
        self.timeout = None
        self.mgmt_timeout = None
        self.rfc3576 = None
        self.ipsec = None

    def update_name(self):
        self.name = self.id

    def get_one_item(self):
        return Radius_Accounting_Server()

    def __str__(self):
        return 'RADIUS ACCT server ' + self.name

    def __repr__(self):
        return 'RADIUS ACCT server ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Mobility_Group_Member():
    def __init__(self, name=None):
        self.objname = 'Mobility group member'
        self.name = None
        self.mac_address = None
        self.ip_address = None
        self.mobility_group_name = None
        self.multicast_ip = None
        self.state = None

    def update_name(self):
        self.name = self.ip_address

    def get_one_item(self):
        return Mobility_Group_Member()

    def __str__(self):
        return 'Mobility group member ' + self.name

    def __repr__(self):
        return 'Mobility group member ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Port():
    def __init__(self, name=None):
        self.objname = 'Port Information'
        self.name = None
        self.number = None
        self.type = None
        self.stp_state = None
        self.admin_mode = None
        self.phy_mode = None
        self.phy_status = None
        self.link_status = None
        self.link_trap = None
        self.poe = None
        self.sfp_type = None

    def update_name(self):
        self.name = self.number

    def get_one_item(self):
        return Port()

    def __str__(self):
        return 'Port info for ' + self.name

    def __repr__(self):
        return 'Port info for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Rogue_Ap():  # Can be different between software versions, this is based on 8.3.150 output
    def __init__(self, name=None):
        self.objname = 'Rogue AP Information'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.mac_address = None
        self.classification = None
        self.state = None
        self.detecting_aps = None
        self.rogue_clients_number = None
        self.highest_rssi_ap = None
        self.highest_rssi_value = None
        self.channel = None
        self.second_rssi_ap = None
        self.second_rssi_value = None
        self.last_heard = None
        self.band = None

    def update_name(self):
        self.name = self.mac_address

    def __str__(self):
        return 'Rogue AP info for ' + self.name

    def __repr__(self):
        return 'Rogue AP info for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class System_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'System Info'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.name_chassis = None
        self.burned_in_mac_address = None
        self.maximum_number_of_aps_supported = None
        self.system_information = None
        self.manufacturers_name = None
        self.product_name = None
        self.build_info = None
        self.product_version = None
        self.rtos_version = None
        self.bootloader_version = None
        self.emergency_image_version = None
        self.field_recovery_image_version = None
        self.firmware_version = None
        self.oui_file_update_time = None
        self.build_type = None
        self.oui_file_last_update_time = None
        self.build_type = None
        self.system_name = None
        self.system_location = None
        self.system_contact = None
        self.system_objectid = None
        self.redundancy_mode = None
        self.ip_address = None
        self.ipv6_address = None
        self.last_reset = None
        self.system_up_time = None
        self.system_timezone_location = None
        self.system_stats_realtime_interval = None
        self.system_stats_normal_interval = None
        self.configured_country = None
        self.operating_environment = None
        self.internal_temp_alarm_limits = None
        self.internal_temperature = None
        self.mgig_temp_alarm_limits = None
        self.mgig_temperature = None
        self.external_temp_alarm_limits = None
        self.external_temperature = None
        self.fan_status = None
        self.fan_speed_mode = None
        self.power_supply_1 = None
        self.power_supply_2 = None
        self.state_of_802_11b_network = None
        self.state_of_802_11a_network = None
        self.number_of_wlans = None
        self.number_of_active_clients = None
        self.oui_classification_failure_count = None
        self.memory_current_usage = None
        self.memory_average_usage = None
        self.cpu_current_usage = None
        self.cpu_average_usage = None
        self.flash_type = None
        self.flash_size = None
        self.maximum_number_of_aps_supported = None
        self.system_nas_id = None
        self.wlc_mic_certificate_types = None
        self.licensing_type = None
        self.licensing_type_usb = None
        self.backup_controller_configuration = None
        self.ap_primary_backup_controller = None
        self.ap_secondary_backup_controller = None
        self.raid_drive_0 = None
        self.raid_drive_1 = None

    def __str__(self):
        return 'WLC System Information'

    def __repr__(self):
        return 'WLC System Information'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Redundancy_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Redundancy Configuration'
        self.name = None
        self.type = 'mixed'  # defines if class contain operational or config data
        self.redundancy_mode = None
        self.local_state = None
        self.peer_state = None
        self.unit = None
        self.unit_id = None
        self.redundancy_state = None
        self.mobility_mac = None
        self.redundancy_management_ip_address = None
        self.peer_redundancy_management_ip_address = None
        self.redundancy_port_ip_address = None
        self.peer_redundancy_port_ip_address = None
        self.peer_service_port_ip_address = None

    def __str__(self):
        return 'WLC redundancy config'

    def __repr__(self):
        return 'WLC redundancy config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Mobility_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Mobility Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.mobility_protocol_port = None
        self.default_mobility_domain = None
        self.multicast_mode = None
        self.mobility_domain_id_for_802_11r = None
        self.mobility_keepalive_interval = None
        self.mobility_keepalive_count = None
        self.mobility_group_members_configured = None
        self.mobility_control_message_dscp_value = None

    def __str__(self):
        return 'WLC mobility config'

    def __repr__(self):
        return 'WLC mobility config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Network_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Network Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.network_information = None
        self.rf_network_name = None
        self.dns_server_ip = None
        self.web_mode = None
        self.secure_web_mode = None
        self.secure_web_mode_cipher_option_high = None
        self.secure_web_mode_ssl_protocol = None
        self.web_csrf_check = None
        self.ocsp = None
        self.ocsp_responder_url = None
        self.secure_shell_ssh = None
        self.secure_shell_ssh_cipher_option_high = None
        self.telnet = None
        self.ethernet_multicast_forwarding = None
        self.ethernet_broadcast_forwarding = None
        self.ipv4_ap_multicast_broadcast_mode = None
        self.ipv6_ap_multicast_broadcast_mode = None
        self.igmp_snooping = None
        self.igmp_timeout = None
        self.igmp_query_interval = None
        self.mld_snooping = None
        self.mld_timeout = None
        self.mld_query_interval = None
        self.user_idle_timeout = None
        self.arp_idle_timeout = None
        self.cisco_ap_default_master = None
        self.ap_join_priority = None
        self.mgmt_via_wireless_interface = None
        self.mgmt_via_dynamic_interface = None
        self.bridge_mac_filter_config = None
        self.bridge_security_mode = None
        self.mesh_full_sector_dfs = None
        self.mesh_backhaul_rrm = None
        self.ap_fallback = None
        self.web_auth_cmcc_support = None
        self.web_auth_redirect_ports = None
        self.web_auth_proxy_redirect_ = None
        self.web_auth_captive_bypass__ = None
        self.web_auth_secure_web_ = None
        self.web_auth_secure_web_cipher_option_ = None
        self.web_auth_secure_web_sslv3_ = None
        self.web_auth_secure_redirection_ = None
        self.fast_ssid_change = None
        self.ap_discovery_nat_ip_only = None
        self.ip_mac_addr_binding_check = None
        self.link_local_bridging_status = None
        self.ccx_lite_status = None
        self.oeap_600_dual_rlan_ports = None
        self.oeap_local_network = None
        self.oeap_600_split_tunneling_printers = None
        self.webportal_online_client = None
        self.webportal_ntf_logout_client = None
        self.mdns_snooping = None
        self.mdns_query_interval = None
        self.web_color_theme = None
        self.capwap_prefer_mode = None
        self.network_profile = None
        self.client_ip_conflict_detection_dhcp = None
        self.mesh_bh_rrm = None
        self.mesh_aggressive_dca = None
        self.mesh_auto_rf = None
        self.http_profiling_port = None
        self.http_proxy_ip_address = None
        self.http_proxy_port = None
        self.wgb_client_forced_l2_roam = None

    def __str__(self):
        return 'WLC network config'

    def __repr__(self):
        return 'WLC network config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Dhcp_Server():
    def __init__(self, name=None):
        self.objname = 'DHCP Server Configuration'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.ip_address = None
        self.dhcp_rx_discover_count = None
        self.dhcp_tx_discover_count = None
        self.dhcp_ack_count = None
        self.dhcp_request_count = None
        self.dhcp_inform_count = None
        self.dhcp_decline_count = None
        self.dhcp_release_count = None
        self.dhcp_reply_count = None
        self.dhcp_offer_count = None
        self.dhcp_nak_count = None
        self.tx_fails = None
        self.last_rx_time = None
        self.last_tx_time = None

    def __str__(self):
        return 'DHCP server ' + self.name

    def __repr__(self):
        return 'DHCP server ' + self.name

    def update_name(self):
        self.name = self.ip_address

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Cleanair_24G_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'CleanAir 2.4 GHz Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.clean_air_solution = None
        self.air_quality_settings = None
        self.air_quality_settings_air_quality_reporting = None
        self.air_quality_settings_air_quality_reporting_period_min = None
        self.air_quality_settings_air_quality_alarms = None
        self.air_quality_settings_air_quality_alarms_air_quality_alarm_threshold = None
        self.air_quality_settings_air_quality_alarms_unclassified_interference = None
        self.air_quality_settings_air_quality_alarms_unclassified_severity_threshold = None
        self.air_quality_settings_interference_device_reporting = None
        self.air_quality_settings_interference_device_types = None
        self.air_quality_settings_interference_device_types_bluetooth_link = None
        self.air_quality_settings_interference_device_types_microwave_oven = None
        self.air_quality_settings_interference_device_types_802_11_fh = None
        self.air_quality_settings_interference_device_types_bluetooth_discovery = None
        self.air_quality_settings_interference_device_types_tdd_transmitter = None
        self.air_quality_settings_interference_device_types_jammer = None
        self.air_quality_settings_interference_device_types_continuous_transmitter = None
        self.air_quality_settings_interference_device_types_dect_like_phone = None
        self.air_quality_settings_interference_device_types_video_camera = None
        self.air_quality_settings_interference_device_types_802_15_4 = None
        self.air_quality_settings_interference_device_types_wifi_inverted = None
        self.air_quality_settings_interference_device_types_wifi_invalid_channel = None
        self.air_quality_settings_interference_device_types_superag = None
        self.air_quality_settings_interference_device_types_canopy = None
        self.air_quality_settings_interference_device_types_microsoft_device = None
        self.air_quality_settings_interference_device_types_wimax_mobile = None
        self.air_quality_settings_interference_device_types_wimax_fixed = None
        self.air_quality_settings_interference_device_types_ble_beacon = None
        self.air_quality_settings_interference_device_alarms = None
        self.air_quality_settings_interference_device_types_triggering_alarms = None
        self.air_quality_settings_interference_device_types_triggering_alarms_bluetooth_link = None
        self.air_quality_settings_interference_device_types_triggering_alarms_microwave_oven = None
        self.air_quality_settings_interference_device_types_triggering_alarms_802_11_fh = None
        self.air_quality_settings_interference_device_types_triggering_alarms_bluetooth_discovery = None
        self.air_quality_settings_interference_device_types_triggering_alarms_tdd_transmitter = None
        self.air_quality_settings_interference_device_types_triggering_alarms_jammer = None
        self.air_quality_settings_interference_device_types_triggering_alarms_continuous_transmitter = None
        self.air_quality_settings_interference_device_types_triggering_alarms_dect_like_phone = None
        self.air_quality_settings_interference_device_types_triggering_alarms_video_camera = None
        self.air_quality_settings_interference_device_types_triggering_alarms_802_15_4 = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wifi_inverted = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wifi_invalid_channel = None
        self.air_quality_settings_interference_device_types_triggering_alarms_superag = None
        self.air_quality_settings_interference_device_types_triggering_alarms_canopy = None
        self.air_quality_settings_interference_device_types_triggering_alarms_microsoft_device = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wimax_mobile = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wimax_fixed = None
        self.air_quality_settings_interference_device_types_triggering_alarms_ble_beacon = None
        self.additional_clean_air_settings = None
        self.additional_clean_air_settings_cleanair_ed_rrm_state = None
        self.additional_clean_air_settings_cleanair_ed_rrm_sensitivity = None
        self.additional_clean_air_settings_cleanair_ed_rrm_custom_threshold = None
        self.additional_clean_air_settings_cleanair_rogue_contribution = None
        self.additional_clean_air_settings_cleanair_rogue_duty_cycle_threshold = None
        self.additional_clean_air_settings_cleanair_persistent_devices_state = None
        self.additional_clean_air_settings_cleanair_persistent_device_propagation = None

    def __str__(self):
        return 'CleanAir 2.4 GHz config'

    def __repr__(self):
        return 'CleanAir 2.4 GHz config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Cleanair_5G_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'CleanAir 5 GHz Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.clean_air_solution = None
        self.air_quality_settings = None
        self.air_quality_settings_air_quality_reporting = None
        self.air_quality_settings_air_quality_reporting_period_min = None
        self.air_quality_settings_air_quality_alarms = None
        self.air_quality_settings_air_quality_alarms_air_quality_alarm_threshold = None
        self.air_quality_settings_air_quality_alarms_unclassified_interference = None
        self.air_quality_settings_air_quality_alarms_unclassified_severity_threshold = None
        self.air_quality_settings_interference_device_reporting = None
        self.air_quality_settings_interference_device_types = None
        self.air_quality_settings_interference_device_types_tdd_transmitter = None
        self.air_quality_settings_interference_device_types_jammer = None
        self.air_quality_settings_interference_device_types_continuous_transmitter = None
        self.air_quality_settings_interference_device_types_dect_like_phone = None
        self.air_quality_settings_interference_device_types_video_camera = None
        self.air_quality_settings_interference_device_types_wifi_inverted = None
        self.air_quality_settings_interference_device_types_wifi_invalid_channel = None
        self.air_quality_settings_interference_device_types_superag = None
        self.air_quality_settings_interference_device_types_canopy = None
        self.air_quality_settings_interference_device_types_wimax_mobile = None
        self.air_quality_settings_interference_device_types_wimax_fixed = None
        self.air_quality_settings_interference_device_alarms = None
        self.air_quality_settings_interference_device_types_triggering_alarms = None
        self.air_quality_settings_interference_device_types_triggering_alarms_tdd_transmitter = None
        self.air_quality_settings_interference_device_types_triggering_alarms_jammer = None
        self.air_quality_settings_interference_device_types_triggering_alarms_continuous_transmitter = None
        self.air_quality_settings_interference_device_types_triggering_alarms_dect_like_phone = None
        self.air_quality_settings_interference_device_types_triggering_alarms_video_camera = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wifi_inverted = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wifi_invalid_channel = None
        self.air_quality_settings_interference_device_types_triggering_alarms_superag = None
        self.air_quality_settings_interference_device_types_triggering_alarms_canopy = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wimax_mobile = None
        self.air_quality_settings_interference_device_types_triggering_alarms_wimax_fixed = None
        self.additional_clean_air_settings = None
        self.additional_clean_air_settings_cleanair_ed_rrm_state = None
        self.additional_clean_air_settings_cleanair_ed_rrm_sensitivity = None
        self.additional_clean_air_settings_cleanair_ed_rrm_custom_threshold = None
        self.additional_clean_air_settings_cleanair_rogue_contribution = None
        self.additional_clean_air_settings_cleanair_rogue_duty_cycle_threshold = None
        self.additional_clean_air_settings_cleanair_persistent_devices_state = None
        self.additional_clean_air_settings_cleanair_persistent_device_propagation = None

    def __str__(self):
        return 'CleanAir 5 GHz config'

    def __repr__(self):
        return 'CleanAir 5 GHz config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Switch_Config():  # No lists in this part of config - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Switch Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.d_802_3x_flow_control_mode = None
        self.fips_prerequisite_features = None
        self.wlancc_prerequisite_features = None
        self.ucapl_prerequisite_features = None
        self.last_login_information_display = None
        self.dtls_wlc_mic = None
        self.secret_obfuscation = None
        self.strong_password_check_features = None
        self.strong_password_check_features_case_check = None
        self.strong_password_check_features_consecutive_check = None
        self.strong_password_check_features_default_check = None
        self.strong_password_check_features_username_check = None
        self.strong_password_check_features_position_check = None
        self.strong_password_check_features_case_digit_check = None
        self.strong_password_check_features_min__password_length = None
        self.strong_password_check_features_min__upper_case_chars = None
        self.strong_password_check_features_min__lower_case_chars = None
        self.strong_password_check_features_min__digits_chars = None
        self.strong_password_check_features_min__special_chars = None
        self.mgmt_user = None
        self.mgmt_user_password_lifetime_days = None
        self.mgmt_user_password_lockout = None
        self.mgmt_user_lockout_attempts = None
        self.mgmt_user_lockout_timeout_mins = None
        self.snmpv3_user = None
        self.snmpv3_user_password_lifetime_days = None
        self.snmpv3_user_password_lockout = None
        self.snmpv3_user_lockout_attempts = None
        self.snmpv3_user_lockout_timeout_mins = None

    def __str__(self):
        return 'WLC switch config'

    def __repr__(self):
        return 'WLC switch config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Radius_Config():
    def __init__(self, name=None):
        self.objname = 'RADIUS Configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.vendor_id_backward_compatibility = None
        self.call_station_id_case = None
        self.accounting_call_station_id_type = None
        self.auth_call_station_id_type = None
        self.extended_source_ports_support = None
        self.aggressive_failover = None
        self.keywrap = None
        self.fallback_test = None
        self.fallback_test_test_mode = None
        self.fallback_test_probe_user_name = None
        self.fallback_test_interval_in_seconds = None
        self.mac_delimiter_for_authentication_messages = None
        self.mac_delimiter_for_accounting_messages = None
        self.radius_authentication_framed_mtu = None

    def __str__(self):
        return 'RADIUS config'

    def __repr__(self):
        return 'RADIUS config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ipv6_Config():
    def __init__(self, name=None):
        self.objname = 'IPv6 global configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.global_config = None
        self.reachable_lifetime_value = None
        self.stale_lifetime_value = None
        self.down_lifetime_value = None
        self.ra_throttling = None
        self.ra_throttling_allow_at_least = None
        self.ra_throttling_allow_at_most = None
        self.ra_throttling_max_through = None
        self.ra_throttling_throttle_period = None
        self.ra_throttling_interval_option = None
        self.ns_mulitcast_cachemiss_forwarding = None
        self.na_mulitcast_forwarding = None
        self.ipv6_capwap_udp_lite = None
        self.operating_system_ipv6_state = None

    def __str__(self):
        return 'IPv6 config'

    def __repr__(self):
        return 'IPv6 config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Advanced_Config():
    def __init__(self, name=None):
        self.objname = 'Advanced configuration'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.probe_request_filtering = None
        self.probes_fwd_to_controller_per_client_per_radio = None
        self.probe_request_rate_limiting_interval = None
        self.aggregate_probe_request_interval = None
        self.increased_backoff_parameters_for_probe = None
        self.eap_identity_request_timeout_seconds = None
        self.eap_identity_request_max_retries = None
        self.eap_key_index_for_dynamic_wep = None
        self.eap_max_login_ignore_identity_response = None
        self.eap_request_timeout_seconds = None
        self.eap_request_max_retries = None
        self.eapol_key_timeout_milliseconds = None
        self.eapol_key_max_retries = None
        self.eap_broadcast_key_interval = None
        self.fastpath_packet_capture = None
        self.fastpath_fast_cache_control = None
        self.fastpath_fast_testmode = None
        self.dot11_padding = None
        self.padding_size = None
        self.advanced_hotspot_commands = None
        self.anqp_4_way_state = None
        self.garp_broadcast_state = None
        self.gas_request_rate_limit = None
        self.anqp_comeback_delay = None

    def __str__(self):
        return 'Really advanced WLC config'

    def __repr__(self):
        return 'Really advanced WLC config'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ap_Group_Wlan():  # Special class to save info about WLAN configuration in AP group config
    def __init__(self, name=None):
        self.objname = 'Wlan_Ap_Group'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.wlan_id = None
        self.interface = None
        self.nac = None
        self.radio_policy = None
        self.open_dns_profile = None

    def update_name(self):
        self.name = self.wlan_id

    def __str__(self):
        return 'WLAN config in AP Group ' + self.name

    def __repr__(self):
        return 'WLAN config in AP Group ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ap_Group_Wlans(NamedList):  # This class is important to add name attribute of AP that heard this list of APs
    def __init__(self, list_name, item_name):
        self.objname = 'Ap_Group_Wlans'
        self.item_name = 'Ap_Group_Wlan'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.ap_group = None  # Name of AP group that has these WLANs configured

    def get_one_item(self):
        return Ap_Group_Wlan()

    def update_name(self):
        if self.ap_group is not None:
            self.name = self.ap_group

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ap_Group():  # Item for NamedList "AP Groups" - subclass of wlc_config
    def __init__(self):
        self.objname = 'AP group config'
        self.name = None
        self.site_name = None
        self.site_description = None
        self.venue_group_code = None
        self.venue_type_code = None
        self.nas_identifier = None
        self.client_traffic_qinq_enable = None
        self.dhcpv4_qinq_enable = None
        self.ap_operating_class = None
        self.capwap_prefer_mode = None
        self.antenna_monitoring_status = None
        self.rf_profile_24 = None
        self.rf_profile_5 = None
        self.fabric_flex_acl_template_name = None
        self.ap_names = None
        self.wlans = Ap_Group_Wlans('Ap_Group_Wlans', 'Ap_Group_Wlan')

    def update_name(self):
        if self.site_name is not None:
            self.name = self.site_name

    def __str__(self):
        return 'AP group config for group ' + self.name

    def __repr__(self):
        return 'AP group config for group ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Nearby_Ap():  # Can be different between software versions, this is based on 8.3.150 output
    def __init__(self, name=None):
        self.objname = 'Nearby AP Information'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.mac_address = None
        self.rssi = None
        self.channel = None
        self.bandwidth = None
        # self.ap_name = None #Name of AP that heard this nearby AP
        # self.ap_slot = None #Slot ID of AP that heard this nearby AP

    def update_name(self):
        self.name = self.mac_address

    def __str__(self):
        return 'Nearby AP info for ' + self.name

    def __repr__(self):
        return 'Nearby AP info for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Nearby_Aps(NamedList):  # This class is important to add name attribute of AP that heard this list of APs
    def __init__(self, list_name, item_name):
        self.objname = 'Nearby_Aps'
        self.item_name = 'Nearby_Ap'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.ap_name = None  # Name of AP that heard these nearby APs
        self.ap_slot = None  # Slot ID of AP that heard these nearby APs

    def get_one_item(self):
        return Nearby_Ap()

    def update_name(self):
        if self.ap_name is not None:
            self.name = self.ap_name + '_slot' + self.ap_slot

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ap_Rf_Config():  # Item for NamedList "AP RF Configs" - subclass of wlc_config
    def __init__(self):
        self.objname = 'AP RF config'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.number_of_slots = None
        self.ap_name = None
        self.mac_address = None
        self.slot_id = None
        self.radio_type = None
        self.sub_band_type = None
        self.nearby_aps = Nearby_Aps('Nearby_Aps', 'Nearby_Ap')
        self.noise_profile = None
        self.noise_profile_channel_1 = None
        self.noise_profile_channel_2 = None
        self.noise_profile_channel_3 = None
        self.noise_profile_channel_4 = None
        self.noise_profile_channel_5 = None
        self.noise_profile_channel_6 = None
        self.noise_profile_channel_7 = None
        self.noise_profile_channel_8 = None
        self.noise_profile_channel_9 = None
        self.noise_profile_channel_10 = None
        self.noise_profile_channel_11 = None
        self.noise_profile_channel_12 = None
        self.noise_profile_channel_13 = None
        self.noise_profile_channel_14 = None
        self.noise_profile_channel_34 = None
        self.noise_profile_channel_36 = None
        self.noise_profile_channel_38 = None
        self.noise_profile_channel_40 = None
        self.noise_profile_channel_42 = None
        self.noise_profile_channel_44 = None
        self.noise_profile_channel_46 = None
        self.noise_profile_channel_48 = None
        self.noise_profile_channel_52 = None
        self.noise_profile_channel_56 = None
        self.noise_profile_channel_60 = None
        self.noise_profile_channel_64 = None
        self.noise_profile_channel_100 = None
        self.noise_profile_channel_104 = None
        self.noise_profile_channel_108 = None
        self.noise_profile_channel_112 = None
        self.noise_profile_channel_116 = None
        self.noise_profile_channel_120 = None
        self.noise_profile_channel_124 = None
        self.noise_profile_channel_128 = None
        self.noise_profile_channel_132 = None
        self.noise_profile_channel_136 = None
        self.noise_profile_channel_140 = None
        self.noise_profile_channel_144 = None
        self.noise_profile_channel_149 = None
        self.noise_profile_channel_153 = None
        self.noise_profile_channel_157 = None
        self.noise_profile_channel_161 = None
        self.noise_profile_channel_165 = None
        self.noise_profile_channel_169 = None
        self.noise_profile_channel_173 = None
        self.interference_profile = None
        self.interference_profile_channel_1 = None
        self.interference_profile_channel_2 = None
        self.interference_profile_channel_3 = None
        self.interference_profile_channel_4 = None
        self.interference_profile_channel_5 = None
        self.interference_profile_channel_6 = None
        self.interference_profile_channel_7 = None
        self.interference_profile_channel_8 = None
        self.interference_profile_channel_9 = None
        self.interference_profile_channel_10 = None
        self.interference_profile_channel_11 = None
        self.interference_profile_channel_12 = None
        self.interference_profile_channel_13 = None
        self.interference_profile_channel_14 = None
        self.interference_profile_channel_34 = None
        self.interference_profile_channel_36 = None
        self.interference_profile_channel_38 = None
        self.interference_profile_channel_40 = None
        self.interference_profile_channel_42 = None
        self.interference_profile_channel_44 = None
        self.interference_profile_channel_46 = None
        self.interference_profile_channel_48 = None
        self.interference_profile_channel_52 = None
        self.interference_profile_channel_56 = None
        self.interference_profile_channel_60 = None
        self.interference_profile_channel_64 = None
        self.interference_profile_channel_100 = None
        self.interference_profile_channel_104 = None
        self.interference_profile_channel_108 = None
        self.interference_profile_channel_112 = None
        self.interference_profile_channel_116 = None
        self.interference_profile_channel_120 = None
        self.interference_profile_channel_124 = None
        self.interference_profile_channel_128 = None
        self.interference_profile_channel_132 = None
        self.interference_profile_channel_136 = None
        self.interference_profile_channel_140 = None
        self.interference_profile_channel_144 = None
        self.interference_profile_channel_149 = None
        self.interference_profile_channel_153 = None
        self.interference_profile_channel_157 = None
        self.interference_profile_channel_161 = None
        self.interference_profile_channel_165 = None
        self.interference_profile_channel_169 = None
        self.interference_profile_channel_173 = None
        self.rogue_histogram = None
        self.rogue_histogram_channel_1 = None
        self.rogue_histogram_channel_2 = None
        self.rogue_histogram_channel_3 = None
        self.rogue_histogram_channel_4 = None
        self.rogue_histogram_channel_5 = None
        self.rogue_histogram_channel_6 = None
        self.rogue_histogram_channel_7 = None
        self.rogue_histogram_channel_8 = None
        self.rogue_histogram_channel_9 = None
        self.rogue_histogram_channel_10 = None
        self.rogue_histogram_channel_11 = None
        self.rogue_histogram_channel_12 = None
        self.rogue_histogram_channel_13 = None
        self.rogue_histogram_channel_14 = None
        self.rogue_histogram_channel_34 = None
        self.rogue_histogram_channel_36 = None
        self.rogue_histogram_channel_38 = None
        self.rogue_histogram_channel_40 = None
        self.rogue_histogram_channel_42 = None
        self.rogue_histogram_channel_44 = None
        self.rogue_histogram_channel_46 = None
        self.rogue_histogram_channel_48 = None
        self.rogue_histogram_channel_52 = None
        self.rogue_histogram_channel_56 = None
        self.rogue_histogram_channel_60 = None
        self.rogue_histogram_channel_64 = None
        self.rogue_histogram_channel_100 = None
        self.rogue_histogram_channel_104 = None
        self.rogue_histogram_channel_108 = None
        self.rogue_histogram_channel_112 = None
        self.rogue_histogram_channel_116 = None
        self.rogue_histogram_channel_120 = None
        self.rogue_histogram_channel_124 = None
        self.rogue_histogram_channel_128 = None
        self.rogue_histogram_channel_132 = None
        self.rogue_histogram_channel_136 = None
        self.rogue_histogram_channel_140 = None
        self.rogue_histogram_channel_144 = None
        self.rogue_histogram_channel_149 = None
        self.rogue_histogram_channel_153 = None
        self.rogue_histogram_channel_157 = None
        self.rogue_histogram_channel_161 = None
        self.rogue_histogram_channel_165 = None
        self.rogue_histogram_channel_169 = None
        self.rogue_histogram_channel_173 = None
        self.load_profile = None
        self.load_profile_receive_utilization = None
        self.load_profile_transmit_utilization = None
        self.load_profile_channel_utilization = None
        self.load_profile_attached_clients = None
        self.coverage_profile = None
        self.failed_clients = None
        self.client_signal_strengths = None
        self.client_signal_strengths_rssi_100_dbm = None
        self.client_signal_strengths_rssi_92_dbm = None
        self.client_signal_strengths_rssi_84_dbm = None
        self.client_signal_strengths_rssi_76_dbm = None
        self.client_signal_strengths_rssi_68_dbm = None
        self.client_signal_strengths_rssi_60_dbm = None
        self.client_signal_strengths_rssi_52_dbm = None
        self.client_signal_to_noise_ratios = None
        self.client_signal_to_noise_ratios_snr_0_db = None
        self.client_signal_to_noise_ratios_snr_5_db = None
        self.client_signal_to_noise_ratios_snr_10_db = None
        self.client_signal_to_noise_ratios_snr_15_db = None
        self.client_signal_to_noise_ratios_snr_20_db = None
        self.client_signal_to_noise_ratios_snr_25_db = None
        self.client_signal_to_noise_ratios_snr_30_db = None
        self.client_signal_to_noise_ratios_snr_35_db = None
        self.client_signal_to_noise_ratios_snr_40_db = None
        self.client_signal_to_noise_ratios_snr_45_db = None
        self.radar_information = None
        self.channel_assignment_information = None
        self.channel_assignment_information_current_channel_average_energy = None
        self.channel_assignment_information_previous_channel_average_energy = None
        self.channel_assignment_information_channel_change_count = None
        self.channel_assignment_information_last_channel_change_time = None
        self.channel_assignment_information_recommended_best_channel = None
        self.rf_parameter_recommendations = None
        self.rf_parameter_recommendations_power_level = None
        self.rf_parameter_recommendations_rts_cts_threshold = None
        self.rf_parameter_recommendations_fragmentation_threshold = None
        self.rf_parameter_recommendations_antenna_pattern = None

    def __str__(self):
        return 'AP RF config ' + self.name

    def __repr__(self):
        return 'AP RF config ' + self.name

    def update_name(self):
        if self.ap_name is not None and self.slot_id is not None:
            self.name = self.ap_name + '_slot' + self.slot_id

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Dynamic_Interface():  # Item for NamedList "dynamic interface" - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Dynamic Interface'
        self.name = None
        self.type = 'mixed'  # defines if class contain operational or config data
        self.interface_configuration = None
        self.interface_name = None
        self.mac_address = None
        self.ip_address = None
        self.ip_netmask = None
        self.ip_gateway = None
        self.external_nat_ip_state = None
        self.external_nat_ip_address = None
        self.link_local_ipv6_address = None
        self.state_link_local_ipv6 = None
        self.ipv6_address = None
        self.state_ipv6 = None
        self.ipv6_gateway = None
        self.ipv6_gateway_mac_address = None
        self.state_ipv6_gateway = None
        self.nas_identifier = None
        self.vlan = None
        self.quarantine_vlan = None
        self.active_physical_port = None
        self.primary_physical_port = None
        self.backup_physical_port = None
        self.dhcp_proxy_mode = None
        self.primary_dhcp_server = None
        self.secondary_dhcp_server = None
        self.dhcp_option_82 = None
        self.dhcp_option_82_bridge_mode_insertion = None
        self.ipv4_acl = None
        self.url_acl = None
        self.ipv6_acl = None
        self.url_acl1 = None
        self.mdns_profile_name = None
        self.ap_manager = None
        self.guest_interface = None
        self.d_3g_vlan = None
        self.l2_multicast = None
        self.slaac = None
        self.dhcp_protocol = None
        self.speed = None
        self.duplex = None
        self.auto_negotiation = None
        self.link_status = None
        self.virtual_dns_host_name = None
        self.remote_id_format = None
        self.link_select_suboption = None
        self.relay_src_intf = None
        self.vpn_select_suboption = None

    def __str__(self):
        return 'Dynamic interface ' + self.name

    def __repr__(self):
        return 'Dynamic interface ' + self.name

    def update_name(self):
        self.name = self.interface_name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Interface_Group():  # Item for NamedList "interface groups" - subclass of wlc_config
    def __init__(self, name=None):
        self.objname = 'Interface Group'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.name = None
        self.interface_group_name = None
        self.quarantine = None
        self.number_of_wlans_using_the_interface_group = None
        self.number_of_ap_groups_using_the_interface_group = None
        self.number_of_interfaces_contained = None
        self.mdns_profile_name = None
        self.failure_detect_mode = None
        self.interface_group_description = None
        self.interfaces = None

    def __str__(self):
        return 'Interface group ' + self.interface_group_name

    def __repr__(self):
        return 'Interface group ' + self.interface_group_name

    def update_name(self):
        self.name = self.interface_group_name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ssid_Config():  # Item for NamedList "WLANs" - subclass of wlc_config
    def __init__(self):
        self.objname = 'SSID config'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data
        self.wlan_identifier = None
        self.profile_name = None
        self.network_name_ssid = None
        self.status = None
        self.mac_filtering = None
        self.broadcast_ssid = None
        self.aaa_policy_override = None
        self.network_admission_control = None
        self.client_profiling_status = None
        self.client_profiling_status_radius_profiling = None
        self.client_profiling_status_radius_profiling_dhcp = None
        self.client_profiling_status_radius_profiling_http = None
        self.client_profiling_status_local_profiling = None
        self.client_profiling_status_local_profiling_dhcp = None
        self.client_profiling_status_local_profiling_http = None
        self.radius_nac_state = None
        self.snmp_nac_state = None
        self.quarantine_vlan = None
        self.maximum_clients_allowed = None
        self.security_group_tag = None
        self.maximum_number_of_clients_per_ap_radio = None
        self.atf_policy = None
        self.number_of_active_clients = None
        self.exclusionlist = None
        self.exclusionlist_timeout = None
        self.session_timeout = None
        self.user_idle_timeout = None
        self.sleep_client = None
        self.sleep_client_timeout = None
        self.web_auth_captive_bypass_mode = None
        self.user_idle_threshold = None
        self.nas_identifier = None
        self.chd_per_wlan = None
        self.webauth_dhcp_exclusion = None
        self.interface = None
        self.multicast_interface = None
        self.wlan_ipv4_acl = None
        self.wlan_ipv6_acl = None
        self.wlan_layer2_acl = None
        self.wlan_url_acl = None
        self.mdns_status = None
        self.mdns_profile_name = None
        self.dhcp_server = None
        self.central_nat_peer_peer_blocking = None
        self.dhcp_address_assignment_required = None
        self.static_ip_client_tunneling = None
        self.tunnel_profile = None
        self.pmipv6_mobility_type = None
        self.pmipv6_mobility_type_pmipv6_mag_profile = None
        self.pmipv6_mobility_type_pmipv6_default_realm = None
        self.pmipv6_mobility_type_pmipv6_nai_type = None
        self.pmipv6_mobility_type_pmipv6_mag_location = None
        self.quality_of_service = None
        self.per_ssid_rate_limits = None
        self.average_data_rate = None
        self.average_realtime_data_rate = None
        self.burst_data_rate = None
        self.burst_realtime_data_rate = None
        self.per_client_rate_limits = None
        self.average_data_rate = None
        self.average_realtime_data_rate = None
        self.burst_data_rate = None
        self.burst_realtime_data_rate = None
        self.scan_defer_priority = None
        self.scan_defer_time = None
        self.wmm = None
        self.wmm_uapsd_compliant_client_support = None
        self.media_stream_multicast_direct = None
        self.ccx_aironetie_support = None
        self.ccx_gratuitous_proberesponse_gpr = None
        self.ccx_diagnostics_channel_capability = None
        self.dot11_phone_mode_7920 = None
        self.wired_protocol = None
        self.passive_client_feature = None
        self.peer_to_peer_blocking_action = None
        self.radio_policy = None
        self.dtim_period_for_802_11a_radio = None
        self.dtim_period_for_802_11b_radio = None
        self.radius_servers = None
        self.radius_servers_authentication = None
        self.radius_servers_accounting = None
        self.radius_servers_accounting_interim_update = None
        self.radius_servers_accounting_interim_update_interval = None
        self.radius_servers_accounting_framed_ipv6_acct_avp = None
        self.radius_servers_dynamic_interface = None
        self.radius_servers_dynamic_interface_priority = None
        self.local_eap_authentication = None
        self.radius_nai_realm = None
        self.mu_mimo = None
        self.security = None
        self.security_802_11_authentication = None
        self.security_ft_support = None
        self.security_static_wep_keys = None
        self.security_802_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2 = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa_ssn_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_tkip_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_aes_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_ccmp256_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_gcmp128_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_gcmp256_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_osen_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_802_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_psk = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_cckm = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_ft_1x802_11r = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_ft_psk802_11r = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_pmf_1x802_11w = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_pmf_psk802_11w = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_osen_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_suiteb_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_auth_key_management_suiteb192_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_ft_reassociation_timeout = None
        self.security_wi_fi_protected_access_wpa_wpa2_ft_over_the_ds_mode = None
        self.security_wi_fi_protected_access_wpa_wpa2_gtk_randomization = None
        self.security_wi_fi_protected_access_wpa_wpa2_skc_cache_support = None
        self.security_wi_fi_protected_access_wpa_wpa2_cckm_tsf_tolerance = None
        self.security_wi_fi_direct_policy_configured = None
        self.security_eap_passthrough = None
        self.security_ckip = None
        self.security_web_based_authentication = None
        self.security_web_authentication_timeout = None
        self.security_web_passthrough = None
        self.security_mac_auth_server = None
        self.security_web_portal_server = None
        self.security_qrscan_des_key = None
        self.security_conditional_web_redirect = None
        self.security_splash_page_web_redirect = None
        self.security_auto_anchor = None
        self.security_flexconnect_local_switching = None
        self.security_flexconnect_central_association = None
        self.security_flexconnect_central_dhcp_flag = None
        self.security_flexconnect_nat_pat_flag = None
        self.security_flexconnect_dns_override_flag = None
        self.security_flexconnect_pppoe_pass_through = None
        self.security_flexconnect_local_switching_ip_source_guar = None
        self.security_flexconnect_vlan_based_central_switching = None
        self.security_flexconnect_local_authentication = None
        self.security_flexconnect_learn_ip_address = None
        self.security_client_mfp = None
        self.security_pmf = None
        self.security_pmf_association_comeback_time = None
        self.security_pmf_sa_query_retrytimeout = None
        self.security_tkip_mic_countermeasure_hold_down_timer = None
        self.security_eap_params = None
        self.avc_visibility = None
        self.avc_profile_name = None
        self.flex_avc_profile_name = None
        self.opendns_profile_name = None
        self.opendns_wlan_mode = None
        self.flow_monitor_name = None
        self.split_tunnel_configuration = None
        self.split_tunnel_configuration_split_tunnel = None
        self.call_snooping = None
        self.roamed_call_re_anchor_policy = None
        self.sip_cac_fail_send_486_busy_policy = None
        self.sip_cac_fail_send_dis_association_policy = None
        self.kts_based_cac_policy = None
        self.assisted_roaming_prediction_optimization = None
        self.d_802_11k_neighbor_list = None
        self.d_802_11k_neighbor_list_dual_band = None
        self.d_802_11v_directed_multicast_service = None
        self.d_802_11v_bss_max_idle_service = None
        self.d_802_11v_bss_transition_service = None
        self.d_802_11v_bss_transition_disassoc_imminent = None
        self.d_802_11v_bss_transition_disassoc_timer = None
        self.d_802_11v_bss_transition_oproam_disassoc_timer = None
        self.dms_db_is_empty = None
        self.band_select = None
        self.load_balancing = None
        self.multicast_buffer = None
        self.universal_ap_admin = None
        self.broadcast_tagging = None
        self.prp = None
        self.mobility_anchor_list = None
        self.d_802_11u = None
        self.msap_services = None
        self.local_policy = None
        self.priority__policy_name = None
        self.lync_state = None
        self.audio_qos_policy = None
        self.video_qos_policy = None
        self.app_share_qos_policy = None
        self.file_transfer_qos_policy = None
        self.qos_fastlane_status = None
        self.selective_reanchoring_status = None
        self.lobby_admin_access = None
        self.fabric_status = None
        self.vnid_name = None
        self.vnid = None
        self.applied_sgt_tag = None
        self.peer_ip_address = None
        self.flex_acl_name = None
        self.flex_avc_policy_name = None
        self.u3_interface = None
        self.u3_reporting_interval = None

    def update_name(self):
        self.name = self.network_name_ssid

    def __str__(self):
        return 'SSID config ' + self.name

    def __repr__(self):
        return 'SSID config ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Wlc_Config():
    def __init__(self, hostname=None, parsing_date=None, software_version=None, collection_time='None'):
        self.__wlc_config_version__ = '0.2.0'
        self.__parser_version__ = '0.81'
        self.software_version = software_version
        self.objname = 'WLC AireOS config'
        self.platform = None #9800\AireOS
        self.type = 'mixed'  # defines if class contain operational or config data
        self.name = None  # hostname?
        self.parsing_date = parsing_date
        self.collection_time = collection_time
        self.hostname = hostname
        self.dhcp_proxy = None
        self.dynamic_interfaces = NamedList('Dynamic Interfaces',
                                            'Dynamic_Interface')  # item type should be Dynamic Interface
        self.interface_group = NamedList('Interface Groups', 'Interface_Group')
        self.ssid = NamedList('SSIDs', 'Ssid_Config')  # item type should be Ssid_Config
        self.ap_rf = NamedList('AP RF Configs', 'Ap_Rf_Config')  # item type should be Ap_Rf_Config
        self.rogue_aps = NamedList('Rogue APs', 'Rogue_AP')
        self.ports = NamedList('Ports', 'Port')
        self.mobility_group_members = NamedList('Mobility group members', 'Mobility group member')
        self.radius_authentication_servers = NamedList('Radius authentication servers', 'Radius authentication server')
        self.radius_accounting_servers = NamedList('Radius accounting servers', 'Radius accounting server')
        self.ap_configs = NamedList('AP Configs', 'Ap_Config')
        self.dhcp_servers = NamedList('DHCP servers', 'Dhcp_Server')
        self.rf_profiles = NamedList('RF profiles', 'Rf_Profile')
        self.ap_groups = NamedList('AP Groups', 'Ap_Group')
        self.radius_config = Radius_Config()
        self.switch = Switch_Config()
        self.network = Network_Config()
        self.advanced = Advanced_Config()
        self.redundancy = Redundancy_Config()
        self.mobility_config = Mobility_Config()
        self.system = System_Config()
        self.band5 = Band5_Config()
        self.band24 = Band24_Config()
        self.cleanair_24 = Cleanair_24G_Config()
        self.cleanair_5 = Cleanair_5G_Config()
        self.ipv6 = Ipv6_Config()

    def add_subclass(self, object):
        if isinstance(object, NamedList):  # For Named LIST objects
            if object.item_name == 'Ssid_Config': self.ssid = object
            if object.item_name == 'Dynamic_Interface': self.dynamic_interfaces = object
            if object.item_name == 'Interface_Group': self.interface_group = object
            if object.item_name == 'Ap_Rf_Config': self.ap_rf = object
            if object.item_name == 'Rogue_AP': self.rogue_aps = object
            if object.item_name == 'Port': self.ports = object
            if object.item_name == 'Radius authentication server': self.radius_authentication_servers = object
            if object.item_name == 'Radius accounting server': self.radius_accounting_servers = object
            if object.item_name == 'Mobility group member': self.mobility_group_members = object
            if object.item_name == 'Rf_Profile': self.rf_profiles = object
            if object.item_name == 'Ap_Config': self.ap_configs = object  # Check item name here self.ap_configs = NamedList('AP Configs', 'Ap_Config')
            if object.item_name == 'Dhcp_Server': self.dhcp_servers = object
            if object.item_name == 'Ap_Group': self.ap_groups = object
            if object.item_name == 'Nearby_Ap':
                self.ap_rf[object.name].nearby_aps = object
        else:  ##For NON - Named List objects
            if isinstance(object, Switch_Config): self.switch = object
            if isinstance(object, Ipv6_Config): self.ipv6 = object
            if isinstance(object, Radius_Config): self.radius_config = object
            if isinstance(object, Network_Config): self.network = object
            if isinstance(object, Redundancy_Config): self.redundancy = object
            if isinstance(object, System_Config): self.system = object
            if isinstance(object, Advanced_Config): self.advanced = object
            if isinstance(object, Band5_Config): self.band5 = object
            if isinstance(object, Band24_Config): self.band24 = object
            if isinstance(object, Cleanair_24G_Config): self.cleanair_24 = object
            if isinstance(object, Cleanair_5G_Config): self.cleanair_5 = object
            if isinstance(object, Mobility_Config): self.mobility_config = object

    def __str__(self):
        return 'WLC config for host: ' + self.hostname + ', platform: ' + self.platform + ', version is ' + self.software_version + ', collection time is ' + self.collection_time + ', parsing date is ' + self.parsing_date

    def __repr__(self):
        return 'WLC config for host: ' + self.hostname + ', platform: ' + self.platform + ', version is ' + self.software_version + ', collection time is ' + self.collection_time + ', parsing date is ' + self.parsing_date

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

# AireOS PARSING DICTIONARIES SECTION

advanced_config_parsing_dict = {
    'Probe request filtering': 'probe_request_filtering',
    'Probes fwd to controller per client per radio': 'probes_fwd_to_controller_per_client_per_radio',
    'Probe request rate-limiting interval': 'probe_request_rate_limiting_interval',
    'Aggregate Probe request interval': 'aggregate_probe_request_interval',
    'Increased backoff parameters for probe respon': 'increased_backoff_parameters_for_probe',
    'EAP-Identity-Request Timeout (seconds)': 'eap_identity_request_timeout_seconds',
    'EAP-Identity-Request Max Retries': 'eap_identity_request_max_retries',
    'EAP Key-Index for Dynamic WEP': 'eap_key_index_for_dynamic_wep',
    'EAP Max-Login Ignore Identity Response': 'eap_max_login_ignore_identity_response',
    'EAP-Request Timeout (seconds)': 'eap_request_timeout_seconds',
    'EAP-Request Max Retries': 'eap_request_max_retries',
    'EAPOL-Key Timeout (milliseconds)': 'eapol_key_timeout_milliseconds',
    'EAPOL-Key Max Retries': 'eapol_key_max_retries',
    'EAP-Broadcast Key Interval': 'eap_broadcast_key_interval',
    'Fastpath Packet Capture': 'fastpath_packet_capture',
    'Fastpath Fast Cache Control': 'fastpath_fast_cache_control',
    'Fastpath Fast Testmode': 'fastpath_fast_testmode',
    'dot11-padding': 'dot11_padding',
    'padding-size': 'padding_size',
    'Advanced Hotspot Commands': 'advanced_hotspot_commands',
    'ANQP 4-way state': 'anqp_4_way_state',
    'GARP Broadcast state:': 'garp_broadcast_state',
    'GAS request rate limit': 'gas_request_rate_limit',
    'ANQP comeback delay in TUs(TU=1024usec)': 'anqp_comeback_delay',
}

ipv6_config_parsing_dict = {
    'Global Config': 'global_config',
    'Reachable-lifetime value': 'reachable_lifetime_value',
    'Stale-lifetime value': 'stale_lifetime_value',
    'Down-lifetime value': 'down_lifetime_value',
    'RA Throttling': 'ra_throttling',
    'RA Throttling allow at-least': 'ra_throttling_allow_at_least',
    'RA Throttling allow at-most': 'ra_throttling_allow_at_most',
    'RA Throttling max-through': 'ra_throttling_max_through',
    'RA Throttling throttle-period': 'ra_throttling_throttle_period',
    'RA Throttling interval-option': 'ra_throttling_interval_option',
    'NS Mulitcast CacheMiss Forwarding': 'ns_mulitcast_cachemiss_forwarding',
    'NA Mulitcast Forwarding': 'na_mulitcast_forwarding',
    'IPv6 Capwap UDP Lite': 'ipv6_capwap_udp_lite',
    'Operating System IPv6 state': 'operating_system_ipv6_state',
}

radius_config_parsing_dict = {
    'Vendor Id Backward Compatibility': 'vendor_id_backward_compatibility',
    'Call Station Id Case': 'call_station_id_case',
    'Accounting Call Station Id Type': 'accounting_call_station_id_type',
    'Auth Call Station Id Type': 'auth_call_station_id_type',
    'Extended Source Ports Support': 'extended_source_ports_support',
    'Aggressive Failover': 'aggressive_failover',
    'Keywrap': 'keywrap',
    'Fallback Test:': 'fallback_test',
    'Test Mode': 'fallback_test_test_mode',
    'Probe User Name': 'fallback_test_probe_user_name',
    'Interval (in seconds)': 'fallback_test_interval_in_seconds',
    'MAC Delimiter for Authentication Messages': 'mac_delimiter_for_authentication_messages',
    'MAC Delimiter for Accounting Messages': 'mac_delimiter_for_accounting_messages',
    'RADIUS Authentication Framed-MTU': 'radius_authentication_framed_mtu',
}

ap_group_parsing_dict = {
    'Site Name': 'site_name',
    'Site Description': 'site_description',
    'Venue Group Code': 'venue_group_code',
    'Venue Type Code': 'venue_type_code',
    'NAS-identifier': 'nas_identifier',
    'Client Traffic QinQ Enable': 'client_traffic_qinq_enable',
    'DHCPv4 QinQ Enable': 'dhcpv4_qinq_enable',
    'AP Operating Class': 'ap_operating_class',
    'Capwap Prefer Mode': 'capwap_prefer_mode',
    'Antenna Monitoring - Status': 'antenna_monitoring_status',
    '2.4 GHz band': 'rf_profile_24',
    '5 GHz band': 'rf_profile_5',
    'Fabric Flex Acl Template Name': 'fabric_flex_acl_template_name',
}
band_24_parsing_dict = {
    '802.11b Network': 'd_802_11b_network',
    '11gSupport': 'd_11gsupport',
    '11nSupport': 'd_11nsupport',
    '802.11b/g Operational Rates': 'd_802_11b_g_operational_rates',
    '802.11b 1M Rate': 'd_802_11b_g_operational_rates_802_11b_g_1m_rate',
    '802.11b 2M Rate': 'd_802_11b_g_operational_rates_802_11b_g_2m_rate',
    '802.11b 5.5M Rate': 'd_802_11b_g_operational_rates_802_11b_g_5_5m_rate',
    '802.11b 11M Rate': 'd_802_11b_g_operational_rates_802_11b_g_11m_rate',
    '802.11b/g 1M Rate': 'd_802_11b_g_operational_rates_802_11b_g_1m_rate',
    '802.11b/g 2M Rate': 'd_802_11b_g_operational_rates_802_11b_g_2m_rate',
    '802.11b/g 5.5M Rate': 'd_802_11b_g_operational_rates_802_11b_g_5_5m_rate',
    '802.11b/g 11M Rate': 'd_802_11b_g_operational_rates_802_11b_g_11m_rate',
    '802.11g 6M Rate': 'd_802_11b_g_operational_rates_802_11g_6m_rate',
    '802.11g 9M Rate': 'd_802_11b_g_operational_rates_802_11g_9m_rate',
    '802.11g 12M Rate': 'd_802_11b_g_operational_rates_802_11g_12m_rate',
    '802.11g 18M Rate': 'd_802_11b_g_operational_rates_802_11g_18m_rate',
    '802.11g 24M Rate': 'd_802_11b_g_operational_rates_802_11g_24m_rate',
    '802.11g 36M Rate': 'd_802_11b_g_operational_rates_802_11g_36m_rate',
    '802.11g 48M Rate': 'd_802_11b_g_operational_rates_802_11g_48m_rate',
    '802.11g 54M Rate': 'd_802_11b_g_operational_rates_802_11g_54m_rate',
    '802.11n MCS Settings:': 'd_802_11n_mcs_settings',
    'MCS 0': 'd_802_11n_mcs_settings_mcs_0',
    'MCS 1': 'd_802_11n_mcs_settings_mcs_1',
    'MCS 2': 'd_802_11n_mcs_settings_mcs_2',
    'MCS 3': 'd_802_11n_mcs_settings_mcs_3',
    'MCS 4': 'd_802_11n_mcs_settings_mcs_4',
    'MCS 5': 'd_802_11n_mcs_settings_mcs_5',
    'MCS 6': 'd_802_11n_mcs_settings_mcs_6',
    'MCS 7': 'd_802_11n_mcs_settings_mcs_7',
    'MCS 8': 'd_802_11n_mcs_settings_mcs_8',
    'MCS 9': 'd_802_11n_mcs_settings_mcs_9',
    'MCS 10': 'd_802_11n_mcs_settings_mcs_10',
    'MCS 11': 'd_802_11n_mcs_settings_mcs_11',
    'MCS 12': 'd_802_11n_mcs_settings_mcs_12',
    'MCS 13': 'd_802_11n_mcs_settings_mcs_13',
    'MCS 14': 'd_802_11n_mcs_settings_mcs_14',
    'MCS 15': 'd_802_11n_mcs_settings_mcs_15',
    'MCS 16': 'd_802_11n_mcs_settings_mcs_16',
    'MCS 17': 'd_802_11n_mcs_settings_mcs_17',
    'MCS 18': 'd_802_11n_mcs_settings_mcs_18',
    'MCS 19': 'd_802_11n_mcs_settings_mcs_19',
    'MCS 20': 'd_802_11n_mcs_settings_mcs_20',
    'MCS 21': 'd_802_11n_mcs_settings_mcs_21',
    'MCS 22': 'd_802_11n_mcs_settings_mcs_22',
    'MCS 23': 'd_802_11n_mcs_settings_mcs_23',
    'MCS 24': 'd_802_11n_mcs_settings_mcs_24',
    'MCS 25': 'd_802_11n_mcs_settings_mcs_25',
    'MCS 26': 'd_802_11n_mcs_settings_mcs_26',
    'MCS 27': 'd_802_11n_mcs_settings_mcs_27',
    'MCS 28': 'd_802_11n_mcs_settings_mcs_28',
    'MCS 29': 'd_802_11n_mcs_settings_mcs_29',
    'MCS 30': 'd_802_11n_mcs_settings_mcs_30',
    'MCS 31': 'd_802_11n_mcs_settings_mcs_31',
    '802.11n Status:': 'd_802_11n_status',
    'A-MPDU Tx:': 'd_802_11n_status_a_mpdu_tx',
    'Priority 0': 'd_802_11n_status_a_mpdu_tx_priority_0',
    'Priority 1': 'd_802_11n_status_a_mpdu_tx_priority_1',
    'Priority 2': 'd_802_11n_status_a_mpdu_tx_priority_2',
    'Priority 3': 'd_802_11n_status_a_mpdu_tx_priority_3',
    'Priority 4': 'd_802_11n_status_a_mpdu_tx_priority_4',
    'Priority 5': 'd_802_11n_status_a_mpdu_tx_priority_5',
    'Priority 6': 'd_802_11n_status_a_mpdu_tx_priority_6',
    'Priority 7': 'd_802_11n_status_a_mpdu_tx_priority_7',
    'Aggregation scheduler': 'd_802_11n_status_a_mpdu_tx_aggregation_scheduler',
    'Realtime Timeout': 'd_802_11n_status_a_mpdu_tx_aggregation_scheduler_realtime_timeout',
    'Non Realtime Timeout': 'd_802_11n_status_a_mpdu_tx_aggregation_scheduler_non_realtime_timeout',
    'A-MSDU Tx:': 'd_802_11n_status_a_msdu_tx',
    'Priority 01': 'd_802_11n_status_a_msdu_tx_priority_0',
    'Priority 11': 'd_802_11n_status_a_msdu_tx_priority_1',
    'Priority 21': 'd_802_11n_status_a_msdu_tx_priority_2',
    'Priority 31': 'd_802_11n_status_a_msdu_tx_priority_3',
    'Priority 41': 'd_802_11n_status_a_msdu_tx_priority_4',
    'Priority 51': 'd_802_11n_status_a_msdu_tx_priority_5',
    'Priority 61': 'd_802_11n_status_a_msdu_tx_priority_6',
    'Priority 71': 'd_802_11n_status_a_msdu_tx_priority_7',
    'A-MSDU Max Subframes': 'd_802_11n_status_a_msdu_max_subframes',
    'A-MSDU MAX Length': 'd_802_11n_status_a_msdu_max_length',
    'Rifs Rx': 'd_802_11n_status_rifs_rx',
    'Guard Interval': 'd_802_11n_status_guard_interval',
    'Beacon Interval': 'beacon_interval',
    'CF Pollable mode': 'cf_pollable_mode',
    'CF Poll Request mandatory': 'cf_poll_request_mandatory',
    'CFP Period': 'cfp_period',
    'CFP Maximum Duration': 'cfp_maximum_duration',
    'Default Channel': 'default_channel',
    'Default Tx Power Level': 'default_tx_power_level',
    'DTPC  Status': 'dtpc_status',
    'RSSI Low Check': 'rssi_low_check',
    'RSSI Threshold': 'rssi_threshold',
    'Call Admission Limit': 'call_admission_limit',
    'G711 CU Quantum': 'g711_cu_quantum',
    'ED Threshold': 'ed_threshold',
    'Fragmentation Threshold': 'fragmentation_threshold',
    'PBCC mandatory': 'pbcc_mandatory',
    'RTS Threshold': 'rts_threshold',
    'Short Preamble mandatory': 'short_preamble_mandatory',
    'Short Retry Limit': 'short_retry_limit',
    'Legacy Tx Beamforming setting': 'legacy_tx_beamforming_setting',
    'Traffic Stream Metrics Status': 'traffic_stream_metrics_status',
    'Expedited BW Request Status': 'expedited_bw_request_status',
    'World Mode': 'world_mode',
    'Faster Carrier Tracking Loop': 'faster_carrier_tracking_loop',
    'EDCA profile type': 'edca_profile_type',
    'Voice MAC optimization status': 'voice_mac_optimization_status',
    'Call Admission Control (CAC) configuration': 'call_admission_control_cac_configuration',
    'Voice AC - Admission control (ACM)': 'call_admission_control_cac_configuration_voice_ac_admission_control_acm',
    'Voice Stream-Size': 'call_admission_control_cac_configuration_voice_stream_size',
    'Voice Max-Streams': 'call_admission_control_cac_configuration_voice_max_streams',
    'Voice max RF bandwidth': 'call_admission_control_cac_configuration_voice_max_rf_bandwidth',
    'Voice reserved roaming bandwidth': 'call_admission_control_cac_configuration_voice_reserved_roaming_bandwidth',
    'Voice CAC Method': 'call_admission_control_cac_configuration_voice_cac_method',
    'Voice tspec inactivity timeout': 'call_admission_control_cac_configuration_voice_tspec_inactivity_timeout',
    'CAC SIP-Voice configuration': 'cac_sip_voice_configuration',
    'SIP based CAC': 'cac_sip_voice_configuration_sip_based_cac',
    'SIP Codec Type': 'cac_sip_voice_configuration_sip_codec_type',
    'SIP call bandwidth:': 'cac_sip_voice_configuration_sip_call_bandwidth',
    'SIP call bandwidth sample-size': 'cac_sip_voice_configuration_sip_call_bandwidth_sample_size',
    'Video AC - Admission control (ACM)': 'cac_sip_voice_configuration_video_ac_admission_control_acm',
    'Video max RF bandwidth': 'cac_sip_voice_configuration_video_max_rf_bandwidth',
    'Video reserved roaming bandwidth': 'cac_sip_voice_configuration_video_reserved_roaming_bandwidth',
    'Video load-based CAC mode': 'cac_sip_voice_configuration_video_load_based_cac_mode',
    'Video CAC Method': 'cac_sip_voice_configuration_video_cac_method',
    'CAC SIP-Video configuration': 'cac_sip_video_configuration',
    'SIP based CAC1': 'cac_sip_video_configuration_sip_based_cac',
    'Best-effort AC - Admission control (ACM)': 'cac_sip_video_configuration_best_effort_ac_admission_control_acm',
    'Background AC - Admission control (ACM)': 'cac_sip_video_configuration_background_ac_admission_control_acm',
    'Maximum Number of Clients per AP': 'maximum_number_of_clients_per_ap',
    'L2Roam 802.11bg RF Parameters': 'l2roam_802_11bg_rf_parameters',
    'Config Mode': 'l2roam_802_11bg_rf_parameters_config_mode',
    'Minimum RSSI': 'l2roam_802_11bg_rf_parameters_minimum_rssi',
    'Roam Hysteresis': 'l2roam_802_11bg_rf_parameters_roam_hysteresis',
    'Scan Threshold': 'l2roam_802_11bg_rf_parameters_scan_threshold',
    'Transition time': 'l2roam_802_11bg_rf_parameters_transition_time',
}

band_5_parsing_dict = {
    '802.11a Network': 'd_802_11a_network',
    '11acSupport': 'd_11acsupport',
    '11nSupport': 'd_11nsupport',
    '802.11a Low Band': 'd_11nsupport_802_11a_low_band',
    '802.11a Mid Band': 'd_11nsupport_802_11a_mid_band',
    '802.11a High Band': 'd_11nsupport_802_11a_high_band',
    '802.11a Operational Rates': 'd_802_11a_operational_rates',
    '802.11a 6M Rate': 'd_802_11a_operational_rates_802_11a_6m_rate',
    '802.11a 9M Rate': 'd_802_11a_operational_rates_802_11a_9m_rate',
    '802.11a 12M Rate': 'd_802_11a_operational_rates_802_11a_12m_rate',
    '802.11a 18M Rate': 'd_802_11a_operational_rates_802_11a_18m_rate',
    '802.11a 24M Rate': 'd_802_11a_operational_rates_802_11a_24m_rate',
    '802.11a 36M Rate': 'd_802_11a_operational_rates_802_11a_36m_rate',
    '802.11a 48M Rate': 'd_802_11a_operational_rates_802_11a_48m_rate',
    '802.11a 54M Rate': 'd_802_11a_operational_rates_802_11a_54m_rate',
    '802.11n MCS Settings:': 'd_802_11n_mcs_settings',
    'MCS 0': 'd_802_11n_mcs_settings_mcs_0',
    'MCS 1': 'd_802_11n_mcs_settings_mcs_1',
    'MCS 2': 'd_802_11n_mcs_settings_mcs_2',
    'MCS 3': 'd_802_11n_mcs_settings_mcs_3',
    'MCS 4': 'd_802_11n_mcs_settings_mcs_4',
    'MCS 5': 'd_802_11n_mcs_settings_mcs_5',
    'MCS 6': 'd_802_11n_mcs_settings_mcs_6',
    'MCS 7': 'd_802_11n_mcs_settings_mcs_7',
    'MCS 8': 'd_802_11n_mcs_settings_mcs_8',
    'MCS 9': 'd_802_11n_mcs_settings_mcs_9',
    'MCS 10': 'd_802_11n_mcs_settings_mcs_10',
    'MCS 11': 'd_802_11n_mcs_settings_mcs_11',
    'MCS 12': 'd_802_11n_mcs_settings_mcs_12',
    'MCS 13': 'd_802_11n_mcs_settings_mcs_13',
    'MCS 14': 'd_802_11n_mcs_settings_mcs_14',
    'MCS 15': 'd_802_11n_mcs_settings_mcs_15',
    'MCS 16': 'd_802_11n_mcs_settings_mcs_16',
    'MCS 17': 'd_802_11n_mcs_settings_mcs_17',
    'MCS 18': 'd_802_11n_mcs_settings_mcs_18',
    'MCS 19': 'd_802_11n_mcs_settings_mcs_19',
    'MCS 20': 'd_802_11n_mcs_settings_mcs_20',
    'MCS 21': 'd_802_11n_mcs_settings_mcs_21',
    'MCS 22': 'd_802_11n_mcs_settings_mcs_22',
    'MCS 23': 'd_802_11n_mcs_settings_mcs_23',
    'MCS 24': 'd_802_11n_mcs_settings_mcs_24',
    'MCS 25': 'd_802_11n_mcs_settings_mcs_25',
    'MCS 26': 'd_802_11n_mcs_settings_mcs_26',
    'MCS 27': 'd_802_11n_mcs_settings_mcs_27',
    'MCS 28': 'd_802_11n_mcs_settings_mcs_28',
    'MCS 29': 'd_802_11n_mcs_settings_mcs_29',
    'MCS 30': 'd_802_11n_mcs_settings_mcs_30',
    'MCS 31': 'd_802_11n_mcs_settings_mcs_31',
    '802.11ac MCS Settings:': 'd_802_11ac_mcs_settings',
    'Nss=1: MCS 0-9': 'd_802_11ac_mcs_settings_nss_1_mcs_0_9',
    'Nss=2: MCS 0-9': 'd_802_11ac_mcs_settings_nss_2_mcs_0_9',
    'Nss=3: MCS 0-9': 'd_802_11ac_mcs_settings_nss_3_mcs_0_9',
    'Nss=4: MCS 0-7': 'd_802_11ac_mcs_settings_nss_4_mcs_0_7',
    'Nss=4: MCS 0-9': 'd_802_11ac_mcs_settings_nss_4_mcs_0_9',
    '802.11n Status:': 'd_802_11n_status',
    'A-MPDU Tx:': 'd_802_11n_status_a_mpdu_tx',
    'Priority 0': 'd_802_11n_status_a_mpdu_tx_priority_0',
    'Priority 1': 'd_802_11n_status_a_mpdu_tx_priority_1',
    'Priority 2': 'd_802_11n_status_a_mpdu_tx_priority_2',
    'Priority 3': 'd_802_11n_status_a_mpdu_tx_priority_3',
    'Priority 4': 'd_802_11n_status_a_mpdu_tx_priority_4',
    'Priority 5': 'd_802_11n_status_a_mpdu_tx_priority_5',
    'Priority 6': 'd_802_11n_status_a_mpdu_tx_priority_6',
    'Priority 7': 'd_802_11n_status_a_mpdu_tx_priority_7',
    'Aggregation scheduler': 'd_802_11n_status_a_mpdu_tx_aggregation_scheduler',
    'Frame Burst': 'd_802_11n_status_a_mpdu_tx_frame_burst',
    'Realtime Timeout': 'd_802_11n_status_a_mpdu_tx_frame_burst_realtime_timeout',
    'Non Realtime Timeout': 'd_802_11n_status_a_mpdu_tx_frame_burst_non_realtime_timeout',
    'A-MSDU Tx:': 'd_802_11n_status_a_msdu_tx',
    'Priority 01': 'd_802_11n_status_a_msdu_tx_priority_0',
    'Priority 11': 'd_802_11n_status_a_msdu_tx_priority_1',
    'Priority 21': 'd_802_11n_status_a_msdu_tx_priority_2',
    'Priority 31': 'd_802_11n_status_a_msdu_tx_priority_3',
    'Priority 41': 'd_802_11n_status_a_msdu_tx_priority_4',
    'Priority 51': 'd_802_11n_status_a_msdu_tx_priority_5',
    'Priority 61': 'd_802_11n_status_a_msdu_tx_priority_6',
    'Priority 71': 'd_802_11n_status_a_msdu_tx_priority_7',
    'A-MSDU Max Subframes': 'd_802_11n_status_a_msdu_max_subframes',
    'A-MSDU MAX Length': 'd_802_11n_status_a_msdu_max_length',
    'Rifs Rx': 'd_802_11n_status_rifs_rx',
    'Guard Interval': 'd_802_11n_status_guard_interval',
    'Beacon Interval': 'beacon_interval',
    'CF Pollable mandatory': 'cf_pollable_mandatory',
    'CF Poll Request mandatory': 'cf_poll_request_mandatory',
    'CFP Period': 'cfp_period',
    'CFP Maximum Duration': 'cfp_maximum_duration',
    'Default Channel': 'default_channel',
    'Default Tx Power Level': 'default_tx_power_level',
    'DTPC  Status': 'dtpc_status',
    'Fragmentation Threshold': 'fragmentation_threshold',
    'RSSI Low Check': 'rssi_low_check',
    'RSSI Threshold': 'rssi_threshold',
    'TI Threshold': 'ti_threshold',
    'Legacy Tx Beamforming setting': 'legacy_tx_beamforming_setting',
    'Traffic Stream Metrics Status': 'traffic_stream_metrics_status',
    'Expedited BW Request Status': 'expedited_bw_request_status',
    'World Mode': 'world_mode',
    'dfs-peakdetect': 'dfs_peakdetect',
    'EDCA profile type': 'edca_profile_type',
    'Voice MAC optimization status': 'voice_mac_optimization_status',
    'Call Admission Control (CAC) configuration': 'call_admission_control_cac_configuration',
    'Voice AC:': 'voice_ac',
    'Voice AC - Admission control (ACM)': 'voice_ac_voice_ac_admission_control_acm',
    'Voice Stream-Size': 'voice_ac_voice_stream_size',
    'Voice Max-Streams': 'voice_ac_voice_max_streams',
    'Voice max RF bandwidth': 'voice_ac_voice_max_rf_bandwidth',
    'Voice reserved roaming bandwidth': 'voice_ac_voice_reserved_roaming_bandwidth',
    'Voice CAC Method': 'voice_ac_voice_cac_method',
    'Voice tspec inactivity timeout': 'voice_ac_voice_tspec_inactivity_timeout',
    'CAC SIP-Voice configuration': 'cac_sip_voice_configuration',
    'SIP based CAC': 'cac_sip_voice_configuration_sip_based_cac',
    'SIP Codec Type': 'cac_sip_voice_configuration_sip_codec_type',
    'SIP call bandwidth': 'cac_sip_voice_configuration_sip_call_bandwidth',
    'SIP call bandwith sample-size': 'cac_sip_voice_configuration_sip_call_bandwith_sample_size',
    'Video AC:': 'video_ac',
    'Video AC - Admission control (ACM)': 'video_ac_video_ac_admission_control_acm',
    'Video max RF bandwidth': 'video_ac_video_max_rf_bandwidth',
    'Video reserved roaming bandwidth': 'video_ac_video_reserved_roaming_bandwidth',
    'Video load-based CAC mode': 'video_ac_video_load_based_cac_mode',
    'Video CAC Method': 'video_ac_video_cac_method',
    'CAC SIP-Video Configuration': 'cac_sip_video_configuration',
    'SIP based CAC1': 'cac_sip_video_configuration_sip_based_cac',
    'Best-effort AC - Admission control (ACM)': 'cac_sip_video_configuration_best_effort_ac_admission_control_acm',
    'Background AC - Admission control (ACM)': 'cac_sip_video_configuration_background_ac_admission_control_acm',
    'Maximum Number of Clients per AP Radio': 'maximum_number_of_clients_per_ap_radio',
    'L2Roam 802.11a RF Parameters': 'l2roam_802_11a_rf_parameters',
    'Config Mode': 'l2roam_802_11a_rf_parameters_config_mode',
    'Minimum RSSI': 'l2roam_802_11a_rf_parameters_minimum_rssi',
    'Roam Hysteresis': 'l2roam_802_11a_rf_parameters_roam_hysteresis',
    'Scan Threshold': 'l2roam_802_11a_rf_parameters_scan_threshold',
    'Transition time': 'l2roam_802_11a_rf_parameters_transition_time',
    '802.11h Configuration': 'd_802_11h_configuration',
    'Power Constraint': 'power_constraint',
    'Channel Switch': 'channel_switch',
    'Channel Mode': 'channel_mode',
    'Smart DFS': 'smart_dfs',
}

cleanair_5g_parsing_dict = {
    'Clean Air Solution': 'clean_air_solution',
    'Air Quality Settings:': 'air_quality_settings',
    'Air Quality Reporting': 'air_quality_settings_air_quality_reporting',
    'Air Quality Reporting Period (min)': 'air_quality_settings_air_quality_reporting_period_min',
    'Air Quality Alarms': 'air_quality_settings_air_quality_alarms',
    'Air Quality Alarm Threshold': 'air_quality_settings_air_quality_alarms_air_quality_alarm_threshold',
    'Unclassified Interference': 'air_quality_settings_air_quality_alarms_unclassified_interference',
    'Unclassified Severity Threshold': 'air_quality_settings_air_quality_alarms_unclassified_severity_threshold',
    'Interference Device Reporting': 'air_quality_settings_interference_device_reporting',
    'Interference Device Types:': 'air_quality_settings_interference_device_types',
    'TDD Transmitter': 'air_quality_settings_interference_device_types_tdd_transmitter',
    'Jammer': 'air_quality_settings_interference_device_types_jammer',
    'Continuous Transmitter': 'air_quality_settings_interference_device_types_continuous_transmitter',
    'DECT-like Phone': 'air_quality_settings_interference_device_types_dect_like_phone',
    'Video Camera': 'air_quality_settings_interference_device_types_video_camera',
    'WiFi Inverted': 'air_quality_settings_interference_device_types_wifi_inverted',
    'WiFi Invalid Channel': 'air_quality_settings_interference_device_types_wifi_invalid_channel',
    'SuperAG': 'air_quality_settings_interference_device_types_superag',
    'Canopy': 'air_quality_settings_interference_device_types_canopy',
    'WiMax Mobile': 'air_quality_settings_interference_device_types_wimax_mobile',
    'WiMax Fixed': 'air_quality_settings_interference_device_types_wimax_fixed',
    'Interference Device Alarms': 'air_quality_settings_interference_device_alarms',
    'Interference Device Types Triggering Alarms:': 'air_quality_settings_interference_device_types_triggering_alarms',
    'TDD Transmitter1': 'air_quality_settings_interference_device_types_triggering_alarms_tdd_transmitter',
    'Jammer1': 'air_quality_settings_interference_device_types_triggering_alarms_jammer',
    'Continuous Transmitter1': 'air_quality_settings_interference_device_types_triggering_alarms_continuous_transmitter',
    'DECT-like Phone1': 'air_quality_settings_interference_device_types_triggering_alarms_dect_like_phone',
    'Video Camera1': 'air_quality_settings_interference_device_types_triggering_alarms_video_camera',
    'WiFi Inverted1': 'air_quality_settings_interference_device_types_triggering_alarms_wifi_inverted',
    'WiFi Invalid Channel1': 'air_quality_settings_interference_device_types_triggering_alarms_wifi_invalid_channel',
    'SuperAG1': 'air_quality_settings_interference_device_types_triggering_alarms_superag',
    'Canopy1': 'air_quality_settings_interference_device_types_triggering_alarms_canopy',
    'WiMax Mobile1': 'air_quality_settings_interference_device_types_triggering_alarms_wimax_mobile',
    'WiMax Fixed1': 'air_quality_settings_interference_device_types_triggering_alarms_wimax_fixed',
    'Additional Clean Air Settings:': 'additional_clean_air_settings',
    'CleanAir ED-RRM State': 'additional_clean_air_settings_cleanair_ed_rrm_state',
    'CleanAir ED-RRM Sensitivity': 'additional_clean_air_settings_cleanair_ed_rrm_sensitivity',
    'CleanAir ED-RRM Custom Threshold': 'additional_clean_air_settings_cleanair_ed_rrm_custom_threshold',
    'CleanAir Rogue Contribution': 'additional_clean_air_settings_cleanair_rogue_contribution',
    'CleanAir Rogue Duty-Cycle Threshold': 'additional_clean_air_settings_cleanair_rogue_duty_cycle_threshold',
    'CleanAir Persistent Devices state': 'additional_clean_air_settings_cleanair_persistent_devices_state',
    'CleanAir Persistent Device Propagation': 'additional_clean_air_settings_cleanair_persistent_device_propagation',
}

cleanair_24g_parsing_dict = {
    'Clean Air Solution': 'clean_air_solution',
    'Air Quality Settings:': 'air_quality_settings',
    'Air Quality Reporting': 'air_quality_settings_air_quality_reporting',
    'Air Quality Reporting Period (min)': 'air_quality_settings_air_quality_reporting_period_min',
    'Air Quality Alarms': 'air_quality_settings_air_quality_alarms',
    'Air Quality Alarm Threshold': 'air_quality_settings_air_quality_alarms_air_quality_alarm_threshold',
    'Unclassified Interference': 'air_quality_settings_air_quality_alarms_unclassified_interference',
    'Unclassified Severity Threshold': 'air_quality_settings_air_quality_alarms_unclassified_severity_threshold',
    'Interference Device Reporting': 'air_quality_settings_interference_device_reporting',
    'Interference Device Types:': 'air_quality_settings_interference_device_types',
    'Bluetooth Link': 'air_quality_settings_interference_device_types_bluetooth_link',
    'Microwave Oven': 'air_quality_settings_interference_device_types_microwave_oven',
    '802.11 FH': 'air_quality_settings_interference_device_types_802_11_fh',
    'Bluetooth Discovery': 'air_quality_settings_interference_device_types_bluetooth_discovery',
    'TDD Transmitter': 'air_quality_settings_interference_device_types_tdd_transmitter',
    'Jammer': 'air_quality_settings_interference_device_types_jammer',
    'Continuous Transmitter': 'air_quality_settings_interference_device_types_continuous_transmitter',
    'DECT-like Phone': 'air_quality_settings_interference_device_types_dect_like_phone',
    'Video Camera': 'air_quality_settings_interference_device_types_video_camera',
    '802.15.4': 'air_quality_settings_interference_device_types_802_15_4',
    'WiFi Inverted': 'air_quality_settings_interference_device_types_wifi_inverted',
    'WiFi Invalid Channel': 'air_quality_settings_interference_device_types_wifi_invalid_channel',
    'SuperAG': 'air_quality_settings_interference_device_types_superag',
    'Canopy': 'air_quality_settings_interference_device_types_canopy',
    'Microsoft Device': 'air_quality_settings_interference_device_types_microsoft_device',
    'WiMax Mobile': 'air_quality_settings_interference_device_types_wimax_mobile',
    'WiMax Fixed': 'air_quality_settings_interference_device_types_wimax_fixed',
    'BLE Beacon': 'air_quality_settings_interference_device_types_ble_beacon',
    'Interference Device Alarms': 'air_quality_settings_interference_device_alarms',
    'Interference Device Types Triggering Alarms:': 'air_quality_settings_interference_device_types_triggering_alarms',
    'Bluetooth Link1': 'air_quality_settings_interference_device_types_triggering_alarms_bluetooth_link',
    'Microwave Oven1': 'air_quality_settings_interference_device_types_triggering_alarms_microwave_oven',
    '802.11 FH1': 'air_quality_settings_interference_device_types_triggering_alarms_802_11_fh',
    'Bluetooth Discovery1': 'air_quality_settings_interference_device_types_triggering_alarms_bluetooth_discovery',
    'TDD Transmitter1': 'air_quality_settings_interference_device_types_triggering_alarms_tdd_transmitter',
    'Jammer1': 'air_quality_settings_interference_device_types_triggering_alarms_jammer',
    'Continuous Transmitter1': 'air_quality_settings_interference_device_types_triggering_alarms_continuous_transmitter',
    'DECT-like Phone1': 'air_quality_settings_interference_device_types_triggering_alarms_dect_like_phone',
    'Video Camera1': 'air_quality_settings_interference_device_types_triggering_alarms_video_camera',
    '802.15.41': 'air_quality_settings_interference_device_types_triggering_alarms_802_15_4',
    'WiFi Inverted1': 'air_quality_settings_interference_device_types_triggering_alarms_wifi_inverted',
    'WiFi Invalid Channel1': 'air_quality_settings_interference_device_types_triggering_alarms_wifi_invalid_channel',
    'SuperAG1': 'air_quality_settings_interference_device_types_triggering_alarms_superag',
    'Canopy1': 'air_quality_settings_interference_device_types_triggering_alarms_canopy',
    'Microsoft Device1': 'air_quality_settings_interference_device_types_triggering_alarms_microsoft_device',
    'WiMax Mobile1': 'air_quality_settings_interference_device_types_triggering_alarms_wimax_mobile',
    'WiMax Fixed1': 'air_quality_settings_interference_device_types_triggering_alarms_wimax_fixed',
    'BLE Beacon1': 'air_quality_settings_interference_device_types_triggering_alarms_ble_beacon',
    'Additional Clean Air Settings:': 'additional_clean_air_settings',
    'CleanAir ED-RRM State': 'additional_clean_air_settings_cleanair_ed_rrm_state',
    'CleanAir ED-RRM Sensitivity': 'additional_clean_air_settings_cleanair_ed_rrm_sensitivity',
    'CleanAir ED-RRM Custom Threshold': 'additional_clean_air_settings_cleanair_ed_rrm_custom_threshold',
    'CleanAir Rogue Contribution': 'additional_clean_air_settings_cleanair_rogue_contribution',
    'CleanAir Rogue Duty-Cycle Threshold': 'additional_clean_air_settings_cleanair_rogue_duty_cycle_threshold',
    'CleanAir Persistent Devices state': 'additional_clean_air_settings_cleanair_persistent_devices_state',
    'CleanAir Persistent Device Propagation': 'additional_clean_air_settings_cleanair_persistent_device_propagation',
}

system_info_parsing_dict = {
    'Burned-in MAC Address': 'burned_in_mac_address',
    'Maximum number of APs supported': 'maximum_number_of_aps_supported',
    'System Information': 'system_information',
    'Manufacturer': 'manufacturers_name',
    'Product Name': 'product_name',
    'Build Info': 'build_info',
    'Product Version': 'product_version',
    'RTOS Version': 'rtos_version',
    'Bootloader Version': 'bootloader_version',
    'Emergency Image Version': 'emergency_image_version',
    'Field Recovery Image Version': 'field_recovery_image_version',
    'Firmware Version': 'firmware_version',
    'OUI File Update Time': 'oui_file_update_time',
    'Build Type': 'build_type',
    'OUI File Last Update Time': 'oui_file_last_update_time',
    'Build Type1': 'build_type',
    'System Name': 'system_name',
    'System Location': 'system_location',
    'System Contact': 'system_contact',
    'System ObjectID': 'system_objectid',
    'Redundancy Mode': 'redundancy_mode',
    'IP Address': 'ip_address',
    'IPv6 Address': 'ipv6_address',
    'Last Reset': 'last_reset',
    'System Up Time': 'system_up_time',
    'System Timezone Location': 'system_timezone_location',
    'System Stats Realtime Interval': 'system_stats_realtime_interval',
    'System Stats Normal Interval': 'system_stats_normal_interval',
    'Configured Country': 'configured_country',
    'Operating Environment': 'operating_environment',
    'Internal Temp Alarm Limits': 'internal_temp_alarm_limits',
    'Internal Temperature': 'internal_temperature',
    'Mgig Temp Alarm Limits': 'mgig_temp_alarm_limits',
    'Mgig Temperature': 'mgig_temperature',
    'External Temp Alarm Limits': 'external_temp_alarm_limits',
    'External Temperature': 'external_temperature',
    'Fan Status': 'fan_status',
    'Fan Speed Mode': 'fan_speed_mode',
    'Power Supply 1': 'power_supply_1',
    'Power Supply 2': 'power_supply_2',
    'State of 802.11b Network': 'state_of_802_11b_network',
    'State of 802.11a Network': 'state_of_802_11a_network',
    'Number of WLANs': 'number_of_wlans',
    'Number of Active Clients': 'number_of_active_clients',
    'OUI Classification Failure Count': 'oui_classification_failure_count',
    'Memory Current Usage': 'memory_current_usage',
    'Memory Average Usage': 'memory_average_usage',
    'CPU Current Usage': 'cpu_current_usage',
    'CPU Average Usage': 'cpu_average_usage',
    'Flash Type': 'flash_type',
    'Flash Size': 'flash_size',
    'Maximum number of APs supported1': 'maximum_number_of_aps_supported',
    'System Nas-Id': 'system_nas_id',
    'WLC MIC Certificate Types': 'wlc_mic_certificate_types',
    'Licensing Type': 'licensing_type',
    'USB': 'licensing_type_usb',
    'Backup Controller Configuration': 'backup_controller_configuration',
    'AP primary Backup Controller': 'ap_primary_backup_controller',
    'AP secondary Backup Controller': 'ap_secondary_backup_controller',
    'Drive 0': 'raid_drive_0',
    'Drive 1': 'raid_drive_1',
}

redundancy_mode_parsing_dict = {
    'Redundancy Mode': 'redundancy_mode',
    'Local State': 'local_state',
    'Peer State': 'peer_state',
    'Unit': 'unit',
    'Unit ID': 'unit_id',
    'Redunadancy State': 'redundancy_state',  # Grammar error in some SW versions
    'Redundancy State': 'redundancy_state',
    'Mobility MAC': 'mobility_mac',
    'Redundancy Management IP Address': 'redundancy_management_ip_address',
    'Peer Redundancy Management IP Address': 'peer_redundancy_management_ip_address',
    'Redundancy Port IP Address': 'redundancy_port_ip_address',
    'Peer Redundancy Port IP Address': 'peer_redundancy_port_ip_address',
    'Peer Service Port IP Address': 'peer_service_port_ip_address',
}

dhcp_server_parsing_dict = {
    'DHCP Server IP Address:': 'ip_address',
    'DHCP RX DISCOVER Count:': 'dhcp_rx_discover_count',
    'DHCP TX DISCOVER Count:': 'dhcp_tx_discover_count',
    'DHCP ACK Count:': 'dhcp_ack_count',
    'DHCP REQUEST Count:': 'dhcp_request_count',
    'DHCP INFORM Count:': 'dhcp_inform_count',
    'DHCP DECLINE Count:': 'dhcp_decline_count',
    'DHCP RELEASE Count:': 'dhcp_release_count',
    'DHCP REPLY Count:': 'dhcp_reply_count',
    'DHCP OFFER Count:': 'dhcp_offer_count',
    'DHCP NAK Count:': 'dhcp_nak_count',
    'Tx Fails:': 'tx_fails',
    'Last Rx Time:': 'last_rx_time',
    'Last Tx Time:': 'last_tx_time',
}

nearby_aps_parsing_dict = {
    'Nearby AP': 'channel',
}

ap_config_parsing_dict = {
    'Cisco AP Identifier': 'cisco_ap_identifier',
    'Cisco AP Name': 'cisco_ap_name',
    'Country code': 'country_code',
    'Regulatory Domain allowed by Country': 'regulatory_domain_allowed_by_country',
    'AP Country code': 'ap_country_code',
    'Wireless Logging State': 'wireless_logging_state',
    'AP Regulatory Domain': 'ap_regulatory_domain',
    'Switch Port Number': 'switch_port_number',
    'MAC Address': 'mac_address',
    'IP Address Configuration': 'ip_address_configuration',
    'IP Address': 'ip_address',
    'IP NetMask': 'ip_netmask',
    'Gateway IP Addr': 'gateway_ip_addr',
    'NAT External IP Address': 'nat_external_ip_address',
    'CAPWAP Path MTU': 'capwap_path_mtu',
    'DHCP Release Override': 'dhcp_release_override',
    'Telnet State': 'telnet_state',
    'Ssh State': 'ssh_state',
    'Cisco AP Location': 'cisco_ap_location',
    'Cisco AP Floor Label': 'cisco_ap_floor_label',
    'Cisco AP Group Name': 'cisco_ap_group_name',
    'Primary Cisco Switch Name': 'primary_cisco_switch_name',
    'Primary Cisco Switch IP Address': 'primary_cisco_switch_ip_address',
    'Secondary Cisco Switch Name': 'secondary_cisco_switch_name',
    'Secondary Cisco Switch IP Address': 'secondary_cisco_switch_ip_address',
    'Tertiary Cisco Switch Name': 'tertiary_cisco_switch_name',
    'Tertiary Cisco Switch IP Address': 'tertiary_cisco_switch_ip_address',
    'Administrative State': 'administrative_state',
    'Operation State': 'operation_state',
    'Mirroring Mode': 'mirroring_mode',
    'AP Mode': 'ap_mode',
    'Public Safety': 'public_safety',
    'ATF Mode:': 'atf_mode',
    'AP SubMode': 'ap_submode',
    'Rogue Detection': 'rogue_detection',
    'Remote AP Debug': 'remote_ap_debug',
    'Logging trap severity level': 'logging_trap_severity_level',
    'Logging syslog facility': 'logging_syslog_facility',
    'S/W  Version': 's_w_version',
    'Boot  Version': 'boot_version',
    'Mini IOS Version': 'mini_ios_version',
    'Stats Reporting Period': 'stats_reporting_period',
    'Stats Collection Mode': 'stats_collection_mode',
    'Radio Core Mode': 'radio_core_mode',
    'Slub Debug Mode': 'slub_debug_mode',
    'LED State': 'led_state',
    'PoE Pre-Standard Switch': 'poe_pre_standard_switch',
    'PoE Power Injector MAC Addr': 'poe_power_injector_mac_addr',
    'Power Type/Mode': 'power_type_mode',
    'Number Of Slots': 'number_of_slots',
    'AP Model': 'ap_model',
    'AP Image': 'ap_image',
    'IOS Version': 'ios_version',
    'Reset Button': 'reset_button',
    'AP Serial Number': 'ap_serial_number',
    'AP Certificate Type': 'ap_certificate_type',
    'AP Lag Status': 'ap_lag_status',
    'AP User Mode': 'ap_user_mode',
    'AP User Name': 'ap_user_name',
    'AP Dot1x User Mode': 'ap_dot1x_user_mode',
    'AP Dot1x User Name': 'ap_dot1x_user_name',
    'Cisco AP system logging host': 'cisco_ap_system_logging_host',
    'AP Core Dump Config': 'ap_core_dump_config',
    'AP Up Time': 'ap_up_time',
    'AP LWAPP Up Time': 'ap_lwapp_up_time',
    'Join Date and Time': 'join_date_and_time',
    'Join Taken Time': 'join_taken_time',
    'Attributes for Slot  0': 'slot_0',
    'Radio Type': 'slot_0_radio_type',
    'Radio Subtype': 'slot_0_radio_subtype',
    'Assignment Method': 'slot_0_radio_role_assignment_method',
    'Band': 'slot_0_radio_role_band',
    'Current CCA Mode': 'slot_0_phy_dsss_parameters_current_cca_mode',
    'ED Threshold': 'slot_0_phy_dsss_parameters_ed_threshold',
    'Administrative State1': 'slot_0_administrative_state',
    'Operation State1': 'slot_0_operation_state',
    'Mesh Radio Role': 'slot_0_mesh_radio_role',
    'Radio Role': 'slot_0_radio_role',
    'CellId': 'slot_0_cellid',
    'Station Configuration': 'slot_0_station_configuration',
    'Configuration': 'slot_0_configuration',
    'Number Of WLANs': 'slot_0_number_of_wlans',
    'Medium Occupancy Limit': 'slot_0_medium_occupancy_limit',
    'CFP Period': 'slot_0_cfp_period',
    'CFP MaxDuration': 'slot_0_cfp_maxduration',
    'BSSID': 'slot_0_bssid',
    'Operation Rate Set': 'slot_0_operation_rate_set',
    '6000 Kilo Bits': 'slot_0_operation_rate_set_6000_kilo_bits',
    '9000 Kilo Bits': 'slot_0_operation_rate_set_9000_kilo_bits',
    '5500 Kilo Bits': 'slot_0_operation_rate_set_5500_kilo_bits',
    '1000 Kilo Bits': 'slot_0_operation_rate_set_1000_kilo_bits',
    '2000 Kilo Bits': 'slot_0_operation_rate_set_2000_kilo_bits',
    '11000 Kilo Bits': 'slot_0_operation_rate_set_11000_kilo_bits',
    '12000 Kilo Bits': 'slot_0_operation_rate_set_12000_kilo_bits',
    '18000 Kilo Bits': 'slot_0_operation_rate_set_18000_kilo_bits',
    '24000 Kilo Bits': 'slot_0_operation_rate_set_24000_kilo_bits',
    '36000 Kilo Bits': 'slot_0_operation_rate_set_36000_kilo_bits',
    '48000 Kilo Bits': 'slot_0_operation_rate_set_48000_kilo_bits',
    '54000 Kilo Bits': 'slot_0_operation_rate_set_54000_kilo_bits',
    'MCS Set': 'slot_0_mcs_set',
    'MCS 0': 'slot_0_mcs_set_mcs_0',
    'MCS 1': 'slot_0_mcs_set_mcs_1',
    'MCS 2': 'slot_0_mcs_set_mcs_2',
    'MCS 3': 'slot_0_mcs_set_mcs_3',
    'MCS 4': 'slot_0_mcs_set_mcs_4',
    'MCS 5': 'slot_0_mcs_set_mcs_5',
    'MCS 6': 'slot_0_mcs_set_mcs_6',
    'MCS 7': 'slot_0_mcs_set_mcs_7',
    'MCS 8': 'slot_0_mcs_set_mcs_8',
    'MCS 9': 'slot_0_mcs_set_mcs_9',
    'MCS 10': 'slot_0_mcs_set_mcs_10',
    'MCS 11': 'slot_0_mcs_set_mcs_11',
    'MCS 12': 'slot_0_mcs_set_mcs_12',
    'MCS 13': 'slot_0_mcs_set_mcs_13',
    'MCS 14': 'slot_0_mcs_set_mcs_14',
    'MCS 15': 'slot_0_mcs_set_mcs_15',
    'MCS 16': 'slot_0_mcs_set_mcs_16',
    'MCS 17': 'slot_0_mcs_set_mcs_17',
    'MCS 18': 'slot_0_mcs_set_mcs_18',
    'MCS 19': 'slot_0_mcs_set_mcs_19',
    'MCS 20': 'slot_0_mcs_set_mcs_20',
    'MCS 21': 'slot_0_mcs_set_mcs_21',
    'MCS 22': 'slot_0_mcs_set_mcs_22',
    'MCS 23': 'slot_0_mcs_set_mcs_23',
    'MCS 24': 'slot_0_mcs_set_mcs_24',
    'MCS 25': 'slot_0_mcs_set_mcs_25',
    'MCS 26': 'slot_0_mcs_set_mcs_26',
    'MCS 27': 'slot_0_mcs_set_mcs_27',
    'MCS 28': 'slot_0_mcs_set_mcs_28',
    'MCS 29': 'slot_0_mcs_set_mcs_29',
    'MCS 30': 'slot_0_mcs_set_mcs_30',
    'MCS 31': 'slot_0_mcs_set_mcs_31',
    '802.11ac MCS Set': 'slot_0_802_11ac_mcs_set',
    'Nss=1: MCS 0-9': 'slot_0_802_11ac_mcs_set_nss_1_mcs_0_9',
    'Nss=2: MCS 0-9': 'slot_0_802_11ac_mcs_set_nss_2_mcs_0_9',
    'Nss=3: MCS 0-9': 'slot_0_802_11ac_mcs_set_nss_3_mcs_0_9',
    'Nss=4: MCS 0-7': 'slot_0_802_11ac_mcs_set_nss_4_mcs_0_7',
    'Phy DSSS parameters': 'slot_0_phy_dsss_parameters',
    'Rogue BSSID': 'slot_0_containment_count_rogue_bssid',
    'Containment Type': 'slot_0_containment_count_rogue_bssid_containment_type',
    'Channel Count': 'slot_0_containment_count_rogue_bssid_channel_count',
    'Beacon Period': 'slot_0_beacon_period',
    'Fragmentation Threshold': 'slot_0_fragmentation_threshold',
    'Multi Domain Capability Implemented': 'slot_0_multi_domain_capability_implemented',
    'Multi Domain Capability Enabled': 'slot_0_multi_domain_capability_enabled',
    'Country String': 'slot_0_country_string',
    'Multi Domain Capability': 'slot_0_multi_domain_capability',
    'Configuration1': 'slot_0_multi_domain_capability_configuration',
    'First Chan Num': 'slot_0_multi_domain_capability_first_chan_num',
    'Number Of Channels': 'slot_0_multi_domain_capability_number_of_channels',
    'MAC Operation Parameters': 'slot_0_mac_operation_parameters',
    'Configuration2': 'slot_0_mac_operation_parameters_configuration',
    'Fragmentation Threshold1': 'slot_0_mac_operation_parameters_fragmentation_threshold',
    'Packet Retry Limit': 'slot_0_mac_operation_parameters_packet_retry_limit',
    'Tx Power': 'slot_0_tx_power',
    'Num Of Supported Power Levels': 'slot_0_tx_power_num_of_supported_power_levels',
    'Tx Power Level 1': 'slot_0_tx_power_tx_power_level_1',
    'Tx Power Level 2': 'slot_0_tx_power_tx_power_level_2',
    'Tx Power Level 3': 'slot_0_tx_power_tx_power_level_3',
    'Tx Power Level 4': 'slot_0_tx_power_tx_power_level_4',
    'Tx Power Level 5': 'slot_0_tx_power_tx_power_level_5',
    'Tx Power Level 6': 'slot_0_tx_power_tx_power_level_6',
    'Tx Power Level 7': 'slot_0_tx_power_tx_power_level_7',
    'Tx Power Level 8': 'slot_0_tx_power_tx_power_level_8',
    'Tx Power Configuration': 'slot_0_tx_power_tx_power_configuration',
    'Current Tx Power Level': 'slot_0_tx_power_current_tx_power_level',
    'Tx Power Assigned By': 'slot_0_tx_power_tx_power_assigned_by',
    'Phy OFDM parameters': 'slot_0_phy_ofdm_parameters',
    'Configuration3': 'slot_0_phy_ofdm_parameters_configuration',
    'Current Channel': 'slot_0_phy_ofdm_parameters_current_channel',
    'Channel Assigned By': 'slot_0_phy_ofdm_parameters_channel_assigned_by',
    'Extension Channel': 'slot_0_phy_ofdm_parameters_extension_channel',
    'Channel Width': 'slot_0_phy_ofdm_parameters_channel_width',
    'Allowed Channel List': 'slot_0_phy_ofdm_parameters_allowed_channel_list',
    '': 'slot_0_phy_ofdm_parameters_allowed_channel_list_',
    'TI Threshold': 'slot_0_phy_ofdm_parameters_ti_threshold',
    'DCA Channel List': 'slot_0_phy_ofdm_parameters_dca_channel_list',
    'Legacy Tx Beamforming Configuration': 'slot_0_phy_ofdm_parameters_legacy_tx_beamforming_configuration',
    'Legacy Tx Beamforming': 'slot_0_phy_ofdm_parameters_legacy_tx_beamforming',
    'Antenna Type': 'slot_0_phy_ofdm_parameters_antenna_type',
    'Internal Antenna Gain (in .5 dBi units)': 'slot_0_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units',
    'Diversity': 'slot_0_phy_ofdm_parameters_diversity',
    '802.11n Antennas': 'slot_0_phy_ofdm_parameters_802_11n_antennas',
    'A': 'slot_0_phy_ofdm_parameters_802_11n_antennas_a',
    'B': 'slot_0_phy_ofdm_parameters_802_11n_antennas_b',
    'C': 'slot_0_phy_ofdm_parameters_802_11n_antennas_c',
    'D': 'slot_0_phy_ofdm_parameters_802_11n_antennas_d',
    'Performance Profile Parameters': 'slot_0_performance_profile_parameters',
    'Configuration4': 'slot_0_performance_profile_parameters_configuration',
    'Interference threshold': 'slot_0_performance_profile_parameters_interference_threshold',
    'Noise threshold': 'slot_0_performance_profile_parameters_noise_threshold',
    'RF utilization threshold': 'slot_0_performance_profile_parameters_rf_utilization_threshold',
    'Data-rate threshold': 'slot_0_performance_profile_parameters_data_rate_threshold',
    'Client threshold': 'slot_0_performance_profile_parameters_client_threshold',
    'Coverage SNR threshold': 'slot_0_performance_profile_parameters_coverage_snr_threshold',
    'Coverage exception level': 'slot_0_performance_profile_parameters_coverage_exception_level',
    'Client minimum exception level': 'slot_0_performance_profile_parameters_client_minimum_exception_level',
    'Rogue Containment Information': 'slot_0_rogue_containment_information',
    'Containment Count': 'slot_0_containment_count',
    'CleanAir Management Information': 'slot_0_cleanair_management_information',
    'CleanAir Capable': 'slot_0_cleanair_management_information_cleanair_capable',
    'CleanAir Management Administration St': 'slot_0_cleanair_management_information_cleanair_management_administration_st',
    'CleanAir Management Operation State': 'slot_0_cleanair_management_information_cleanair_management_operation_state',
    'Rapid Update Mode': 'slot_0_cleanair_management_information_rapid_update_mode',
    'Spectrum Expert connection': 'slot_0_cleanair_management_information_spectrum_expert_connection',
    'CleanAir NSI Key': 'slot_0_cleanair_management_information_spectrum_expert_connection_cleanair_nsi_key',
    'Spectrum Expert Connections counter': 'slot_0_cleanair_management_information_spectrum_expert_connection_spectrum_expert_connections_counter',
    'CleanAir Sensor State': 'slot_0_cleanair_management_information_cleanair_sensor_state',
    'Radio Extended Configurations': 'slot_0_radio_extended_configurations',
    'Beacon period': 'slot_0_radio_extended_configurations_beacon_period',
    'Beacon range': 'slot_0_radio_extended_configurations_beacon_range',
    'Multicast buffer': 'slot_0_radio_extended_configurations_multicast_buffer',
    'Multicast data-rate': 'slot_0_radio_extended_configurations_multicast_data_rate',
    'RX SOP threshold': 'slot_0_radio_extended_configurations_rx_sop_threshold',
    'CCA threshold': 'slot_0_radio_extended_configurations_cca_threshold',
    'Attributes for Slot  1': 'slot_1',
    'Radio Type1': 'slot_1_radio_type',
    'Radio Subband': 'slot_1_radio_subband',
    'Administrative State2': 'slot_1_administrative_state',
    'Operation State2': 'slot_1_operation_state',
    'Mesh Radio Role1': 'slot_1_mesh_radio_role',
    'Radio Role1': 'slot_1_radio_role',
    'CellId1': 'slot_1_cellid',
    'Station Configuration1': 'slot_1_station_configuration',
    'Configuration5': 'slot_1_configuration',
    'Number Of WLANs1': 'slot_1_number_of_wlans',
    'Medium Occupancy Limit1': 'slot_1_medium_occupancy_limit',
    'CFP Period1': 'slot_1_cfp_period',
    'CFP MaxDuration1': 'slot_1_cfp_maxduration',
    'BSSID1': 'slot_1_bssid',
    'Operation Rate Set1': 'slot_1_operation_rate_set',
    '6000 Kilo Bits1': 'slot_1_operation_rate_set_6000_kilo_bits',
    '9000 Kilo Bits1': 'slot_1_operation_rate_set_9000_kilo_bits',
    '12000 Kilo Bits1': 'slot_1_operation_rate_set_12000_kilo_bits',
    '18000 Kilo Bits1': 'slot_1_operation_rate_set_18000_kilo_bits',
    '24000 Kilo Bits1': 'slot_1_operation_rate_set_24000_kilo_bits',
    '36000 Kilo Bits1': 'slot_1_operation_rate_set_36000_kilo_bits',
    '48000 Kilo Bits1': 'slot_1_operation_rate_set_48000_kilo_bits',
    '54000 Kilo Bits1': 'slot_1_operation_rate_set_54000_kilo_bits',
    'MCS Set1': 'slot_1_mcs_set',
    'MCS 01': 'slot_1_mcs_set_mcs_0',
    'MCS 32': 'slot_1_mcs_set_mcs_3',
    'MCS 41': 'slot_1_mcs_set_mcs_4',
    'MCS 51': 'slot_1_mcs_set_mcs_5',
    'MCS 61': 'slot_1_mcs_set_mcs_6',
    'MCS 71': 'slot_1_mcs_set_mcs_7',
    'MCS 81': 'slot_1_mcs_set_mcs_8',
    'MCS 91': 'slot_1_mcs_set_mcs_9',
    'MCS 101': 'slot_1_mcs_set_mcs_10',
    'MCS 111': 'slot_1_mcs_set_mcs_11',
    'MCS 121': 'slot_1_mcs_set_mcs_12',
    'MCS 131': 'slot_1_mcs_set_mcs_13',
    'MCS 141': 'slot_1_mcs_set_mcs_14',
    'MCS 151': 'slot_1_mcs_set_mcs_15',
    'MCS 161': 'slot_1_mcs_set_mcs_16',
    'MCS 171': 'slot_1_mcs_set_mcs_17',
    'MCS 181': 'slot_1_mcs_set_mcs_18',
    'MCS 191': 'slot_1_mcs_set_mcs_19',
    'MCS 201': 'slot_1_mcs_set_mcs_20',
    'MCS 211': 'slot_1_mcs_set_mcs_21',
    'MCS 221': 'slot_1_mcs_set_mcs_22',
    'MCS 231': 'slot_1_mcs_set_mcs_23',
    'MCS 241': 'slot_1_mcs_set_mcs_24',
    'MCS 251': 'slot_1_mcs_set_mcs_25',
    'MCS 261': 'slot_1_mcs_set_mcs_26',
    'MCS 271': 'slot_1_mcs_set_mcs_27',
    'MCS 281': 'slot_1_mcs_set_mcs_28',
    'MCS 291': 'slot_1_mcs_set_mcs_29',
    'MCS 301': 'slot_1_mcs_set_mcs_30',
    'MCS 311': 'slot_1_mcs_set_mcs_31',
    '802.11ac MCS Set1': 'slot_1_802_11ac_mcs_set',
    'Nss=1: MCS 0-91': 'slot_1_802_11ac_mcs_set_nss_1_mcs_0_9',
    'Nss=2: MCS 0-91': 'slot_1_802_11ac_mcs_set_nss_2_mcs_0_9',
    'Nss=3: MCS 0-91': 'slot_1_802_11ac_mcs_set_nss_3_mcs_0_9',
    'Nss=4: MCS 0-71': 'slot_1_802_11ac_mcs_set_nss_4_mcs_0_7',
    'Nss=4: MCS 0-91': 'slot_1_802_11ac_mcs_set_nss_4_mcs_0_9',
    'Beacon Period1': 'slot_1_beacon_period',
    'Fragmentation Threshold2': 'slot_1_fragmentation_threshold',
    'Multi Domain Capability Implemented1': 'slot_1_multi_domain_capability_implemented',
    'Multi Domain Capability Enabled1': 'slot_1_multi_domain_capability_enabled',
    'Country String1': 'slot_1_country_string',
    'Multi Domain Capability1': 'slot_1_multi_domain_capability',
    'Configuration6': 'slot_1_multi_domain_capability_configuration',
    'First Chan Num1': 'slot_1_multi_domain_capability_first_chan_num',
    'Number Of Channels1': 'slot_1_multi_domain_capability_number_of_channels',
    'MAC Operation Parameters1': 'slot_1_mac_operation_parameters',
    'Configuration7': 'slot_1_mac_operation_parameters_configuration',
    'Fragmentation Threshold3': 'slot_1_mac_operation_parameters_fragmentation_threshold',
    'Packet Retry Limit1': 'slot_1_mac_operation_parameters_packet_retry_limit',
    'Tx Power1': 'slot_1_tx_power',
    'Num Of Supported Power Levels1': 'slot_1_tx_power_num_of_supported_power_levels',
    'Tx Power Level 11': 'slot_1_tx_power_tx_power_level_1',
    'Tx Power Level 21': 'slot_1_tx_power_tx_power_level_2',
    'Tx Power Level 31': 'slot_1_tx_power_tx_power_level_3',
    'Tx Power Level 41': 'slot_1_tx_power_tx_power_level_4',
    'Tx Power Level 51': 'slot_1_tx_power_tx_power_level_5',
    'Tx Power Level 61': 'slot_1_tx_power_tx_power_level_6',
    'Tx Power Level 71': 'slot_1_tx_power_tx_power_level_7',
    'Tx Power Level 81': 'slot_1_tx_power_tx_power_level_8',
    'Tx Power Configuration1': 'slot_1_tx_power_tx_power_configuration',
    'Current Tx Power Level1': 'slot_1_tx_power_current_tx_power_level',
    'Tx Power Assigned By1': 'slot_1_tx_power_tx_power_assigned_by',
    'Phy OFDM parameters1': 'slot_1_phy_ofdm_parameters',
    'Configuration8': 'slot_1_phy_ofdm_parameters_configuration',
    'Current Channel1': 'slot_1_phy_ofdm_parameters_current_channel',
    'Channel Assigned By1': 'slot_1_phy_ofdm_parameters_channel_assigned_by',
    'Extension Channel1': 'slot_1_phy_ofdm_parameters_extension_channel',
    'Channel Width1': 'slot_1_phy_ofdm_parameters_channel_width',
    'Allowed Channel List1': 'slot_1_phy_ofdm_parameters_allowed_channel_list',
    '1': 'slot_1_phy_ofdm_parameters_allowed_channel_list_',
    'TI Threshold1': 'slot_1_phy_ofdm_parameters_ti_threshold',
    'DCA Channel List1': 'slot_1_phy_ofdm_parameters_dca_channel_list',
    'Legacy Tx Beamforming Configuration1': 'slot_1_phy_ofdm_parameters_legacy_tx_beamforming_configuration',
    'Legacy Tx Beamforming1': 'slot_1_phy_ofdm_parameters_legacy_tx_beamforming',
    'Antenna Type1': 'slot_1_phy_ofdm_parameters_antenna_type',
    'Internal Antenna Gain (in .5 dBi units)1': 'slot_1_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units',
    'Diversity1': 'slot_1_phy_ofdm_parameters_diversity',
    '802.11n Antennas1': 'slot_1_phy_ofdm_parameters_802_11n_antennas',
    'A1': 'slot_1_phy_ofdm_parameters_802_11n_antennas_a',
    'B1': 'slot_1_phy_ofdm_parameters_802_11n_antennas_b',
    'C1': 'slot_1_phy_ofdm_parameters_802_11n_antennas_c',
    'D1': 'slot_1_phy_ofdm_parameters_802_11n_antennas_d',
    'Performance Profile Parameters1': 'slot_1_performance_profile_parameters',
    'Interference threshold1': 'slot_1_performance_profile_parameters_interference_threshold',
    'Noise threshold1': 'slot_1_performance_profile_parameters_noise_threshold',
    'RF utilization threshold1': 'slot_1_performance_profile_parameters_rf_utilization_threshold',
    'Data-rate threshold1': 'slot_1_performance_profile_parameters_data_rate_threshold',
    'Client threshold1': 'slot_1_performance_profile_parameters_client_threshold',
    'Coverage SNR threshold1': 'slot_1_performance_profile_parameters_coverage_snr_threshold',
    'Coverage exception level1': 'slot_1_performance_profile_parameters_coverage_exception_level',
    'Client minimum exception level1': 'slot_1_performance_profile_parameters_client_minimum_exception_level',
    'Rogue Containment Information1': 'slot_1_rogue_containment_information',
    'Containment Count1': 'slot_1_containment_count',
    'CleanAir Management Information1': 'slot_1_cleanair_management_information',
    'CleanAir Capable1': 'slot_1_cleanair_management_information_cleanair_capable',
    'CleanAir Management Administration St1': 'slot_1_cleanair_management_information_cleanair_management_administration_st',
    'CleanAir Management Operation State1': 'slot_1_cleanair_management_information_cleanair_management_operation_state',
    'Rapid Update Mode1': 'slot_1_cleanair_management_information_rapid_update_mode',
    'Spectrum Expert connection1': 'slot_1_cleanair_management_information_spectrum_expert_connection',
    'CleanAir NSI Key1': 'slot_1_cleanair_management_information_spectrum_expert_connection_cleanair_nsi_key',
    'Spectrum Expert Connections counter1': 'slot_1_cleanair_management_information_spectrum_expert_connection_spectrum_expert_connections_counter',
    'CleanAir Sensor State1': 'slot_1_cleanair_management_information_cleanair_sensor_state',
    'Radio Extended Configurations1': 'slot_1_radio_extended_configurations',
    'Beacon period1': 'slot_1_radio_extended_configurations_beacon_period',
    'Beacon range1': 'slot_1_radio_extended_configurations_beacon_range',
    'Multicast buffer1': 'slot_1_radio_extended_configurations_multicast_buffer',
    'Multicast data-rate1': 'slot_1_radio_extended_configurations_multicast_data_rate',
    'RX SOP threshold1': 'slot_1_radio_extended_configurations_rx_sop_threshold',
    'CCA threshold1': 'slot_1_radio_extended_configurations_cca_threshold',
}

ap_rf_parsing_dict = {
    'AP Name': 'ap_name',
    'MAC Address': 'mac_address',
    'Slot ID': 'slot_id',
    'Radio Type': 'radio_type',
    'Sub-band Type': 'sub_band_type',
    'Noise Profile': 'noise_profile',
    'Channel 1': 'noise_profile_channel_1',
    'Channel 2': 'noise_profile_channel_2',
    'Channel 3': 'noise_profile_channel_3',
    'Channel 4': 'noise_profile_channel_4',
    'Channel 5': 'noise_profile_channel_5',
    'Channel 6': 'noise_profile_channel_6',
    'Channel 7': 'noise_profile_channel_7',
    'Channel 8': 'noise_profile_channel_8',
    'Channel 9': 'noise_profile_channel_9',
    'Channel 10': 'noise_profile_channel_10',
    'Channel 11': 'noise_profile_channel_11',
    'Channel 12': 'noise_profile_channel_12',
    'Channel 13': 'noise_profile_channel_13',
    'Channel 14': 'noise_profile_channel_14',
    'Channel 34': 'noise_profile_channel_34',
    'Channel 36': 'noise_profile_channel_36',
    'Channel 38': 'noise_profile_channel_38',
    'Channel 40': 'noise_profile_channel_40',
    'Channel 42': 'noise_profile_channel_42',
    'Channel 44': 'noise_profile_channel_44',
    'Channel 46': 'noise_profile_channel_46',
    'Channel 48': 'noise_profile_channel_48',
    'Channel 52': 'noise_profile_channel_52',
    'Channel 56': 'noise_profile_channel_56',
    'Channel 60': 'noise_profile_channel_60',
    'Channel 64': 'noise_profile_channel_64',
    'Channel 100': 'noise_profile_channel_100',
    'Channel 104': 'noise_profile_channel_104',
    'Channel 108': 'noise_profile_channel_108',
    'Channel 112': 'noise_profile_channel_112',
    'Channel 116': 'noise_profile_channel_116',
    'Channel 120': 'noise_profile_channel_120',
    'Channel 124': 'noise_profile_channel_124',
    'Channel 128': 'noise_profile_channel_128',
    'Channel 132': 'noise_profile_channel_132',
    'Channel 136': 'noise_profile_channel_136',
    'Channel 140': 'noise_profile_channel_140',
    'Channel 144': 'noise_profile_channel_144',
    'Channel 149': 'noise_profile_channel_149',
    'Channel 153': 'noise_profile_channel_153',
    'Channel 157': 'noise_profile_channel_157',
    'Channel 161': 'noise_profile_channel_161',
    'Channel 165': 'noise_profile_channel_165',
    'Channel 169': 'noise_profile_channel_169',
    'Channel 173': 'noise_profile_channel_173',
    'Interference Profile': 'interference_profile',
    'Channel 15': 'interference_profile_channel_1',
    'Channel 21': 'interference_profile_channel_2',
    'Channel 31': 'interference_profile_channel_3',
    'Channel 41': 'interference_profile_channel_4',
    'Channel 51': 'interference_profile_channel_5',
    'Channel 61': 'interference_profile_channel_6',
    'Channel 71': 'interference_profile_channel_7',
    'Channel 81': 'interference_profile_channel_8',
    'Channel 91': 'interference_profile_channel_9',
    'Channel 101': 'interference_profile_channel_10',
    'Channel 111': 'interference_profile_channel_11',
    'Channel 121': 'interference_profile_channel_12',
    'Channel 131': 'interference_profile_channel_13',
    'Channel 141': 'interference_profile_channel_14',
    'Channel 341': 'interference_profile_channel_34',
    'Channel 361': 'interference_profile_channel_36',
    'Channel 381': 'interference_profile_channel_38',
    'Channel 401': 'interference_profile_channel_40',
    'Channel 421': 'interference_profile_channel_42',
    'Channel 441': 'interference_profile_channel_44',
    'Channel 461': 'interference_profile_channel_46',
    'Channel 481': 'interference_profile_channel_48',
    'Channel 521': 'interference_profile_channel_52',
    'Channel 561': 'interference_profile_channel_56',
    'Channel 601': 'interference_profile_channel_60',
    'Channel 641': 'interference_profile_channel_64',
    'Channel 1001': 'interference_profile_channel_100',
    'Channel 1041': 'interference_profile_channel_104',
    'Channel 1081': 'interference_profile_channel_108',
    'Channel 1121': 'interference_profile_channel_112',
    'Channel 1161': 'interference_profile_channel_116',
    'Channel 1201': 'interference_profile_channel_120',
    'Channel 1241': 'interference_profile_channel_124',
    'Channel 1281': 'interference_profile_channel_128',
    'Channel 1321': 'interference_profile_channel_132',
    'Channel 1361': 'interference_profile_channel_136',
    'Channel 1401': 'interference_profile_channel_140',
    'Channel 1441': 'interference_profile_channel_144',
    'Channel 1491': 'interference_profile_channel_149',
    'Channel 1531': 'interference_profile_channel_153',
    'Channel 1571': 'interference_profile_channel_157',
    'Channel 1611': 'interference_profile_channel_161',
    'Channel 1651': 'interference_profile_channel_165',
    'Channel 1691': 'interference_profile_channel_169',
    'Channel 1731': 'interference_profile_channel_173',
    'Rogue Histogram': 'rogue_histogram',
    'Channel 16': 'rogue_histogram_channel_1',
    'Channel 22': 'rogue_histogram_channel_2',
    'Channel 32': 'rogue_histogram_channel_3',
    'Channel 43': 'rogue_histogram_channel_4',
    'Channel 53': 'rogue_histogram_channel_5',
    'Channel 62': 'rogue_histogram_channel_6',
    'Channel 72': 'rogue_histogram_channel_7',
    'Channel 82': 'rogue_histogram_channel_8',
    'Channel 92': 'rogue_histogram_channel_9',
    'Channel 102': 'rogue_histogram_channel_10',
    'Channel 113': 'rogue_histogram_channel_11',
    'Channel 122': 'rogue_histogram_channel_12',
    'Channel 133': 'rogue_histogram_channel_13',
    'Channel 142': 'rogue_histogram_channel_14',
    'Channel 342': 'rogue_histogram_channel_34',
    'Channel 362': 'rogue_histogram_channel_36',
    'Channel 382': 'rogue_histogram_channel_38',
    'Channel 402': 'rogue_histogram_channel_40',
    'Channel 422': 'rogue_histogram_channel_42',
    'Channel 442': 'rogue_histogram_channel_44',
    'Channel 462': 'rogue_histogram_channel_46',
    'Channel 482': 'rogue_histogram_channel_48',
    'Channel 522': 'rogue_histogram_channel_52',
    'Channel 562': 'rogue_histogram_channel_56',
    'Channel 602': 'rogue_histogram_channel_60',
    'Channel 642': 'rogue_histogram_channel_64',
    'Channel 1002': 'rogue_histogram_channel_100',
    'Channel 1042': 'rogue_histogram_channel_104',
    'Channel 1082': 'rogue_histogram_channel_108',
    'Channel 1122': 'rogue_histogram_channel_112',
    'Channel 1162': 'rogue_histogram_channel_116',
    'Channel 1202': 'rogue_histogram_channel_120',
    'Channel 1242': 'rogue_histogram_channel_124',
    'Channel 1282': 'rogue_histogram_channel_128',
    'Channel 1322': 'rogue_histogram_channel_132',
    'Channel 1362': 'rogue_histogram_channel_136',
    'Channel 1402': 'rogue_histogram_channel_140',
    'Channel 1442': 'rogue_histogram_channel_144',
    'Channel 1492': 'rogue_histogram_channel_149',
    'Channel 1532': 'rogue_histogram_channel_153',
    'Channel 1572': 'rogue_histogram_channel_157',
    'Channel 1612': 'rogue_histogram_channel_161',
    'Channel 1652': 'rogue_histogram_channel_165',
    'Channel 1692': 'rogue_histogram_channel_169',
    'Channel 1732': 'rogue_histogram_channel_173',
    'Load Profile': 'load_profile',
    'Receive Utilization': 'load_profile_receive_utilization',
    'Transmit Utilization': 'load_profile_transmit_utilization',
    'Channel Utilization': 'load_profile_channel_utilization',
    'Attached Clients': 'load_profile_attached_clients',
    'Coverage Profile': 'coverage_profile',
    'Failed Clients': 'failed_clients',
    'Client Signal Strengths': 'client_signal_strengths',
    'RSSI -100 dbm': 'client_signal_strengths_rssi_100_dbm',
    'RSSI  -92 dbm': 'client_signal_strengths_rssi_92_dbm',
    'RSSI  -84 dbm': 'client_signal_strengths_rssi_84_dbm',
    'RSSI  -76 dbm': 'client_signal_strengths_rssi_76_dbm',
    'RSSI  -68 dbm': 'client_signal_strengths_rssi_68_dbm',
    'RSSI  -60 dbm': 'client_signal_strengths_rssi_60_dbm',
    'RSSI  -52 dbm': 'client_signal_strengths_rssi_52_dbm',
    'Client Signal To Noise Ratios': 'client_signal_to_noise_ratios',
    'SNR    0 dB': 'client_signal_to_noise_ratios_snr_0_db',
    'SNR    5 dB': 'client_signal_to_noise_ratios_snr_5_db',
    'SNR   10 dB': 'client_signal_to_noise_ratios_snr_10_db',
    'SNR   15 dB': 'client_signal_to_noise_ratios_snr_15_db',
    'SNR   20 dB': 'client_signal_to_noise_ratios_snr_20_db',
    'SNR   25 dB': 'client_signal_to_noise_ratios_snr_25_db',
    'SNR   30 dB': 'client_signal_to_noise_ratios_snr_30_db',
    'SNR   35 dB': 'client_signal_to_noise_ratios_snr_35_db',
    'SNR   40 dB': 'client_signal_to_noise_ratios_snr_40_db',
    'SNR   45 dB': 'client_signal_to_noise_ratios_snr_45_db',
    'Radar Information': 'radar_information',
    'Channel Assignment Information': 'channel_assignment_information',
    'Current Channel Average Energy': 'channel_assignment_information_current_channel_average_energy',
    'Previous Channel Average Energy': 'channel_assignment_information_previous_channel_average_energy',
    'Channel Change Count': 'channel_assignment_information_channel_change_count',
    'Last Channel Change Time': 'channel_assignment_information_last_channel_change_time',
    'Recommended Best Channel': 'channel_assignment_information_recommended_best_channel',
    'RF Parameter Recommendations': 'rf_parameter_recommendations',
    'Power Level': 'rf_parameter_recommendations_power_level',
    'RTS/CTS Threshold': 'rf_parameter_recommendations_rts_cts_threshold',
    'Fragmentation Threshold': 'rf_parameter_recommendations_fragmentation_threshold',
    'Antenna Pattern': 'rf_parameter_recommendations_antenna_pattern',
}

network_config_parsing_dict = {
    'RF-Network Name': 'rf_network_name',
    'DNS Server IP': 'dns_server_ip',
    'Web Mode': 'web_mode',
    'Secure Web Mode': 'secure_web_mode',
    'Secure Web Mode Cipher-Option High': 'secure_web_mode_cipher_option_high',
    'Secure Web Mode SSL Protocol': 'secure_web_mode_ssl_protocol',
    'Web CSRF check': 'web_csrf_check',
    'OCSP': 'ocsp',
    'OCSP responder URL': 'ocsp_responder_url',
    'Secure Shell (ssh)': 'secure_shell_ssh',
    'Secure Shell (ssh) Cipher-Option High': 'secure_shell_ssh_cipher_option_high',
    'Telnet': 'telnet',
    'Ethernet Multicast Forwarding': 'ethernet_multicast_forwarding',
    'Ethernet Broadcast Forwarding': 'ethernet_broadcast_forwarding',
    'IPv4 AP Multicast/Broadcast Mode': 'ipv4_ap_multicast_broadcast_mode',
    'IPv6 AP Multicast/Broadcast Mode': 'ipv6_ap_multicast_broadcast_mode',
    'IGMP snooping': 'igmp_snooping',
    'IGMP timeout': 'igmp_timeout',
    'IGMP Query Interval': 'igmp_query_interval',
    'MLD snooping': 'mld_snooping',
    'MLD timeout': 'mld_timeout',
    'MLD query interval': 'mld_query_interval',
    'User Idle Timeout': 'user_idle_timeout',
    'ARP Idle Timeout': 'arp_idle_timeout',
    'Cisco AP Default Master': 'cisco_ap_default_master',
    'AP Join Priority': 'ap_join_priority',
    'Mgmt Via Wireless Interface': 'mgmt_via_wireless_interface',
    'Mgmt Via Dynamic Interface': 'mgmt_via_dynamic_interface',
    'Bridge MAC filter Config': 'bridge_mac_filter_config',
    'Bridge Security Mode': 'bridge_security_mode',
    'Mesh Full Sector DFS': 'mesh_full_sector_dfs',
    'Mesh Backhaul RRM': 'mesh_backhaul_rrm',
    'AP Fallback': 'ap_fallback',
    'Web Auth CMCC Support': 'web_auth_cmcc_support',
    'Web Auth Redirect Ports': 'web_auth_redirect_ports',
    'Web Auth Proxy Redirect': 'web_auth_proxy_redirect_',
    'Web Auth Captive-Bypass': 'web_auth_captive_bypass__',
    'Web Auth Secure Web': 'web_auth_secure_web_',
    'Web Auth Secure Web Cipher Option': 'web_auth_secure_web_cipher_option_',
    'Web Auth Secure Web Sslv3': 'web_auth_secure_web_sslv3_',
    'Web Auth Secure Redirection': 'web_auth_secure_redirection_',
    'Fast SSID Change': 'fast_ssid_change',
    'AP Discovery - NAT IP Only': 'ap_discovery_nat_ip_only',
    'IP/MAC Addr Binding Check': 'ip_mac_addr_binding_check',
    'Link Local Bridging Status': 'link_local_bridging_status',
    'CCX-lite status': 'ccx_lite_status',
    'oeap-600 dual-rlan-ports': 'oeap_600_dual_rlan_ports',
    'oeap local-network': 'oeap_local_network',
    'oeap-600 Split Tunneling (Printers)': 'oeap_600_split_tunneling_printers',
    'WebPortal Online Client': 'webportal_online_client',
    'WebPortal NTF_LOGOUT Client': 'webportal_ntf_logout_client',
    'mDNS snooping': 'mdns_snooping',
    'mDNS Query Interval': 'mdns_query_interval',
    'Web Color Theme': 'web_color_theme',
    'Capwap Prefer Mode': 'capwap_prefer_mode',
    'Network Profile': 'network_profile',
    'Client ip conflict detection (DHCP)': 'client_ip_conflict_detection_dhcp',
    'Mesh BH RRM': 'mesh_bh_rrm',
    'Mesh Aggressive DCA': 'mesh_aggressive_dca',
    'Mesh Auto RF': 'mesh_auto_rf',
    'HTTP Profiling Port': 'http_profiling_port',
    'HTTP-Proxy Ip Address': 'http_proxy_ip_address',
    'HTTP-Proxy Port': 'http_proxy_port',
    'WGB Client Forced L2 Roam': 'wgb_client_forced_l2_roam',
}

ssid_config_parsing_dict = {
    'WLAN Identifier': 'wlan_identifier',
    'Profile Name': 'profile_name',
    'Network Name (SSID)': 'network_name_ssid',
    'Status': 'status',
    'MAC Filtering': 'mac_filtering',
    'Broadcast SSID': 'broadcast_ssid',
    'AAA Policy Override': 'aaa_policy_override',
    'Network Admission Control': 'network_admission_control',
    'Client Profiling Status': 'client_profiling_status',
    'Radius Profiling': 'client_profiling_status_radius_profiling',
    'DHCP': 'client_profiling_status_radius_profiling_dhcp',
    'HTTP': 'client_profiling_status_radius_profiling_http',
    'Local Profiling': 'client_profiling_status_local_profiling',
    'DHCP1': 'client_profiling_status_local_profiling_dhcp',
    'HTTP1': 'client_profiling_status_local_profiling_http',
    'Radius-NAC State': 'radius_nac_state',
    'SNMP-NAC State': 'snmp_nac_state',
    'Quarantine VLAN': 'quarantine_vlan',
    'Maximum Clients Allowed': 'maximum_clients_allowed',
    'Security Group Tag': 'security_group_tag',
    'Maximum number of Clients per AP Radio': 'maximum_number_of_clients_per_ap_radio',
    'ATF Policy': 'atf_policy',
    'Number of Active Clients': 'number_of_active_clients',
    'Exclusionlist': 'exclusionlist',
    'Exclusionlist Timeout': 'exclusionlist_timeout',
    'Session Timeout': 'session_timeout',
    'User Idle Timeout': 'user_idle_timeout',
    'Sleep Client': 'sleep_client',
    'Sleep Client Timeout': 'sleep_client_timeout',
    'Web Auth Captive Bypass Mode': 'web_auth_captive_bypass_mode',
    'User Idle Threshold': 'user_idle_threshold',
    'NAS-identifier': 'nas_identifier',
    'CHD per WLAN': 'chd_per_wlan',
    'Webauth DHCP exclusion': 'webauth_dhcp_exclusion',
    'Interface': 'interface',
    'Multicast Interface': 'multicast_interface',
    'WLAN IPv4 ACL': 'wlan_ipv4_acl',
    'WLAN IPv6 ACL': 'wlan_ipv6_acl',
    'WLAN Layer2 ACL': 'wlan_layer2_acl',
    'WLAN URL ACL': 'wlan_url_acl',
    'mDNS Status': 'mdns_status',
    'mDNS Profile Name': 'mdns_profile_name',
    'DHCP Server': 'dhcp_server',
    'Central NAT Peer-Peer Blocking': 'central_nat_peer_peer_blocking',
    'DHCP Address Assignment Required': 'dhcp_address_assignment_required',
    'Static IP client tunneling': 'static_ip_client_tunneling',
    'Tunnel Profile': 'tunnel_profile',
    'PMIPv6 Mobility Type': 'pmipv6_mobility_type',
    'PMIPv6 MAG Profile': 'pmipv6_mobility_type_pmipv6_mag_profile',
    'PMIPv6 Default Realm': 'pmipv6_mobility_type_pmipv6_default_realm',
    'PMIPv6 NAI Type': 'pmipv6_mobility_type_pmipv6_nai_type',
    'PMIPv6 MAG location': 'pmipv6_mobility_type_pmipv6_mag_location',
    'Quality of Service': 'quality_of_service',
    'Per-SSID Rate Limits': 'per_ssid_rate_limits',
    'Average Data Rate': 'average_data_rate',
    'Average Realtime Data Rate': 'average_realtime_data_rate',
    'Burst Data Rate': 'burst_data_rate',
    'Burst Realtime Data Rate': 'burst_realtime_data_rate',
    'Per-Client Rate Limits': 'per_client_rate_limits',
    'Average Data Rate1': 'average_data_rate',
    'Average Realtime Data Rate1': 'average_realtime_data_rate',
    'Burst Data Rate1': 'burst_data_rate',
    'Burst Realtime Data Rate1': 'burst_realtime_data_rate',
    'Scan Defer Priority': 'scan_defer_priority',
    'Scan Defer Time': 'scan_defer_time',
    'WMM': 'wmm',
    'WMM UAPSD Compliant Client Support': 'wmm_uapsd_compliant_client_support',
    'Media Stream Multicast-direct': 'media_stream_multicast_direct',
    'CCX - AironetIe Support': 'ccx_aironetie_support',
    'CCX - Gratuitous ProbeResponse (GPR)': 'ccx_gratuitous_proberesponse_gpr',
    'CCX - Diagnostics Channel Capability': 'ccx_diagnostics_channel_capability',
    'Dot11-Phone Mode (7920)': 'dot11_phone_mode_7920',
    'Wired Protocol': 'wired_protocol',
    'Passive Client Feature': 'passive_client_feature',
    'Peer-to-Peer Blocking Action': 'peer_to_peer_blocking_action',
    'Radio Policy': 'radio_policy',
    'DTIM period for 802.11a radio': 'dtim_period_for_802_11a_radio',
    'DTIM period for 802.11b radio': 'dtim_period_for_802_11b_radio',
    'Radius Servers': 'radius_servers',
    'Authentication': 'radius_servers_authentication',
    'Accounting': 'radius_servers_accounting',
    'Interim Update': 'radius_servers_accounting_interim_update',
    'Interim Update Interval': 'radius_servers_accounting_interim_update_interval',
    'Framed IPv6 Acct AVP': 'radius_servers_accounting_framed_ipv6_acct_avp',
    'Dynamic Interface': 'radius_servers_dynamic_interface',
    'Dynamic Interface Priority': 'radius_servers_dynamic_interface_priority',
    'Local EAP Authentication': 'local_eap_authentication',
    'Radius NAI-Realm': 'radius_nai_realm',
    'Mu-Mimo': 'mu_mimo',
    'Security': 'security',
    '802.11 Authentication:': 'security_802_11_authentication',
    'FT Support': 'security_ft_support',
    'Static WEP Keys': 'security_static_wep_keys',
    '802.1X': 'security_802_1x',
    'Wi-Fi Protected Access (WPA/WPA2)': 'security_wi_fi_protected_access_wpa_wpa2',
    'WPA (SSN IE)': 'security_wi_fi_protected_access_wpa_wpa2_wpa_ssn_ie',
    'WPA2 (RSN IE)': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie',
    'TKIP Cipher': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_tkip_cipher',
    'AES Cipher': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_aes_cipher',
    'CCMP256 Cipher': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_ccmp256_cipher',
    'GCMP128 Cipher': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_gcmp128_cipher',
    'GCMP256 Cipher': 'security_wi_fi_protected_access_wpa_wpa2_wpa2_rsn_ie_gcmp256_cipher',
    'OSEN IE': 'security_wi_fi_protected_access_wpa_wpa2_osen_ie',
    'Auth Key Management': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management',
    '802.1x': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_802_1x',
    'PSK': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_psk',
    'CCKM': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_cckm',
    'FT-1X(802.11r)': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_ft_1x802_11r',
    'FT-PSK(802.11r)': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_ft_psk802_11r',
    'PMF-1X(802.11w)': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_pmf_1x802_11w',
    'PMF-PSK(802.11w)': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_pmf_psk802_11w',
    'OSEN-1X': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_osen_1x',
    'SUITEB-1X': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_suiteb_1x',
    'SUITEB192-1X': 'security_wi_fi_protected_access_wpa_wpa2_auth_key_management_suiteb192_1x',
    'FT Reassociation Timeout': 'security_wi_fi_protected_access_wpa_wpa2_ft_reassociation_timeout',
    'FT Over-The-DS mode': 'security_wi_fi_protected_access_wpa_wpa2_ft_over_the_ds_mode',
    'GTK Randomization': 'security_wi_fi_protected_access_wpa_wpa2_gtk_randomization',
    'SKC Cache Support': 'security_wi_fi_protected_access_wpa_wpa2_skc_cache_support',
    'CCKM TSF Tolerance': 'security_wi_fi_protected_access_wpa_wpa2_cckm_tsf_tolerance',
    'Wi-Fi Direct policy configured': 'security_wi_fi_direct_policy_configured',
    'EAP-Passthrough': 'security_eap_passthrough',
    'CKIP': 'security_ckip',
    'Web Based Authentication': 'security_web_based_authentication',
    'Web Authentication Timeout': 'security_web_authentication_timeout',
    'Web-Passthrough': 'security_web_passthrough',
    'Mac-auth-server': 'security_mac_auth_server',
    'Web-portal-server': 'security_web_portal_server',
    'qrscan-des-key': 'security_qrscan_des_key',
    'Conditional Web Redirect': 'security_conditional_web_redirect',
    'Splash-Page Web Redirect': 'security_splash_page_web_redirect',
    'Auto Anchor': 'security_auto_anchor',
    'FlexConnect Local Switching': 'security_flexconnect_local_switching',
    'FlexConnect Central Association': 'security_flexconnect_central_association',
    'flexconnect Central Dhcp Flag': 'security_flexconnect_central_dhcp_flag',
    'flexconnect nat-pat Flag': 'security_flexconnect_nat_pat_flag',
    'flexconnect Dns Override Flag': 'security_flexconnect_dns_override_flag',
    'flexconnect PPPoE pass-through': 'security_flexconnect_pppoe_pass_through',
    'flexconnect local-switching IP-source-guar': 'security_flexconnect_local_switching_ip_source_guar',
    'FlexConnect Vlan based Central Switching': 'security_flexconnect_vlan_based_central_switching',
    'FlexConnect Local Authentication': 'security_flexconnect_local_authentication',
    'FlexConnect Learn IP Address': 'security_flexconnect_learn_ip_address',
    'Client MFP': 'security_client_mfp',
    'PMF': 'security_pmf',
    'PMF Association Comeback Time': 'security_pmf_association_comeback_time',
    'PMF SA Query RetryTimeout': 'security_pmf_sa_query_retrytimeout',
    'Tkip MIC Countermeasure Hold-down Timer': 'security_tkip_mic_countermeasure_hold_down_timer',
    'Eap-params': 'security_eap_params',
    'AVC Visibilty': 'avc_visibility',
    'AVC Profile Name': 'avc_profile_name',
    'Flex Avc Profile Name': 'flex_avc_profile_name',
    'OpenDns Profile Name': 'opendns_profile_name',
    'OpenDns Wlan Mode': 'opendns_wlan_mode',
    'Flow Monitor Name': 'flow_monitor_name',
    'Split Tunnel Configuration': 'split_tunnel_configuration',
    'Split Tunnel': 'split_tunnel_configuration_split_tunnel',
    'Call Snooping': 'call_snooping',
    'Roamed Call Re-Anchor Policy': 'roamed_call_re_anchor_policy',
    'SIP CAC Fail Send-486-Busy Policy': 'sip_cac_fail_send_486_busy_policy',
    'SIP CAC Fail Send Dis-Association Policy': 'sip_cac_fail_send_dis_association_policy',
    'KTS based CAC Policy': 'kts_based_cac_policy',
    'Assisted Roaming Prediction Optimization': 'assisted_roaming_prediction_optimization',
    '802.11k Neighbor List': 'd_802_11k_neighbor_list',
    '802.11k Neighbor List Dual Band': 'd_802_11k_neighbor_list_dual_band',
    '802.11v Directed Multicast Service': 'd_802_11v_directed_multicast_service',
    '802.11v BSS Max Idle Service': 'd_802_11v_bss_max_idle_service',
    '802.11v BSS Transition Service': 'd_802_11v_bss_transition_service',
    '802.11v BSS Transition Disassoc Imminent': 'd_802_11v_bss_transition_disassoc_imminent',
    '802.11v BSS Transition Disassoc Timer': 'd_802_11v_bss_transition_disassoc_timer',
    '802.11v BSS Transition OpRoam Disassoc Timer': 'd_802_11v_bss_transition_oproam_disassoc_timer',
    'DMS DB is empty': 'dms_db_is_empty',
    'Band Select': 'band_select',
    'Load Balancing': 'load_balancing',
    'Multicast Buffer': 'multicast_buffer',
    'Universal Ap Admin': 'universal_ap_admin',
    'Broadcast Tagging': 'broadcast_tagging',
    'PRP': 'prp',
    'Mobility Anchor List': 'mobility_anchor_list',
    '802.11u': 'd_802_11u',
    'MSAP Services': 'msap_services',
    'Local Policy': 'local_policy',
    'Priority  Policy Name': 'priority__policy_name',
    'Lync State': 'lync_state',
    'Audio QoS Policy': 'audio_qos_policy',
    'Video QoS Policy': 'video_qos_policy',
    'App-Share QoS Policy': 'app_share_qos_policy',
    'File Transfer QoS Policy': 'file_transfer_qos_policy',
    'QoS Fastlane Status': 'qos_fastlane_status',
    'Selective Reanchoring Status': 'selective_reanchoring_status',
    'Lobby Admin Access': 'lobby_admin_access',
    'Fabric status': 'fabric_status',
    'Vnid Name': 'vnid_name',
    'Vnid': 'vnid',
    'Applied SGT Tag': 'applied_sgt_tag',
    'Peer Ip Address': 'peer_ip_address',
    'Flex Acl Name': 'flex_acl_name',
    'Flex Avc Policy Name': 'flex_avc_policy_name',
    'U3-Interface': 'u3_interface',
    'U3-Reporting Interval': 'u3_reporting_interval'
}

interface_config_parsing_dict = {
    'Interface Configuration': 'interface_configuration',
    'Interface Name': 'interface_name',
    'MAC Address': 'mac_address',
    'IP Address': 'ip_address',
    'IP Netmask': 'ip_netmask',
    'IP Gateway': 'ip_gateway',
    'External NAT IP State': 'external_nat_ip_state',
    'External NAT IP Address': 'external_nat_ip_address',
    'Link Local IPv6 Address': 'link_local_ipv6_address',
    'STATE': 'state_link_local_ipv6',
    'Primary IPv6 Address': 'ipv6_address',
    'STATE1': 'state_ipv6',
    'Primary IPv6 Gateway': 'ipv6_gateway',
    'Primary IPv6 Gateway Mac Address': 'ipv6_gateway_mac_address',
    'IPv6 Address': 'ipv6_address',
    'IPv6 Gateway': 'ipv6_gateway',
    'IPv6 Gateway Mac Address': 'ipv6_gateway_mac_address',
    'STATE2': 'state_ipv6_gateway',
    'NAS-Identifier': 'nas_identifier',
    'VLAN': 'vlan',
    'Quarantine-vlan': 'quarantine_vlan',
    'Active Physical Port': 'active_physical_port',
    'Primary Physical Port': 'primary_physical_port',
    'Backup Physical Port': 'backup_physical_port',
    'DHCP Proxy Mode': 'dhcp_proxy_mode',
    'Primary DHCP Server': 'primary_dhcp_server',
    'Secondary DHCP Server': 'secondary_dhcp_server',
    'DHCP Option 82': 'dhcp_option_82',
    'DHCP Option 82 bridge mode insertion': 'dhcp_option_82_bridge_mode_insertion',
    'IPv4 ACL': 'ipv4_acl',
    'URL ACL': 'url_acl',
    'IPv6 ACL': 'ipv6_acl',
    'URL ACL1': 'url_acl1',
    'mDNS Profile Name': 'mdns_profile_name',
    'AP Manager': 'ap_manager',
    'Guest Interface': 'guest_interface',
    '3G VLAN': 'd_3g_vlan',
    'L2 Multicast': 'l2_multicast',
    'SLAAC': 'slaac',
    'DHCP Protocol': 'dhcp_protocol',
    'Speed': 'speed',
    'Duplex': 'duplex',
    'Auto Negotiation': 'auto_negotiation',
    'Link Status': 'link_status',
    'Virtual DNS Host Name': 'virtual_dns_host_name',
    'Remote ID format': 'remote_id_format',
    'Link Select Suboption': 'link_select_suboption',
    'Relay Src Intf': 'relay_src_intf',
    'VPN Select Suboption': 'vpn_select_suboption',
}

interface_group_parsing_dict = {
    'Interface Group Name': 'interface_group_name',
    'Quarantine': 'quarantine',
    'Number of Wlans using the Interface Group': 'number_of_wlans_using_the_interface_group',
    'Number of AP Groups using the Interface Group': 'number_of_ap_groups_using_the_interface_group',
    'Number of Interfaces Contained': 'number_of_interfaces_contained',
    'mDNS Profile Name': 'mdns_profile_name',
    'Failure-Detect Mode': 'failure_detect_mode',
    'Interface Group Description': 'interface_group_description',
}

switch_config_parsing_dict = {
    '802.3x Flow Control Mode': 'd_802_3x_flow_control_mode',
    'FIPS prerequisite features': 'fips_prerequisite_features',
    'WLANCC prerequisite features': 'wlancc_prerequisite_features',
    'UCAPL prerequisite features': 'ucapl_prerequisite_features',
    'Last login information display': 'last_login_information_display',
    'DTLS WLC MIC': 'dtls_wlc_mic',
    'secret obfuscation': 'secret_obfuscation',
    'Strong Password Check Features': 'strong_password_check_features',
    'case-check': 'strong_password_check_features_case_check',
    'consecutive-check': 'strong_password_check_features_consecutive_check',
    'default-check': 'strong_password_check_features_default_check',
    'username-check': 'strong_password_check_features_username_check',
    'position-check': 'strong_password_check_features_position_check',
    'case-digit-check': 'strong_password_check_features_case_digit_check',
    'Min. Password length': 'strong_password_check_features_min__password_length',
    'Min. Upper case chars': 'strong_password_check_features_min__upper_case_chars',
    'Min. Lower case chars': 'strong_password_check_features_min__lower_case_chars',
    'Min. Digits chars': 'strong_password_check_features_min__digits_chars',
    'Min. Special chars': 'strong_password_check_features_min__special_chars',
    'Mgmt User': 'mgmt_user',
    'Password Lifetime [days]': 'mgmt_user_password_lifetime_days',
    'Password Lockout': 'mgmt_user_password_lockout',
    'Lockout Attempts': 'mgmt_user_lockout_attempts',
    'Lockout Timeout [mins]': 'mgmt_user_lockout_timeout_mins',
    'SNMPv3 User': 'snmpv3_user',
    'Password Lifetime [days]1': 'snmpv3_user_password_lifetime_days',
    'Password Lockout1': 'snmpv3_user_password_lockout',
    'Lockout Attempts1': 'snmpv3_user_lockout_attempts',
    'Lockout Timeout [mins]1': 'snmpv3_user_lockout_timeout_mins',
}

mobility_config_parsing_dict = {
    'Mobility Protocol Port': 'mobility_protocol_port',
    'Default Mobility Domain': 'default_mobility_domain',
    'Multicast Mode': 'multicast_mode',
    'Mobility Domain ID for 802.11r': 'mobility_domain_id_for_802_11r',
    'Mobility Keepalive Interval': 'mobility_keepalive_interval',
    'Mobility Keepalive Count': 'mobility_keepalive_count',
    'Mobility Group Members Configured': 'mobility_group_members_configured',
    'Mobility Control Message DSCP Value': 'mobility_control_message_dscp_value',
}

rf_profile_parsing_dict = {
    'RF Profile name': 'rf_profile_name',
    'Description': 'description',
    'AP Group Name': 'ap_group_name',
    'Radio policy': 'radio_policy',
    '11n-client-only': 'd_11n_client_only',
    'Transmit Power Threshold v1': 'transmit_power_threshold_v1',
    'Transmit Power Threshold v2': 'transmit_power_threshold_v2',
    'Min Transmit Power': 'min_transmit_power',
    'Max Transmit Power': 'max_transmit_power',
    '802.11b/g Operational Rates': 'd_802_11b_g_operational_rates',
    '802.11b/g 1M Rate': 'd_802_11b_g_operational_rates_802_11b_g_1m_rate',
    '802.11b/g 2M Rate': 'd_802_11b_g_operational_rates_802_11b_g_2m_rate',
    '802.11b/g 5.5M Rate': 'd_802_11b_g_operational_rates_802_11b_g_5_5m_rate',
    '802.11b/g 11M Rate': 'd_802_11b_g_operational_rates_802_11b_g_11m_rate',
    '802.11g 6M Rate': 'd_802_11b_g_operational_rates_802_11g_6m_rate',
    '802.11g 9M Rate': 'd_802_11b_g_operational_rates_802_11g_9m_rate',
    '802.11g 12M Rate': 'd_802_11b_g_operational_rates_802_11g_12m_rate',
    '802.11g 18M Rate': 'd_802_11b_g_operational_rates_802_11g_18m_rate',
    '802.11g 24M Rate': 'd_802_11b_g_operational_rates_802_11g_24m_rate',
    '802.11g 36M Rate': 'd_802_11b_g_operational_rates_802_11g_36m_rate',
    '802.11g 48M Rate': 'd_802_11b_g_operational_rates_802_11g_48m_rate',
    '802.11g 54M Rate': 'd_802_11b_g_operational_rates_802_11g_54m_rate',
    '802.11a Operational Rates': 'd_802_11a_operational_rates',
    '802.11a 6M Rate': 'd_802_11a_operational_rates_802_11a_6m_rate',
    '802.11a 9M Rate': 'd_802_11a_operational_rates_802_11a_9m_rate',
    '802.11a 12M Rate': 'd_802_11a_operational_rates_802_11a_12m_rate',
    '802.11a 18M Rate': 'd_802_11a_operational_rates_802_11a_18m_rate',
    '802.11a 24M Rate': 'd_802_11a_operational_rates_802_11a_24m_rate',
    '802.11a 36M Rate': 'd_802_11a_operational_rates_802_11a_36m_rate',
    '802.11a 48M Rate': 'd_802_11a_operational_rates_802_11a_48m_rate',
    '802.11a 54M Rate': 'd_802_11a_operational_rates_802_11a_54m_rate',
    'Trap Threshold': 'trap_threshold',
    'Clients': 'trap_threshold_clients',
    'Interference': 'trap_threshold_interference',
    'Noise': 'trap_threshold_noise',
    'Utilization': 'trap_threshold_utilization',
    'Multicast Data Rate': 'multicast_data_rate',
    'Rx Sop Threshold': 'rx_sop_threshold',
    'Cca Threshold': 'cca_threshold',
    'Slot Admin State:': 'slot_admin_state',
    'Client Aware FRA': 'client_aware_fra',
    'State': 'client_aware_fra_state',
    'Client Select Utilization Threshold': 'client_aware_fra_client_select_utilization_threshold',
    'Client Reset Utilization Threshold': 'client_aware_fra_client_reset_utilization_threshold',
    'Band Select': 'band_select',
    'Probe Response': 'band_select_probe_response',
    'Cycle Count': 'band_select_cycle_count',
    'Cycle Threshold': 'band_select_cycle_threshold',
    'Expire Suppression': 'band_select_expire_suppression',
    'Expire Dual Band': 'band_select_expire_dual_band',
    'Client Rssi': 'band_select_client_rssi',
    'Client Mid Rssi': 'band_select_client_mid_rssi',
    'Load Balancing': 'load_balancing',
    'Denial': 'load_balancing_denial',
    'Window': 'load_balancing_window',
    'Coverage Data': 'coverage_data',
    'Data': 'coverage_data_data',
    'Voice': 'coverage_data_voice',
    'Minimum Client Level': 'coverage_data_minimum_client_level',
    'Exception Level': 'coverage_data_exception_level',
    'DCA Channel List': 'dca_channel_list',
    'DCA Bandwidth': 'dca_bandwidth',
    'DCA Foreign AP Contribution': 'dca_foreign_ap_contribution',
    '802.11n MCS Rates': 'd_802_11n_mcs_rates',
    'MCS-00 Rate': 'd_802_11n_mcs_rates_mcs_00_rate',
    'MCS-01 Rate': 'd_802_11n_mcs_rates_mcs_01_rate',
    'MCS-02 Rate': 'd_802_11n_mcs_rates_mcs_02_rate',
    'MCS-03 Rate': 'd_802_11n_mcs_rates_mcs_03_rate',
    'MCS-04 Rate': 'd_802_11n_mcs_rates_mcs_04_rate',
    'MCS-05 Rate': 'd_802_11n_mcs_rates_mcs_05_rate',
    'MCS-06 Rate': 'd_802_11n_mcs_rates_mcs_06_rate',
    'MCS-07 Rate': 'd_802_11n_mcs_rates_mcs_07_rate',
    'MCS-08 Rate': 'd_802_11n_mcs_rates_mcs_08_rate',
    'MCS-09 Rate': 'd_802_11n_mcs_rates_mcs_09_rate',
    'MCS-10 Rate': 'd_802_11n_mcs_rates_mcs_10_rate',
    'MCS-11 Rate': 'd_802_11n_mcs_rates_mcs_11_rate',
    'MCS-12 Rate': 'd_802_11n_mcs_rates_mcs_12_rate',
    'MCS-13 Rate': 'd_802_11n_mcs_rates_mcs_13_rate',
    'MCS-14 Rate': 'd_802_11n_mcs_rates_mcs_14_rate',
    'MCS-15 Rate': 'd_802_11n_mcs_rates_mcs_15_rate',
    'MCS-16 Rate': 'd_802_11n_mcs_rates_mcs_16_rate',
    'MCS-17 Rate': 'd_802_11n_mcs_rates_mcs_17_rate',
    'MCS-18 Rate': 'd_802_11n_mcs_rates_mcs_18_rate',
    'MCS-19 Rate': 'd_802_11n_mcs_rates_mcs_19_rate',
    'MCS-20 Rate': 'd_802_11n_mcs_rates_mcs_20_rate',
    'MCS-21 Rate': 'd_802_11n_mcs_rates_mcs_21_rate',
    'MCS-22 Rate': 'd_802_11n_mcs_rates_mcs_22_rate',
    'MCS-23 Rate': 'd_802_11n_mcs_rates_mcs_23_rate',
    'MCS-24 Rate': 'd_802_11n_mcs_rates_mcs_24_rate',
    'MCS-25 Rate': 'd_802_11n_mcs_rates_mcs_25_rate',
    'MCS-26 Rate': 'd_802_11n_mcs_rates_mcs_26_rate',
    'MCS-27 Rate': 'd_802_11n_mcs_rates_mcs_27_rate',
    'MCS-28 Rate': 'd_802_11n_mcs_rates_mcs_28_rate',
    'MCS-29 Rate': 'd_802_11n_mcs_rates_mcs_29_rate',
    'MCS-30 Rate': 'd_802_11n_mcs_rates_mcs_30_rate',
    'MCS-31 Rate': 'd_802_11n_mcs_rates_mcs_31_rate',
    'Client Network Preference': 'client_network_preference'
}

main_parsing_dict_aireos = {
    'WLAN Configuration': ssid_config_parsing_dict,  # Config section start word from list
    'Probe request filtering..': advanced_config_parsing_dict,
    'WLC IPv6 Summary': ipv6_config_parsing_dict,
    'RADIUS Configuration': radius_config_parsing_dict,
    'Mobility Configuration': mobility_config_parsing_dict,
    'Total Number of AP Groups': ap_group_parsing_dict,
    '802.11b CleanAir Configuration': cleanair_24g_parsing_dict,
    '802.11a CleanAir Configuration': cleanair_5g_parsing_dict,
    'Interface Configuration': interface_config_parsing_dict,
    'Interface Group Configuration': interface_group_parsing_dict,
    'Network Information': network_config_parsing_dict,
    'Switch Configuration': switch_config_parsing_dict,
    'AP Airewave Director Configuration': ap_rf_parsing_dict,
    'AP Config': ap_config_parsing_dict,
    'DHCP Info': dhcp_server_parsing_dict,
    'Redundancy Information': redundancy_mode_parsing_dict,
    'System Information': system_info_parsing_dict,
    '802.11a Configuration': band_5_parsing_dict,
    '802.11b Configuration': band_24_parsing_dict,
    'Number of RF Profiles': rf_profile_parsing_dict,
    'Airewave Director Configuration': nearby_aps_parsing_dict,  # Special case for Nearby APs info
}

# TESTING functions section
def parsing_dict_checker(dict, class_instance):
    logging.debug('Checking parsing dictionary for object type: ' + str(type(class_instance)))
    # To test parsing dictionary with the class instance
    for key in dict.keys():
        try:
            getattr(class_instance, dict[key])
        except:
            if not 'unique_' in str(key) and not 'end_table_string' in dict[key]: #skip unique_keys and table parsing dicts - needed for dict identification and table parsing
                logging.debug('ERROR: '+ str(type(class_instance)) + ' ' + str(key) +  ' ' + str(dict[key]))

def test_parsing_dicts_aireos():
    parsing_dict_checker(ssid_config_parsing_dict, Ssid_Config())
    parsing_dict_checker(ipv6_config_parsing_dict, Ipv6_Config())
    parsing_dict_checker(advanced_config_parsing_dict, Advanced_Config())
    parsing_dict_checker(radius_config_parsing_dict, Radius_Config())
    parsing_dict_checker(rf_profile_parsing_dict, Rf_Profile())
    parsing_dict_checker(interface_config_parsing_dict, Dynamic_Interface())
    parsing_dict_checker(switch_config_parsing_dict, Switch_Config())
    parsing_dict_checker(network_config_parsing_dict, Network_Config())
    parsing_dict_checker(mobility_config_parsing_dict, Mobility_Config())
    parsing_dict_checker(ap_config_parsing_dict, Ap_Config())
    parsing_dict_checker(dhcp_server_parsing_dict, Dhcp_Server())
    parsing_dict_checker(redundancy_mode_parsing_dict, Redundancy_Config())
    parsing_dict_checker(system_info_parsing_dict, System_Config())
    parsing_dict_checker(band_5_parsing_dict, Band5_Config())
    parsing_dict_checker(band_24_parsing_dict, Band24_Config())
    parsing_dict_checker(cleanair_24g_parsing_dict, Cleanair_24G_Config())
    parsing_dict_checker(cleanair_5g_parsing_dict, Cleanair_5G_Config())
    logging.debug('Checked AireOS parsing dictionaries test results for correct parsing')