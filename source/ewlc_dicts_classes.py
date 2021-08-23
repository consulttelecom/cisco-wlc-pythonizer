import logging
from aireos_dicts_classes import grep, show, NamedList, Nearby_Ap

class Ewlc_Client_Stats():
    def __init__(self, name=None):
        self.objname = 'Clients statistics'
        self.name = 'Clients statistics'
        self.type = 'operational'  # defines if class contain operational or config data
        self.total_number_of_clients = None
        self.protocol_client_count_802_11b = None
        self.protocol_client_count_802_11g = None
        self.protocol_client_count_802_11a = None
        self.protocol_client_count_802_11n_2_4ghz = None
        self.protocol_client_count_802_11n_5_ghz = None
        self.protocol_client_count_802_11ac = None
        self.protocol_client_count_802_11ax_5_ghz = None
        self.protocol_client_count_802_11ax_2_4_ghz = None
        self.current_client_state_statistics_authenticating = None
        self.current_client_state_statistics_mobility = None
        self.current_client_state_statistics_ip_learn = None
        self.current_client_state_statistics_webauth_pending = None
        self.current_client_state_statistics_run = None
        self.current_client_state_statistics_delete_in_progress = None
        self.client_summary = None
        self.current_clients = None
        self.excluded_clients = None
        self.disabled_clients = None
        self.foreign_clients = None
        self.anchor_clients = None
        self.local_clients = None
        self.total_association_requests_received = None
        self.total_association_attempts = None
        self.total_ft_localauth_requests = None
        self.total_association_failures = None
        self.total_association_response_accepts = None
        self.total_association_response_rejects = None
        self.total_association_response_errors = None
        self.total_association_failures_due_to_blacklist = None
        self.total_association_drops_due_to_multicast_mac = None
        self.total_association_drops_due_to_throttling = None
        self.total_association_drops_due_to_unknown_bssid = None
        self.total_association_drops_due_to_parse_failure = None
        self.total_association_drops_due_to_other_reasons = None
        self.total_association_requests_wired_clients = None
        self.total_association_drops_wired_clients = None
        self.total_association_success_wired_clients = None
        self.total_peer_association_requests_wired_clients = None
        self.total_peer_association_drops_wired_clients = None
        self.total_peer_association_success_wired_clients = None
        self.total_11r_ft_authentication_requests_received = None
        self.total_11r_ft_authentication_response_success = None
        self.total_11r_ft_authentication_response_failure = None
        self.total_11r_ft_action_requests_received = None
        self.total_11r_ft_action_response_success = None
        self.total_11r_ft_action_response_failure = None
        self.total_aid_allocation_failures = None
        self.total_aid_free_failures = None
        self.total_roam_attempts = None
        self.total_roam_attempts_total_cckm_roam_attempts = None
        self.total_roam_attempts_total_11r_roam_attempts = None
        self.total_roam_attempts_total_11i_fast_roam_attempts = None
        self.total_roam_attempts_total_11i_slow_roam_attempts = None
        self.total_roam_attempts_total_other_roam_type_attempts = None
        self.total_roam_failures_in_dot11 = None
        self.total_wpa3_sae_attempts = None
        self.total_wpa3_sae_successful_authentications = None
        self.total_wpa3_sae_authentication_failures = None
        self.total_wpa3_sae_authentication_failures_total_incomplete_protocol_failures = None
        self.total_wpa3_sae_commit_messages_received = None
        self.total_wpa3_sae_commit_messages_rejected = None
        self.total_wpa3_sae_commit_messages_rejected_total_unsupported_group_rejections = None
        self.total_wpa3_sae_commit_messages_sent = None
        self.total_wpa3_sae_confirm_messages_received = None
        self.total_wpa3_sae_confirm_messages_rejected = None
        self.total_wpa3_sae_confirm_messages_rejected_total_wpa3_sae_message_confirm_field_mismatch = None
        self.total_wpa3_sae_confirm_messages_rejected_total_wpa3_sae_confirm_message_invalid_length = None
        self.total_wpa3_sae_confirm_messages_sent = None
        self.total_wpa3_sae_open_sessions = None
        self.total_sae_message_drops_due_to_throttling = None
        self.total_flexconnect_local_auth_roam_attempts = None
        self.total_flexconnect_local_auth_roam_attempts_total_ap_11i_fast_roam_attempts = None
        self.total_flexconnect_local_auth_roam_attempts_total_11i_slow_roam_attempts = None
        self.total_client_state_starts = None
        self.total_client_state_associated = None
        self.total_client_state_l2auth_success = None
        self.total_client_state_l2auth_failures = None
        self.total_blacklisted_clients_on_dot1xauth_failure = None
        self.total_client_state_mab_attempts = None
        self.total_client_state_mab_failed = None
        self.total_client_state_ip_learn_attempts = None
        self.total_client_state_ip_learn_failed = None
        self.total_client_state_l3_auth_attempts = None
        self.total_client_state_l3_auth_failed = None
        self.total_client_state_session_push_attempts = None
        self.total_client_state_session_push_failed = None
        self.total_client_state_run = None
        self.total_client_deleted = None
        self.total_add_mobiles_sent = None
        self.total_delete_mobiles_sent = None
        self.total_client_deferred_delete_mobiles = None
        self.total_client_deferred_delete_mobiles_sent = None
        self.total_client_deferred_delete_mobile_timeouts = None
        self.total_key_exchange_attempts = None
        self.total_broadcast_key_exchange_attempts = None
        self.total_broadcast_key_exchange_failures = None
        self.total_eapol_key_sent = None
        self.total_eapol_key_received = None
        self.total_m1_sent = None
        self.total_m3_sent = None
        self.total_m5_sent = None
        self.total_m2_received = None
        self.total_m4_received = None
        self.total_m6_received = None
        self.total_m1_resent = None
        self.total_m3_resent = None
        self.total_m5_resent = None
        self.total_data_path_client_create = None
        self.total_data_path_client_create_success = None
        self.total_data_path_client_create_failed = None
        self.total_data_path_deplumb_client_create = None
        self.total_data_path_deplumb_client_create_success = None
        self.total_data_path_deplumb_client_create_fail = None
        self.total_data_path_client_update = None
        self.total_data_path_client_update_success = None
        self.total_data_path_client_update_failed = None
        self.total_data_path_client_delete = None
        self.total_data_path_client_delete_success = None
        self.total_data_path_client_delete_failed = None
        self.total_data_path_client_nack = None
        self.total_data_path_client_delete_nack = None
        self.total_data_path_client_unknown_nack = None
        self.total_dms_requests_received_in_action_frame = None
        self.total_dms_responses_sent_in_action_frame = None
        self.total_dms_requests_received_in_re_assoc_request = None
        self.client_state_statistics_associated_state = None
        self.client_state_statistics_l2_state = None
        self.client_state_statistics_mobility_state = None
        self.client_state_statistics_ip_learn_state = None
        self.client_state_statistics_l3_auth_state = None
        self.average_run_state_latency_ms = None
        self.average_run_state_latency_without_user_delay_ms = None
        self.latency_distribution_ms = None
        self.latency_distribution_ms_1_100 = None
        self.latency_distribution_ms_100_200 = None
        self.latency_distribution_ms_200_300 = None
        self.latency_distribution_ms_300_600 = None
        self.latency_distribution_ms_600_1000 = None
        self.latency_distribution_ms_1000_plus = None
        self.webauth_http_statistics = None
        self.webauth_http_statistics_intercepted_http_requests = None
        self.webauth_http_statistics_io_read_events = None
        self.webauth_http_statistics_received_http_messages = None
        self.webauth_http_statistics_io_write_events = None
        self.webauth_http_statistics_sent_http_replies = None
        self.webauth_http_statistics_io_aaa_messages = None
        self.webauth_http_statistics_ssl_ok = None
        self.webauth_http_statistics_ssl_read_would_block = None
        self.webauth_http_statistics_ssl_write_would_block = None
        self.webauth_http_statistics_socket_opens = None
        self.webauth_http_statistics_socket_closes = None
        self.webauth_http_status_counts = None
        self.webauth_http_status_counts_http_200_ok = None
        self.webauth_http_status_counts_http_201_created = None
        self.webauth_http_status_counts_http_202_accepted = None
        self.webauth_http_status_counts_http_203_provisional_info = None
        self.webauth_http_status_counts_http_204_no_content = None
        self.webauth_http_status_counts_http_300_multiple_choices = None
        self.webauth_http_status_counts_http_301_moved_permanently = None
        self.webauth_http_status_counts_http_302_moved_temporarily = None
        self.webauth_http_status_counts_http_303_method = None
        self.webauth_http_status_counts_http_304_not_modified = None
        self.webauth_http_status_counts_http_400_bad_request = None
        self.webauth_http_status_counts_http_401_unauthorized = None
        self.webauth_http_status_counts_http_402_payment_required = None
        self.webauth_http_status_counts_http_403_forbidden = None
        self.webauth_http_status_counts_http_404_not_found = None
        self.webauth_http_status_counts_http_405_method_not_allowed = None
        self.webauth_http_status_counts_http_406_none_acceptable = None
        self.webauth_http_status_counts_http_407_proxy_auth_required = None
        self.webauth_http_status_counts_http_408_request_timeout = None
        self.webauth_http_status_counts_http_409_conflict = None
        self.webauth_http_status_counts_http_410_gone = None
        self.webauth_http_status_counts_http_500_internal_server_error = None
        self.webauth_http_status_counts_http_501_not_implemeneted = None
        self.webauth_http_status_counts_http_502_bad_gateway = None
        self.webauth_http_status_counts_http_503_service_unavailable = None
        self.webauth_http_status_counts_http_504_gateway_timeout = None
        self.webauth_queue_counters = None
        self.webauth_queue_counters_pending_ssl_handshakes = None
        self.webauth_queue_counters_pending_https_new_requests = None
        self.webauth_queue_counters_pending_aaa_replies = None
        self.delete_reasons = None
        self.delete_reasons_no_operation = None
        self.delete_reasons_unknown = None
        self.delete_reasons_deauthentication_or_disassociation_request = None
        self.delete_reasons_session_manager = None
        self.delete_reasons_l3_authentication_failure = None
        self.delete_reasons_delete_received_from_ap = None
        self.delete_reasons_bssid_down = None
        self.delete_reasons_ap_down_disjoin = None
        self.delete_reasons_connection_timeout = None
        self.delete_reasons_mac_authentication_failure = None
        self.delete_reasons_datapath_plumb = None
        self.delete_reasons_due_to_ssid_change = None
        self.delete_reasons_due_to_vlan_change = None
        self.delete_reasons_admin_deauthentication = None
        self.delete_reasons_qos_failure = None
        self.delete_reasons_wpa_key_exchange_timeout = None
        self.delete_reasons_wpa_group_key_update_timeout = None
        self.delete_reasons_802_11w_max_sa_queries_reached = None
        self.delete_reasons_client_deleted_during_ha_recovery = None
        self.delete_reasons_client_blacklist = None
        self.delete_reasons_inter_instance_roam_failure = None
        self.delete_reasons_due_to_mobility_failure = None
        self.delete_reasons_session_timeout = None
        self.delete_reasons_idle_timeout = None
        self.delete_reasons_wired_idle_timeout = None
        self.delete_reasons_supplicant_request = None
        self.delete_reasons_nas_error = None
        self.delete_reasons_policy_manager_internal_error = None
        self.delete_reasons_mobility_wlan_down = None
        self.delete_reasons_mobility_tunnel_down = None
        self.delete_reasons_80211v_smart_roam_failed = None
        self.delete_reasons_dot11v_timer_timeout = None
        self.delete_reasons_dot11v_association_failed = None
        self.delete_reasons_dot11r_pre_authentication_failure = None
        self.delete_reasons_sae_authentication_failure = None
        self.delete_reasons_sae_commit_received_in_associated_state = None
        self.delete_reasons_dot11_failure = None
        self.delete_reasons_dot11_sae_invalid_message = None
        self.delete_reasons_dot11_unsupported_client_capabilities = None
        self.delete_reasons_dot11_association_denied_unspecified = None
        self.delete_reasons_dot11_max_sta = None
        self.delete_reasons_dot11_denied_data_rates = None
        self.delete_reasons_802_11v_client_rssi_lower_than_the_association_rssi_threshold = None
        self.delete_reasons_invalid_qos_parameter = None
        self.delete_reasons_dot11_ie_validation_failed = None
        self.delete_reasons_dot11_group_cipher_in_ie_validation_failed = None
        self.delete_reasons_dot11_invalid_pairwise_cipher = None
        self.delete_reasons_dot11_invalid_akm = None
        self.delete_reasons_dot11_unsupported_rsn_version = None
        self.delete_reasons_dot11_invalid_rsnie_capabilities = None
        self.delete_reasons_dot11_received_invalid_pmkid_in_the_received_rsn_ie = None
        self.delete_reasons_dot11_invalid_mdie = None
        self.delete_reasons_dot11_invalid_ft_ie = None
        self.delete_reasons_dot11_qos_policy = None
        self.delete_reasons_dot11_ap_have_insufficient_bandwidth = None
        self.delete_reasons_dot11_invalid_qos_parameter = None
        self.delete_reasons_client_not_allowed_by_assisted_roaming = None
        self.delete_reasons_iapp_disassociation_for_wired_client = None
        self.delete_reasons_wired_wgb_change = None
        self.delete_reasons_wired_vlan_change = None
        self.delete_reasons_wired_client_deleted_due_to_wgb_delete = None
        self.delete_reasons_avc_client_re_anchored_at_the_foreign_controller = None
        self.delete_reasons_wgb_wired_client_joins_as_a_direct_wireless_client = None
        self.delete_reasons_ap_upgrade = None
        self.delete_reasons_client_dhcp = None
        self.delete_reasons_client_eap_timeout = None
        self.delete_reasons_client_8021x_failure = None
        self.delete_reasons_client_device_idle = None
        self.delete_reasons_client_captive_portal_security_failure = None
        self.delete_reasons_client_decryption_failure = None
        self.delete_reasons_client_interface_disabled = None
        self.delete_reasons_client_user_triggered_disassociation = None
        self.delete_reasons_client_miscellaneous_reason = None
        self.delete_reasons_unknown = None
        self.delete_reasons_client_peer_triggered = None
        self.delete_reasons_client_beacon_loss = None
        self.delete_reasons_client_eap_id_timeout = None
        self.delete_reasons_client_dot1x_timeout = None
        self.delete_reasons_malformed_eap_key_frame = None
        self.delete_reasons_eap_key_install_bit_is_not_expected = None
        self.delete_reasons_eap_key_error_bit_is_not_expected = None
        self.delete_reasons_eap_key_ack_bit_is_not_expected = None
        self.delete_reasons_invalid_key_type = None
        self.delete_reasons_eap_key_secure_bit_is_not_expected = None
        self.delete_reasons_key_description_version_mismatch = None
        self.delete_reasons_wrong_replay_counter = None
        self.delete_reasons_eap_key_mic_bit_expected = None
        self.delete_reasons_mic_validation_failed = None
        self.delete_reasons_error_while_ptk_computation = None
        self.delete_reasons_incorrect_credentials = None
        self.delete_reasons_client_connection_lost = None
        self.delete_reasons_reauthentication_failure = None
        self.delete_reasons_port_admin_disabled = None
        self.delete_reasons_supplicant_restart = None
        self.delete_reasons_no_ip = None
        self.delete_reasons_call_admission_controller_at_anchor_node = None
        self.delete_reasons_anchor_no_memory = None
        self.delete_reasons_anchor_invalid_mobility_bssid = None
        self.delete_reasons_anchor_creation_failure = None
        self.delete_reasons_db_error = None
        self.delete_reasons_wired_client_cleanup_due_to_wgb_roaming = None
        self.delete_reasons_manually_excluded = None
        self.delete_reasons_802_11_association_failure = None
        self.delete_reasons_802_11_authentication_failure = None
        self.delete_reasons_802_1x_authentication_timeout = None
        self.delete_reasons_802_1x_authentication_credential_failure = None
        self.delete_reasons_web_authentication_failure = None
        self.delete_reasons_policy_bind_failure = None
        self.delete_reasons_ip_theft = None
        self.delete_reasons_mac_theft = None
        self.delete_reasons_mac_and_ip_theft = None
        self.delete_reasons_qos_policy_failure = None
        self.delete_reasons_qos_policy_send_to_ap_failure = None
        self.delete_reasons_qos_policy_bind_on_ap_failure = None
        self.delete_reasons_qos_policy_unbind_on_ap_failure = None
        self.delete_reasons_static_ip_anchor_discovery_failure = None
        self.delete_reasons_vlan_failure = None
        self.delete_reasons_acl_failure = None
        self.delete_reasons_redirect_acl_failure = None
        self.delete_reasons_accounting_failure = None
        self.delete_reasons_security_group_tag_failure = None
        self.delete_reasons_fqdn_filter_definition_does_not_exist = None
        self.delete_reasons_wrong_filter_type_expected_postauth_fqdn_filter = None
        self.delete_reasons_wrong_filter_type_expected_preauth_fqdn_filter = None
        self.delete_reasons_invalid_group_id_for_fqdn_filter_valid_range_1_16 = None
        self.delete_reasons_policy_parameter_mismatch = None
        self.delete_reasons_reauth_failure = None
        self.delete_reasons_wrong_psk = None
        self.delete_reasons_policy_failure = None
        self.delete_reasons_ap_initiated_delete_for_idle_timeout = None
        self.delete_reasons_ap_initiated_delete_for_client_acl_mismatch = None
        self.delete_reasons_ap_initiated_delete_for_ap_auth_stop = None
        self.delete_reasons_ap_initiated_delete_for_association_expired_at_ap = None
        self.delete_reasons_ap_initiated_delete_for_4_way_handshake_failed = None
        self.delete_reasons_ap_initiated_delete_for_dhcp_timeout = None
        self.delete_reasons_ap_initiated_delete_for_reassociation_timeout = None
        self.delete_reasons_ap_initiated_delete_for_sa_query_timeout = None
        self.delete_reasons_ap_initiated_delete_for_intra_ap_roam = None
        self.delete_reasons_ap_initiated_delete_for_channel_switch_at_ap = None
        self.delete_reasons_ap_initiated_delete_for_bad_aid = None
        self.delete_reasons_ap_initiated_delete_for_request = None
        self.delete_reasons_ap_initiated_delete_for_interface_reset = None
        self.delete_reasons_ap_initiated_delete_for_all_on_slot = None
        self.delete_reasons_ap_initiated_delete_for_reaper_radio = None
        self.delete_reasons_ap_initiated_delete_for_slot_disable = None
        self.delete_reasons_ap_initiated_delete_for_mic_failure = None
        self.delete_reasons_ap_initiated_delete_for_vlan_delete = None
        self.delete_reasons_ap_initiated_delete_for_channel_change = None
        self.delete_reasons_ap_initiated_delete_for_stop_reassociation = None
        self.delete_reasons_ap_initiated_delete_for_packet_max_retry = None
        self.delete_reasons_ap_initiated_delete_for_transmission_deauth = None
        self.delete_reasons_ap_initiated_delete_for_sensor_station_timeout = None
        self.delete_reasons_ap_initiated_delete_for_age_timeout = None
        self.delete_reasons_ap_initiated_delete_for_transmission_fail_threshold = None
        self.delete_reasons_ap_initiated_delete_for_uplink_receive_timeout = None
        self.delete_reasons_ap_initiated_delete_for_sensor_scan_next_radio = None
        self.delete_reasons_ap_initiated_delete_for_sensor_scan_other_bssid = None
        self.delete_reasons_aaa_server_unavailable = None
        self.delete_reasons_aaa_server_not_ready = None
        self.delete_reasons_no_dot1x_method_configuration = None
        self.delete_reasons_client_abort = None
        self.delete_reasons_association_connection_timeout = None
        self.delete_reasons_mac_auth_connection_timeout = None
        self.delete_reasons_l2_auth_connection_timeout = None
        self.delete_reasons_l3_auth_connection_timeout = None
        self.delete_reasons_mobility_connection_timeout = None
        self.delete_reasons_static_ip_connection_timeout = None
        self.delete_reasons_sm_session_creation_timeout = None
        self.delete_reasons_ip_learn_connection_timeout = None
        self.delete_reasons_nack_ifid_exists = None
        self.delete_reasons_radio_down = None
        self.delete_reasons_guest_lan_invalid_mbssid = None
        self.delete_reasons_guest_lan_no_memory = None
        self.delete_reasons_guest_lan_ceate_request_failed = None
        self.delete_reasons_eogre_reset = None
        self.delete_reasons_eogre_generic_join_failure = None
        self.delete_reasons_eogre_ha_reconciliation = None
        self.delete_reasons_eogre_invalid_vlan = None
        self.delete_reasons_eogre_invalid_domain = None
        self.delete_reasons_eogre_empty_domain = None
        self.delete_reasons_eogre_domain_shut = None
        self.delete_reasons_eogre_invalid_gateway = None
        self.delete_reasons_eogre_all_gateways_down = None
        self.delete_reasons_eogre_flex_no_active_gateway = None
        self.delete_reasons_eogre_rule_matching_error = None
        self.delete_reasons_eogre_aaa_override_error = None
        self.delete_reasons_eogre_client_onboarding_error = None
        self.delete_reasons_eogre_mobility_handoff_error = None
        self.delete_reasons_ip_update_timeout = None
        self.delete_reasons_mobility_peer_delete = None
        self.delete_reasons_nack_ifid_mismatch = None


    def update_name(self):
        self.name = 'Clients statistics'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Https_Server():
    def __init__(self, name=None):
        self.objname = 'HTTP(s) server config'
        self.name = 'HTTP(s) server config'
        self.type = 'mixed'  # defines if class contain operational or config data
        self.http_server_status = None
        self.http_server_port = None
        self.http_server_active_supplementary_listener_ports = None
        self.http_server_authentication_method = None
        self.http_server_auth_retry_0_time_window_0 = None
        self.http_server_digest_algorithm = None
        self.http_server_access_class = None
        self.http_server_ipv4_access_class = None
        self.http_server_ipv6_access_class = None
        self.http_server_base_path = None
        self.http_file_upload_status = None
        self.http_server_upload_path = None
        self.http_server_help_root = None
        self.maximum_number_of_concurrent_server_connections_allowed = None
        self.maximum_number_of_secondary_server_connections_allowed = None
        self.server_idle_time_out = None
        self.server_life_time_out = None
        self.server_session_idle_time_out = None
        self.maximum_number_of_requests_allowed_on_a_connection = None
        self.server_linger_time = None
        self.http_server_active_session_modules = None
        self.http_secure_server_capability = None
        self.http_secure_server_status = None
        self.http_secure_server_port = None
        self.http_secure_server_ciphersuite = None
        self.http_secure_server_tls_version = None
        self.http_secure_server_client_authentication = None
        self.http_secure_server_piv_authentication = None
        self.http_secure_server_piv_authorization_only = None
        self.http_secure_server_trustpoint = None
        self.http_secure_server_peer_validation_trustpoint = None
        self.http_secure_server_ecdhe_curve = None
        self.http_secure_server_active_session_modules = None

    def update_name(self):
        self.name = 'HTTP(s) server config'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Multicast():
    def __init__(self, name=None):
        self.objname = 'Multicast config'
        self.name = 'Multicast config'
        self.type = 'config'  # defines if class contain operational or config data
        self.multicast = None
        self.ap_capwap_multicast = None
        self.ap_capwap_ipv4_multicast_group_address = None
        self.ap_capwap_ipv6_multicast_group_address = None
        self.wireless_broadcast = None
        self.wireless_multicast_non_ip_mcast = None

    def update_name(self):
        self.name = 'Multicast config'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Mobility_All():
    def __init__(self, name=None):
        self.objname = 'Mobility config and list of mobility members'
        self.name = 'Mobility config and members list'
        self.type = 'mixed'  # defines if class contain operational or config data
        self.wireless_management_vlan = None
        self.wireless_management_ip_address = None
        self.wireless_management_ipv6_address = None
        self.mobility_control_message_dscp_value = None
        self.mobility_keepalive_interval_count = None
        self.mobility_group_name = None
        self.mobility_multicast_ipv4_address = None
        self.mobility_multicast_ipv6_address = None
        self.mobility_mac_address = None
        self.mobility_members = NamedList('Mobility members','Mobility member')

    def update_name(self):
        self.name = 'Mobility config and members list'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Mobility_Member():
    def __init__(self, name=None):
        self.objname = 'Mobility Member Information'
        self.name = None
        self.type = 'mixed'  # defines if class contain operational or config data
        self.ip_address = None
        self.public_ip = None
        self.mac_address = None
        self.group_name = None
        self.multicast_ipv4 = None
        self.multicast_ipv6 = None
        self.status = None
        self.pmtu = None

    def update_name(self):
        self.name = self.ip_address

    def __str__(self):
        return 'Mobility Member info for ' + self.name

    def __repr__(self):
        return 'Mobility Member info for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Advanced_Eap():
    def __init__(self, name=None):
        self.objname = 'EAP timers'
        self.type = 'config'
        self.name = None
        self.eap_identity_request_timeout_seconds = None
        self.eap_identity_request_max_retries = None
        self.eap_max_login_ignore_identity_response = None
        self.eap_request_timeout_seconds = None
        self.eap_request_max_retries = None
        self.eapol_key_timeout_milliseconds = None
        self.eapol_key_max_retries = None
        self.eap_broadcast_key_interval = None

    def update_name(self):
        if self.objname is not None:
            self.name = self.objname
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'EAP timers'

    def __repr__(self):
        return 'EAP timers'

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Rf_Tag():
    def __init__(self, name=None):
        self.objname = 'RF TAG'
        self.type = 'config'
        self.name = None
        self.tag_name = None
        self.description = None
        self.rf_policy_5ghz = None
        self.rf_policy_24ghz = None

    def update_name(self):
        if self.tag_name is not None:
            self.name = self.tag_name
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'RF TAG ' + self.name

    def __repr__(self):
        return 'RF TAG ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Site_Tag():
    def __init__(self, name=None):
        self.objname = 'Site TAG'
        self.type = 'config'
        self.name = None
        self.site_tag_name = None
        self.description = None
        self.flex_profile = None
        self.ap_profile = None
        self.local_site = None
        self.fabric_control_plane = None
        self.image_download_profile = None

    def update_name(self):
        if self.site_tag_name is not None:
            self.name = self.site_tag_name
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'Site TAG ' + self.name

    def __repr__(self):
        return 'Site TAG ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Policy_Tag():
    def __init__(self, name=None):
        self.objname = 'Policy TAG'
        self.type = 'config'
        self.name = None
        self.policy_tag_name = None
        self.description = None
        self.wlan_policy_mappings = NamedList('WLAN-policy mappings', 'WLAN-policy mapping') #{'attribute_name':'vlan_mappings','end_table_string':'HTTP-Proxy','list_name':'Flex VLAN mappings','item_name':'Flex VLAN mapping','item_class_name':'Ewlc_Flex_Vlan_Mapping'}, #example for table parsing
        self.rlan_policy_mappings = NamedList('Remote-LAN-policy mappings', 'Remote-LAN-policy mapping') #{'attribute_name':'vlan_mappings','end_table_string':'HTTP-Proxy','list_name':'Flex VLAN mappings','item_name':'Flex VLAN mapping','item_class_name':'Ewlc_Flex_Vlan_Mapping'}, #example for table parsing

    def update_name(self):
        if self.policy_tag_name is not None:
            self.name = self.policy_tag_name
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'Policy TAG ' + self.name

    def __repr__(self):
        return 'Policy TAG ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Wlan_Policy_Mapping():
    def __init__(self, name=None):
        self.objname = 'WLAN - Policy mapping'
        self.type = 'config'
        self.wlan_profile_name = None
        self.policy_name = None

    def update_name(self):
        if self.wlan_profile_name is not None and self.policy_name is not None:
            self.name = self.wlan_profile_name + ' ' + self.policy_name
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'WLAN - Policy mapping ' + self.name

    def __repr__(self):
        return 'WLAN - Policy mapping ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Ewlc_Rlan_Policy_Mapping():
    def __init__(self, name=None):
        self.objname = 'RLAN - Policy mapping'
        self.type = 'config'
        self.remote_lan_profile_name = None
        self.policy_name = None
        self.port_id = None

    def update_name(self):
        if self.remote_lan_profile_name is not None and self.policy_name is not None:
            self.name = self.remote_lan_profile_name + ' ' + self.policy_name
        else:
            self.name = 'Unknown'

    def __str__(self):
        return 'RLAN - Policy mapping ' + self.name

    def __repr__(self):
        return 'RLAN - Policy mapping ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Rogue_Ap_All():
    def __init__(self, name=None):
        self.objname = 'Rogue APs config and list of rogue APs'
        self.name = 'Rogue AP config and list'
        self.type = 'mixed'  # defines if class contain operational or config data
        self.rogue_location_discovery_protocol = None
        self.validate_rogue_aps_against_aaa = None
        self.rogue_security_level = None
        self.rogue_on_wire_auto_contain = None
        self.rogue_using_our_ssid_auto_contain = None
        self.valid_client_on_rogue_ap_auto_contain = None
        self.rogue_ap_timeout = None
        self.default_rogue_detection_report_interval = None
        self.default_rogue_ap_minimum_rssi = None
        self.default_rogue_ap_minimum_transient_time = None
        self.rogue_aps_list = NamedList('Rogue APs','Rogue AP')

    def update_name(self):
        self.name = 'Rogue AP config and APs list'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Rogue_Ap():
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
        self.rssi_value = None
        self.channel = None
        self.band = None #Not an attribute in WLC but added after parsing
        self.last_heard = None

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

class Ewlc_Flex_Vlan_Mapping():
    def __init__(self, name=None):
        self.objname = 'Flex VLAN mapping ID-name'
        self.type = 'config'
        self.name = None
        self.vlan_name = None
        self.vlan_id = None
        self.acl_name = None

    def update_name(self):
        self.name = self.vlan_name

    def __str__(self):
        return 'Flex VLAN mapping ' + self.name

    def __repr__(self):
        return 'Flex VLAN mapping ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Flex_Profile():
    def __init__(self, name=None):
        self.objname = 'Flex profile'
        self.type = 'config'
        self.flex_profile_name = None
        self.description = None
        self.local_auth = None
        self.local_auth_radius_enable = None
        self.local_auth_peap = None
        self.local_auth_leap = None
        self.local_auth_tls = None
        self.local_auth_eap_fast_profile = None
        self.local_auth_user_list = None
        self.radius = None
        self.radius_radius_server_group_name = None
        self.fallback_radio_shut = None
        self.arp_caching = None
        self.efficient_image_upgrade = None
        self.officeextend_ap = None
        self.join_min_latency = None
        self.policy_acl = None
        self.vlan_mappings = NamedList('Flex VLAN mappings','Flex VLAN mapping') #{'attribute_name':'vlan_mappings','end_table_string':'HTTP-Proxy','list_name':'Flex VLAN mappings','item_name':'Flex VLAN mapping','item_class_name':'Ewlc_Flex_Vlan_Mapping'}, #example for table parsing
        self.http_proxy_ip_address = None
        self.http_proxy_port = None
        self.native_vlan_id = None
        self.flex_resilient = None
        self.cts_policy = None
        self.cts_policy_inline_tagging = None
        self.cts_policy_sgacl_enforcement = None
        self.cts_policy_cts_profile_name = None

    def update_name(self):
        self.name = self.flex_profile_name

    def __str__(self):
        return 'Flex profile ' + self.name

    def __repr__(self):
        return 'Flex profile ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Ap_Join_Profile():
    def __init__(self, name=None):
        self.objname = 'AP join profile config'
        self.type = 'config'
        self.name = None
        self.ap_profile_name = None
        self.description = None
        self.stats_timer = None
        self.link_latency = None
        self.data_encryption = None
        self.led_state = None
        self.ntp_server = None
        self.jumbo_mtu = None
        self.d_24ghz_report_interval = None
        self.d_5ghz_report_interval = None
        self.bssid_stats_status = None
        self.bssid_stats_frqncy_interval = None
        self.bssid_neighbor_stats_status = None
        self.bssid_neighbor_stats_interval = None
        self.poe_config = None
        self.poe_config_prestandard_802_3af_switch = None
        self.poe_config_power_injector_state = None
        self.poe_config_power_injector_selection = None
        self.poe_config_injector_switch_mac = None
        self.device_management = None
        self.device_management_telnet = None
        self.device_management_ssh = None
        self.user_management = None
        self.user_management_username = None
        self.tcp_mss = None
        self.tcp_mss_adjust_mss = None
        self.tcp_mss_tcp_adjust_mss = None
        self.capwap_timer = None
        self.capwap_timer_heartbeat_timeout = None
        self.capwap_timer_discovery_timeout = None
        self.capwap_timer_fast_heartbeat_timeout = None
        self.capwap_timer_primary_discovery_timeout = None
        self.capwap_timer_primed_join_timeout = None
        self.retransmit_timer = None
        self.retransmit_timer_count = None
        self.retransmit_timer_interval = None
        self.login_credentials = None
        self.login_credentials_local_username = None
        self.login_credentials_dot1x_username = None
        self.ap_eap_auth_info = None
        self.ap_eap_auth_info_dot1x_eap_method = None
        self.ap_eap_auth_info_lsc_ap_auth_state = None
        self.syslog = None
        self.syslog_facility_value = None
        self.syslog_host = None
        self.syslog_log_level = None
        self.backup_controllers = None
        self.backup_controllers_fallback = None
        self.backup_controllers_primary_backup_name = None
        self.backup_controllers_primary_backup_ip = None
        self.backup_controllers_secondary_backup_name = None
        self.backup_controllers_secondary_backup_ip = None
        self.hyperlocation = None
        self.hyperlocation_admin_state = None
        self.hyperlocation_pak_rssi_threshold_detection = None
        self.hyperlocation_pak_rssi_threshold_trigger = None
        self.hyperlocation_pak_rssi_threshold_reset = None
        self.halo_ble_beacon = None
        self.halo_ble_beacon_interval = None
        self.halo_ble_beacon_tx_power = None
        self.halo_ble_beacon_enabled = None
        self.halo_ble_beacon_apply_global = None
        self.group_nas_id = None
        self.cdp = None
        self.tftp_downgrade = None
        self.tftp_downgrade_ip_address = None
        self.tftp_downgrade_filename = None
        self.time_limit = None
        self.capwap_window_size = None
        self.ap_packet_capture_profile = None
        self.ap_trace_profile = None
        self.mesh_profile_name = None
        self.method_list_name = None
        self.packet_sequence_jump_delba = None
        self.lag_status = None
        self.extended_module = None
        self.usb_module = None
        self.persistent_ssid_broadcast = None
        self.dhcp_server = None
        self.preferred_mode = None
        self.capwap_udp_lite = None
        self.awips = None
        self.fallback_to_dhcp = None
        self.client_rssi_statistics = None
        self.client_rssi_statistics_reporting = None
        self.client_rssi_statistics_reporting_interval = None
        self.traffic_distribution_stats = None
        self.traffic_distribution_stats_interval_sec = None
        self.oeap_mode_config = None
        self.oeap_mode_config_link_encryption = None
        self.oeap_mode_config_rogue_detection = None
        self.oeap_mode_config_local_access = None

    def update_name(self):
        self.name = self.ap_profile_name

    def __str__(self):
        return 'AP join Profile config ' + self.name

    def __repr__(self):
        return 'AP join Profile config ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Policy_Profile():
    def __init__(self, name=None):
        self.objname = 'Policy Profile config'
        self.type = 'config'
        self.name = None
        self.policy_profile_name = None
        self.description = None
        self.status = None
        self.vlan = None
        self.multicast_vlan = None
        self.osen_client_vlan = None
        self.multicast_filter = None
        self.qbss_load = None
        self.passive_client = None
        self.et_analytics = None
        self.staticip_mobility = None
        self.wlan_switching_policy = None
        self.wlan_switching_policy_flex_central_switching = None
        self.wlan_switching_policy_flex_central_authentication = None
        self.wlan_switching_policy_flex_central_dhcp = None
        self.wlan_switching_policy_flex_nat_pat = None
        self.wlan_switching_policy_flex_central_assoc = None
        self.wlan_flex_policy = None
        self.wlan_flex_policy_vlan_based_central_switching = None
        self.wlan_acl = None
        self.wlan_acl_ipv4_acl = None
        self.wlan_acl_ipv6_acl = None
        self.wlan_acl_layer2_acl = None
        self.wlan_acl_preauth_urlfilter_list = None
        self.wlan_acl_postauth_urlfilter_list = None
        self.wlan_timeout = None
        self.wlan_timeout_session_timeout = None
        self.wlan_timeout_idle_timeout = None
        self.wlan_timeout_idle_threshold = None
        self.wlan_timeout_guest_lan_session_timeout = None
        self.wlan_local_profiling = None
        self.wlan_local_profiling_subscriber_policy_name = None
        self.wlan_local_profiling_radius_profiling = None
        self.wlan_local_profiling_http_tlv_caching = None
        self.wlan_local_profiling_dhcp_tlv_caching = None
        self.cts_policy = None
        self.cts_policy_inline_tagging = None
        self.cts_policy_sgacl_enforcement = None
        self.cts_policy_default_sgt = None
        self.wlan_mobility = None
        self.wlan_mobility_anchor = None
        self.avc_visibility = None
        self.ipv4_flow_monitors = None
        self.ipv4_flow_monitors_ingress = None
        self.ipv4_flow_monitors_ingress_wireless_avc_basic = None
        self.ipv4_flow_monitors_egress = None
        self.ipv4_flow_monitors_egress_wireless_avc_basic = None
        self.ipv6_flow_monitors = None
        self.ipv6_flow_monitors_ingress = None
        self.ipv6_flow_monitors_egress = None
        self.nbar_protocol_discovery = None
        self.reanchoring = None
        self.classmap_name_for_reanchoring = None
        self.classmap_name_for_reanchoring_reanchoring_classmap_name = None
        self.qos_per_ssid = None
        self.qos_per_ssid_ingress_service_name = None
        self.qos_per_ssid_egress_service_name = None
        self.qos_per_client = None
        self.qos_per_client_ingress_service_name = None
        self.qos_per_client_egress_service_name = None
        self.umbrella_information = None
        self.umbrella_information_cisco_umbrella_parameter_map = None
        self.umbrella_information_dhcp_dns_option = None
        self.umbrella_information_mode = None
        self.autoqos_mode = None
        self.call_snooping = None
        self.tunnel_profile = None
        self.tunnel_profile_profile_name = None
        self.calendar_profile = None
        self.fabric_profile = None
        self.fabric_profile_profile_name = None
        self.accounting_list = None
        self.accounting_list_accounting_list = None
        self.accounting_list_required = None
        self.accounting_list_server_address = None
        self.opt82 = None
        self.opt82_dhcpopt82enable = None
        self.opt82_dhcpopt82ascii = None
        self.opt82_dhcpopt82rid = None
        self.opt82_apmac = None
        self.opt82_ssid = None
        self.opt82_ap_ethmac = None
        self.opt82_apname = None
        self.opt82_policy_tag = None
        self.opt82_ap_location = None
        self.opt82_vlan_id = None
        self.exclusionlist_params = None
        self.exclusionlist_params_exclusionlist = None
        self.exclusionlist_params_exclusion_timeout = None
        self.aaa_policy_params = None
        self.aaa_policy_params_aaa_override = None
        self.aaa_policy_params_nac = None
        self.aaa_policy_params_aaa_policy_name = None
        self.wgb_policy_params = None
        self.wgb_policy_params_broadcast_tagging = None
        self.wgb_policy_params_client_vlan = None
        self.hotspot_2_0_server_name = None
        self.mobility_anchor_list = None
        self.mobility_anchor_list_ip_address__priority = None
        self.mobility_anchor_list__ = None
        self.mdns_gateway = None
        self.mdns_gateway_mdns_service_policy_name = None
        self.user_defined_private_network = None
        self.user_defined_private_network_unicast_drop = None
        self.policy_proxy_settings = None
        self.policy_proxy_settings_arp_proxy_state = None
        self.policy_proxy_settings_ipv6_proxy_state = None
        self.airtime_fairness_profile = None
        self.airtime_fairness_profile_2_4ghz_atf_policy = None
        self.airtime_fairness_profile_5ghz_atf_policy = None

    def update_name(self):
        self.name = self.policy_profile_name

    def __str__(self):
        return 'Policy Profile config ' + self.name

    def __repr__(self):
        return 'Policy Profile config ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Ssid_Config():
    def __init__(self, name=None):
        self.objname = 'SSID config'
        self.wlan_profile_name = None
        self.identifier = None
        self.description = None
        self.network_name_ssid = None
        self.status = None
        self.broadcast_ssid = None
        self.advertise_apname = None
        self.universal_ap_admin = None
        self.max_associated_clients_per_wlan = None
        self.max_associated_clients_per_ap_per_wlan = None
        self.max_associated_clients_per_ap_radio_per_wlan = None
        self.okc = None
        self.number_of_active_clients = None
        self.chd_per_wlan = None
        self.wmm = None
        self.wifi_direct_policy = None
        self.channel_scan_defer_priority = None
        self.channel_scan_defer_priority_priority_default = None
        self.scan_defer_time_msecs = None
        self.media_stream_multicast_direct = None
        self.ccx_aironetie_support = None
        self.peer_to_peer_blocking_action = None
        self.radio_policy = None
        self.dtim_period_for_802_11a_radio = None
        self.dtim_period_for_802_11b_radio = None
        self.local_eap_authentication = None
        self.mac_filter_authorization_list_name = None
        self.mac_filter_override_authorization_list_name = None
        self.accounting_list_name = None
        self.d_802_1x_authentication_list_name = None
        self.d_802_1x_authorization_list_name = None
        self.security = None
        self.security_802_11_authentication = None
        self.security_static_wep_keys = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3 = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa_ssn_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_aes_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_ccmp256_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_gcmp128_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_gcmp256_cipher = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_802_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_psk = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_cckm = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_ft_dot1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_ft_psk = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_dot1x_sha256 = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_psk_sha256 = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_sae = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_owe = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_suiteb_1x = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_suiteb192_1x = None
        self.security_cckm_tsf_tolerance_msecs = None
        self.security_owe_transition_mode = None
        self.security_osen = None
        self.security_ft_support = None
        self.security_ft_support_ft_reassociation_timeout_secs = None
        self.security_ft_support_ft_over_the_ds_mode = None
        self.security_pmf_support = None
        self.security_pmf_support_pmf_association_comeback_timeout_secs = None
        self.security_pmf_support_pmf_sa_query_time_msecs = None
        self.security_web_based_authentication = None
        self.security_conditional_web_redirect = None
        self.security_splash_page_web_redirect = None
        self.security_webauth_on_mac_filter_failure = None
        self.security_webauth_authentication_list_name = None
        self.security_webauth_authorization_list_name = None
        self.security_webauth_parameter_map = None
        self.band_select = None
        self.load_balancing = None
        self.multicast_buffer = None
        self.multicast_buffers_frames = None
        self.ip_source_guard = None
        self.assisted_roaming = None
        self.assisted_roaming_neighbor_list = None
        self.assisted_roaming_prediction_list = None
        self.assisted_roaming_dual_band_support = None
        self.ieee_802_11v_parameters = None
        self.ieee_802_11v_parameters_directed_multicast_service = None
        self.ieee_802_11v_parameters_bss_max_idle = None
        self.ieee_802_11v_parameters_bss_max_idle_protected_mode = None
        self.ieee_802_11v_parameters_traffic_filtering_service = None
        self.ieee_802_11v_parameters_bss_transition = None
        self.ieee_802_11v_parameters_bss_transition_disassociation_imminent = None
        self.ieee_802_11v_parameters_bss_transition_disassociation_imminent_optimised_roaming_timer_tbtts = None
        self.ieee_802_11v_parameters_bss_transition_disassociation_imminent_timer_tbtts = None
        self.ieee_802_11v_parameters_bss_transition_dual_neighbor_list = None
        self.ieee_802_11v_parameters_wnm_sleep_mode = None
        self.d_802_11ac_mu_mimo = None
        self.d_802_11ax_parameters = None
        self.d_802_11ax_parameters_ofdma_downlink = None
        self.d_802_11ax_parameters_ofdma_uplink = None
        self.d_802_11ax_parameters_mu_mimo_downlink = None
        self.d_802_11ax_parameters_mu_mimo_uplink = None
        self.d_802_11ax_parameters_bss_target_wake_up_time = None
        self.d_802_11ax_parameters_bss_target_wake_up_time_broadcast_support = None
        self.mdns_gateway_status = None
        self.wifi_alliance_agile_multiband = None
        self.device_analytics = None
        self.device_analytics_advertise_support = None
        self.device_analytics_share_data_with_client = None
        self.client_scan_report_11k_beacon_radio_measurement = None
        self.client_scan_report_11k_beacon_radio_measurement_request_on_association = None
        self.client_scan_report_11k_beacon_radio_measurement_request_on_roam = None
        self.wifi_to_cellular_steering = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie_mpsk = None
        self.security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie_randomized_gtk = None
        self.security_owe_transition_mode_wlan_id = None
        self.security_web_based_authentication_ipv4_acl = None
        self.security_web_based_authentication_ipv6_acl = None

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

class Ewlc_Nearby_Ap():
    def __init__(self, name=None):
        self.objname = 'Nearby AP Information'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data
        self.mac_address = None
        self.rssi = None
        self.channel = None
        self.bandwidth = None
        self.rf_leader = None
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


class Ewlc_Nearby_Aps(NamedList):  # This class is important to add name attribute of AP that heard this list of APs
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

class Ewlc_Ap_Rf_24_Config():
    def __init__(self, name=None):
        self.objname = 'AP RF data for 2.4 GHz'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data #self.objname = XXX
        self.number_of_slots = None
        self.ap_name = None
        self.mac_address = None
        self.slot_id = None
        self.radio_type = None
        self.subband_type = None
        self.noise_information = None
        self.noise_information_noise_profile = None
        self.noise_information_channel_1 = None
        self.noise_information_channel_2 = None
        self.noise_information_channel_3 = None
        self.noise_information_channel_4 = None
        self.noise_information_channel_5 = None
        self.noise_information_channel_6 = None
        self.noise_information_channel_7 = None
        self.noise_information_channel_8 = None
        self.noise_information_channel_9 = None
        self.noise_information_channel_10 = None
        self.noise_information_channel_11 = None
        self.noise_information_channel_12 = None
        self.noise_information_channel_13 = None
        self.noise_information_channel_14 = None
        self.interference_information = None
        self.interference_information_interference_profile = None
        self.interference_information_channel_1 = None
        self.interference_information_channel_2 = None
        self.interference_information_channel_3 = None
        self.interference_information_channel_4 = None
        self.interference_information_channel_5 = None
        self.interference_information_channel_6 = None
        self.interference_information_channel_7 = None
        self.interference_information_channel_8 = None
        self.interference_information_channel_9 = None
        self.interference_information_channel_10 = None
        self.interference_information_channel_11 = None
        self.interference_information_channel_12 = None
        self.interference_information_channel_13 = None
        self.interference_information_rogue_histogram_20 = None
        self.interference_information_rogue_histogram_20_channel_1 = None
        self.interference_information_rogue_histogram_20_channel_2 = None
        self.interference_information_rogue_histogram_20_channel_3 = None
        self.interference_information_rogue_histogram_20_channel_4 = None
        self.interference_information_rogue_histogram_20_channel_5 = None
        self.interference_information_rogue_histogram_20_channel_6 = None
        self.interference_information_rogue_histogram_20_channel_7 = None
        self.interference_information_rogue_histogram_20_channel_8 = None
        self.interference_information_rogue_histogram_20_channel_9 = None
        self.interference_information_rogue_histogram_20_channel_10 = None
        self.interference_information_rogue_histogram_20_channel_11 = None
        self.interference_information_rogue_histogram_20_channel_12 = None
        self.interference_information_rogue_histogram_20_channel_13 = None
        self.load_information = None
        self.load_information_load_profile = None
        self.load_information_receive_utilization = None
        self.load_information_transmit_utilization = None
        self.load_information_channel_utilization = None
        self.load_information_attached_clients = None
        self.coverage_information = None
        self.coverage_information_coverage_profile = None
        self.coverage_information_failed_clients = None
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
        self.radar_information_detected_channels = None
        self.radar_information_blacklist_times = None
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
        self.nearby_aps = Ewlc_Nearby_Aps('Nearby_Aps', 'Nearby_Ap')


    def update_name(self):
        if self.ap_name is not None and self.slot_id is not None:
            self.name = self.ap_name + '_slot' + self.slot_id
        else:
            self.name = 'strange name'

    def __str__(self):
        return 'AP RF 2.4GHz data for ' + self.name

    def __repr__(self):
        return 'AP RF 2.4GHz data for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Ap_Rf_5_Config():
    def __init__(self, name=None):
        self.objname = 'AP RF data for 5 GHz'
        self.name = None
        self.type = 'operational'  # defines if class contain operational or config data #self.objname = XXX
        self.number_of_slots = None
        self.ap_name = None
        self.mac_address = None
        self.slot_id = None
        self.radio_type = None
        self.subband_type = None
        self.noise_information = None
        self.noise_information_noise_profile = None
        self.noise_information_channel_34 = None
        self.noise_information_channel_36 = None
        self.noise_information_channel_38 = None
        self.noise_information_channel_40 = None
        self.noise_information_channel_42 = None
        self.noise_information_channel_44 = None
        self.noise_information_channel_46 = None
        self.noise_information_channel_48 = None
        self.noise_information_channel_52 = None
        self.noise_information_channel_56 = None
        self.noise_information_channel_60 = None
        self.noise_information_channel_64 = None
        self.noise_information_channel_100 = None
        self.noise_information_channel_104 = None
        self.noise_information_channel_108 = None
        self.noise_information_channel_112 = None
        self.noise_information_channel_116 = None
        self.noise_information_channel_120 = None
        self.noise_information_channel_124 = None
        self.noise_information_channel_128 = None
        self.noise_information_channel_132 = None
        self.noise_information_channel_136 = None
        self.noise_information_channel_140 = None
        self.noise_information_channel_144 = None
        self.noise_information_channel_149 = None
        self.noise_information_channel_153 = None
        self.noise_information_channel_157 = None
        self.noise_information_channel_161 = None
        self.noise_information_channel_165 = None
        self.noise_information_channel_169 = None
        self.noise_information_channel_173 = None
        self.interference_information = None
        self.interference_information_interference_profile = None
        self.interference_information_channel_34 = None
        self.interference_information_channel_36 = None
        self.interference_information_channel_38 = None
        self.interference_information_channel_40 = None
        self.interference_information_channel_42 = None
        self.interference_information_channel_44 = None
        self.interference_information_channel_46 = None
        self.interference_information_channel_48 = None
        self.interference_information_channel_52 = None
        self.interference_information_channel_56 = None
        self.interference_information_channel_60 = None
        self.interference_information_channel_64 = None
        self.interference_information_channel_100 = None
        self.interference_information_channel_104 = None
        self.interference_information_channel_108 = None
        self.interference_information_channel_112 = None
        self.interference_information_channel_116 = None
        self.interference_information_channel_120 = None
        self.interference_information_channel_124 = None
        self.interference_information_channel_128 = None
        self.interference_information_channel_132 = None
        self.interference_information_channel_136 = None
        self.interference_information_channel_140 = None
        self.interference_information_channel_144 = None
        self.interference_information_channel_149 = None
        self.interference_information_channel_153 = None
        self.interference_information_channel_157 = None
        self.interference_information_channel_161 = None
        self.interference_information_channel_165 = None
        self.interference_information_channel_169 = None
        self.interference_information_channel_173 = None
        self.interference_information_rogue_histogram_20_40_80 = None
        self.interference_information_rogue_histogram_20_40_80_channel_36 = None
        self.interference_information_rogue_histogram_20_40_80_channel_40 = None
        self.interference_information_rogue_histogram_20_40_80_channel_44 = None
        self.interference_information_rogue_histogram_20_40_80_channel_48 = None
        self.interference_information_rogue_histogram_20_40_80_channel_52 = None
        self.interference_information_rogue_histogram_20_40_80_channel_56 = None
        self.interference_information_rogue_histogram_20_40_80_channel_60 = None
        self.interference_information_rogue_histogram_20_40_80_channel_64 = None
        self.interference_information_rogue_histogram_20_40_80_channel_132 = None
        self.interference_information_rogue_histogram_20_40_80_channel_136 = None
        self.interference_information_rogue_histogram_20_40_80_channel_140 = None
        self.interference_information_rogue_histogram_20_40_80_channel_149 = None
        self.interference_information_rogue_histogram_20_40_80_channel_153 = None
        self.interference_information_rogue_histogram_20_40_80_channel_157 = None
        self.interference_information_rogue_histogram_20_40_80_channel_161 = None
        self.interference_information_rogue_histogram_20_40_80_channel_34 = None
        self.interference_information_rogue_histogram_20_40_80_channel_38 = None
        self.interference_information_rogue_histogram_20_40_80_channel_42 = None
        self.interference_information_rogue_histogram_20_40_80_channel_46 = None
        self.interference_information_rogue_histogram_20_40_80_channel_100 = None
        self.interference_information_rogue_histogram_20_40_80_channel_104 = None
        self.interference_information_rogue_histogram_20_40_80_channel_108 = None
        self.interference_information_rogue_histogram_20_40_80_channel_112 = None
        self.interference_information_rogue_histogram_20_40_80_channel_116 = None
        self.interference_information_rogue_histogram_20_40_80_channel_120 = None
        self.interference_information_rogue_histogram_20_40_80_channel_124 = None
        self.interference_information_rogue_histogram_20_40_80_channel_128 = None
        self.interference_information_rogue_histogram_20_40_80_channel_144 = None
        self.interference_information_rogue_histogram_20_40_80_channel_165 = None
        self.interference_information_rogue_histogram_20_40_80_channel_169 = None
        self.interference_information_rogue_histogram_20_40_80_channel_173 = None
        self.interference_information_radar_information_detected_channels = None
        self.interference_information_radar_information_blacklist_times = None
        self.interference_information_radar_information = None
        self.load_information = None
        self.load_information_load_profile = None
        self.load_information_receive_utilization = None
        self.load_information_transmit_utilization = None
        self.load_information_channel_utilization = None
        self.load_information_attached_clients = None
        self.coverage_information = None
        self.coverage_information_coverage_profile = None
        self.coverage_information_failed_clients = None
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
        self.radar_information_detected_channels = None
        self.radar_information_blacklist_times = None
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
        self.nearby_aps = Ewlc_Nearby_Aps('Nearby_Aps', 'Nearby_Ap')

    def update_name(self):
        if self.ap_name is not None and self.slot_id is not None:
            self.name = self.ap_name + '_slot' + self.slot_id

    def __str__(self):
        return 'AP RF 5GHz data for ' + self.name

    def __repr__(self):
        return 'AP RF 5GHz data for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

class Ewlc_Ap_Config():
    def __init__(self, name=None):
        self.objname = 'AP Config'
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data #self.objname = XXX
        self.name = 'empty'
        self.cisco_ap_name = None
        self.cisco_ap_identifier = None
        self.country_code = None
        self.regulatory_domain_allowed_by_country = None
        self.ap_country_code = None
        self.ap_regulatory_domain = None
        self.ap_regulatory_domain_slot_0 = None
        self.ap_regulatory_domain_slot_1 = None
        self.mac_address = None
        self.ip_address_configuration = None
        self.ip_address = None
        self.ip_netmask = None
        self.gateway_ip_address = None
        self.fallback_ip_address_being_used = None
        self.domain = None
        self.name_server = None
        self.capwap_path_mtu = None
        self.capwap_active_window_size = None
        self.telnet_state = None
        self.ssh_state = None
        self.cisco_ap_location = None
        self.site_tag_name = None
        self.rf_tag_name = None
        self.policy_tag_name = None
        self.ap_join_profile = None
        self.flex_profile = None
        self.primary_cisco_controller_name = None
        self.primary_cisco_controller_ip_address = None
        self.secondary_cisco_controller_name = None
        self.secondary_cisco_controller_ip_address = None
        self.tertiary_cisco_controller_name = None
        self.tertiary_cisco_controller_ip_address = None
        self.administrative_state = None
        self.operation_state = None
        self.nat_external_ip_address = None
        self.ap_certificate_type = None
        self.ap_mode = None
        self.ap_vlan_tagging_state = None
        self.ap_vlan_tag = None
        self.capwap_preferred_mode = None
        self.ap_submode = None
        self.office_extend_mode = None
        self.dhcp_server = None
        self.remote_ap_debug = None
        self.logging_trap_severity_level = None
        self.logging_syslog_facility = None
        self.software_version = None
        self.boot_version = None
        self.mini_ios_version = None
        self.stats_reporting_period = None
        self.led_state = None
        self.poe_pre_standard_switch = None
        self.poe_power_injector_mac_address = None
        self.power_type_mode = None
        self.number_of_slots = None
        self.ap_model = None
        self.ios_version = None
        self.reset_button = None
        self.ap_serial_number = None
        self.management_frame_protection_validation = None
        self.ap_user_name = None
        self.ap_802_1x_user_mode = None
        self.ap_802_1x_user_name = None
        self.cisco_ap_system_logging_host = None
        self.cisco_ap_secured_logging_tls_mode = None
        self.ap_up_time = None
        self.ap_capwap_up_time = None
        self.join_date_and_time = None
        self.join_taken_time = None
        self.join_priority = None
        self.ap_link_latency = None
        self.ap_lag_configuration_status = None
        self.lag_support_for_ap = None
        self.rogue_detection = None
        self.rogue_containment_auto_rate = None
        self.rogue_containment_of_standalone_flexconnect_aps = None
        self.rogue_detection_report_interval = None
        self.rogue_ap_minimum_rssi = None
        self.rogue_ap_minimum_transient_time = None
        self.ap_tcp_mss_adjust = None
        self.ap_tcp_mss_size = None
        self.ap_ipv6_tcp_mss_adjust = None
        self.ap_ipv6_tcp_mss_size = None
        self.hyperlocation_admin_status = None
        self.retransmit_count = None
        self.retransmit_interval = None
        self.fabric_status = None
        self.fips_status = None
        self.wlancc_status = None
        self.usb_module_type = None
        self.usb_module_state = None
        self.usb_operational_state = None
        self.usb_override = None
        self.gas_rate_limit_admin_status = None
        self.wpa3_capability = None
        self.ewc_ap_capability = None

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

class Ewlc_Ap_Slot_Config():
    def __init__(self, name=None):
        self.objname = 'AP slot Config'
        self.slot_id = None
        self.name = None
        self.type = 'config'  # defines if class contain operational or config data #self.objname = XXX
        self.name = 'empty'
        self.ap_name = None
        self.ap_regulatory_domain = None
        self.radio_type = None
        self.radio_mode = None
        self.radio_subband = None
        self.atf_mode = None
        self.administrative_state = None
        self.operation_state = None
        self.station_configuration = None
        self.station_configuration_configuration = None
        self.station_configuration_medium_occupancy_limit = None
        self.station_configuration_cfp_period = None
        self.station_configuration_cfp_maximum_duration = None
        self.station_configuration_bssid = None
        self.station_configuration_operation_rate_set = None
        self.station_configuration_operation_rate_set_802_11b_1m_rate = None
        self.station_configuration_operation_rate_set_802_11b_2m_rate = None
        self.station_configuration_operation_rate_set_802_11b_5_5m_rate = None
        self.station_configuration_operation_rate_set_802_11b_11m_rate = None
        self.station_configuration_operation_rate_set_802_11b_6m_rate = None
        self.station_configuration_operation_rate_set_802_11b_9m_rate = None
        self.station_configuration_operation_rate_set_802_11b_12m_rate = None
        self.station_configuration_operation_rate_set_802_11b_18m_rate = None
        self.station_configuration_operation_rate_set_802_11b_24m_rate = None
        self.station_configuration_operation_rate_set_802_11b_36m_rate = None
        self.station_configuration_operation_rate_set_802_11b_48m_rate = None
        self.station_configuration_operation_rate_set_802_11b_54m_rate = None
        self.station_configuration_operation_rate_set_802_11a_6m_rate = None
        self.station_configuration_operation_rate_set_802_11a_9m_rate = None
        self.station_configuration_operation_rate_set_802_11a_12m_rate = None
        self.station_configuration_operation_rate_set_802_11a_18m_rate = None
        self.station_configuration_operation_rate_set_802_11a_24m_rate = None
        self.station_configuration_operation_rate_set_802_11a_36m_rate = None
        self.station_configuration_operation_rate_set_802_11a_48m_rate = None
        self.station_configuration_operation_rate_set_802_11a_54m_rate = None
        self.station_configuration_mcs_set = None
        self.station_configuration_mcs_set_mcs_0 = None
        self.station_configuration_mcs_set_mcs_1 = None
        self.station_configuration_mcs_set_mcs_2 = None
        self.station_configuration_mcs_set_mcs_3 = None
        self.station_configuration_mcs_set_mcs_4 = None
        self.station_configuration_mcs_set_mcs_5 = None
        self.station_configuration_mcs_set_mcs_6 = None
        self.station_configuration_mcs_set_mcs_7 = None
        self.station_configuration_mcs_set_mcs_8 = None
        self.station_configuration_mcs_set_mcs_9 = None
        self.station_configuration_mcs_set_mcs_10 = None
        self.station_configuration_mcs_set_mcs_11 = None
        self.station_configuration_mcs_set_mcs_12 = None
        self.station_configuration_mcs_set_mcs_13 = None
        self.station_configuration_mcs_set_mcs_14 = None
        self.station_configuration_mcs_set_mcs_15 = None
        self.station_configuration_mcs_set_mcs_16 = None
        self.station_configuration_mcs_set_mcs_17 = None
        self.station_configuration_mcs_set_mcs_18 = None
        self.station_configuration_mcs_set_mcs_19 = None
        self.station_configuration_mcs_set_mcs_20 = None
        self.station_configuration_mcs_set_mcs_21 = None
        self.station_configuration_mcs_set_mcs_22 = None
        self.station_configuration_mcs_set_mcs_23 = None
        self.station_configuration_mcs_set_mcs_24 = None
        self.station_configuration_mcs_set_mcs_25 = None
        self.station_configuration_mcs_set_mcs_26 = None
        self.station_configuration_mcs_set_mcs_27 = None
        self.station_configuration_mcs_set_mcs_28 = None
        self.station_configuration_mcs_set_mcs_29 = None
        self.station_configuration_mcs_set_mcs_30 = None
        self.station_configuration_mcs_set_mcs_31 = None
        self.station_configuration_beacon_period = None
        self.station_configuration_multi_domain_capability_implemented = None
        self.station_configuration_multi_domain_capability_enabled = None
        self.station_configuration_country_string = None
        self.multi_domain_capability = None
        self.multi_domain_capability_configuration = None
        self.multi_domain_capability_first_channel = None
        self.multi_domain_capability_number_of_channels = None
        self.multi_domain_capability_mac_operation_parameters = None
        self.multi_domain_capability_mac_operation_parameters_configuration = None
        self.multi_domain_capability_mac_operation_parameters_fragmentation_threshold = None
        self.multi_domain_capability_mac_operation_parameters_packet_retry_limit = None
        self.multi_domain_capability_mac_operation_parameters_rts_cts_threshold = None
        self.multi_domain_capability_mac_operation_parameters_rts_cts_threshold_ = None
        self.multi_domain_capability_tx_power = None
        self.multi_domain_capability_tx_power_number_of_supported_power_levels = None
        self.multi_domain_capability_tx_power_tx_power_level_1 = None
        self.multi_domain_capability_tx_power_tx_power_level_2 = None
        self.multi_domain_capability_tx_power_tx_power_level_3 = None
        self.multi_domain_capability_tx_power_tx_power_level_4 = None
        self.multi_domain_capability_tx_power_tx_power_level_5 = None
        self.multi_domain_capability_tx_power_tx_power_level_6 = None
        self.multi_domain_capability_tx_power_tx_power_level_7 = None
        self.multi_domain_capability_tx_power_tx_power_level_8 = None
        self.multi_domain_capability_tx_power_tx_power_configuration = None
        self.multi_domain_capability_tx_power_current_tx_power_level = None
        self.multi_domain_capability_tx_power_tx_power_assigned_by = None
        self.multi_domain_capability_phy_ofdm_parameters = None
        self.multi_domain_capability_phy_ofdm_parameters_configuration = None
        self.multi_domain_capability_phy_ofdm_parameters_current_channel = None
        self.multi_domain_capability_phy_ofdm_parameters_channel_assigned_by = None
        self.multi_domain_capability_phy_ofdm_parameters_extension_channel = None
        self.multi_domain_capability_phy_ofdm_parameters_channel_width = None
        self.multi_domain_capability_phy_ofdm_parameters_allowed_channel_list = None
        self.multi_domain_capability_phy_ofdm_parameters_ti_threshold = None
        self.multi_domain_capability_phy_ofdm_parameters_dca_channel_list = None
        self.multi_domain_capability_phy_ofdm_parameters_antenna_type = None
        self.multi_domain_capability_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units = None
        self.multi_domain_capability_phy_ofdm_parameters_diversity = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_a = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_b = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_c = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_d = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_mimo = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_tx = None
        self.multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_rx = None
        self.multi_domain_capability_performance_profile_parameters = None
        self.multi_domain_capability_performance_profile_parameters_interference_threshold = None
        self.multi_domain_capability_performance_profile_parameters_noise_threshold = None
        self.multi_domain_capability_performance_profile_parameters_rf_utilization_threshold = None
        self.multi_domain_capability_performance_profile_parameters_client_threshold = None
        self.multi_domain_capability_performance_profile_parameters_coverage_exception_level = None
        self.multi_domain_capability_802_11ax_parameters = None
        self.multi_domain_capability_802_11ax_parameters_he_capable = None
        self.multi_domain_capability_cleanair_management_information = None
        self.multi_domain_capability_cleanair_management_information_cleanair_capable = None
        self.multi_domain_capability_cleanair_management_information_cleanair_management_administration_state = None
        self.multi_domain_capability_cleanair_management_information_cleanair_management_operation_state = None
        self.multi_domain_capability_cleanair_management_information_rapid_update_mode = None
        self.multi_domain_capability_cleanair_management_information_spectrum_expert_connections_counter = None
        self.multi_domain_capability_radio_extended_configurations = None
        self.multi_domain_capability_radio_extended_configurations_beacon_period = None
        self.multi_domain_capability_radio_extended_configurations_beacon_range = None
        self.multi_domain_capability_radio_extended_configurations_multicast_buffer = None
        self.multi_domain_capability_radio_extended_configurations_multicast_data_rate = None
        self.multi_domain_capability_radio_extended_configurations_rx_sop_threshold = None
        self.multi_domain_capability_radio_extended_configurations_cca_threshold = None

    def update_name(self):
        if self.ap_name is None and self.station_configuration_bssid is not None and self.slot_id is not None:
            self.name = self.station_configuration_bssid + '_slot' + self.slot_id
        elif self.ap_name is not None and self.slot_id is not None:
            self.name = self.ap_name + '_slot' + self.slot_id #Change name to ap_name when this attribute is available
        else:
            self.name = None

    def __str__(self):
        return 'AP slot config for ' + self.name

    def __repr__(self):
        return 'AP slot config for ' + self.name

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)


class Wlc_Ios_Xe_Config():
    def __init__(self, hostname=None, parsing_date=None, software_version=None, collection_time='None',
                 install_mode=None, subplatform=None):
        self.__wlc_config_version__ = '0.2.0'
        self.__parser_version__ = '0.81'
        self.software_version = software_version
        self.objname = 'WLC IOS XE config'
        self.platform = None  # 9800\AireOS
        self.subplatform = subplatform
        self.install_mode = install_mode
        self.type = 'mixed'  # defines if class contain operational or config data
        self.name = None  # hostname?
        self.parsing_date = parsing_date
        self.collection_time = collection_time
        self.hostname = hostname
        self.ap_configs = NamedList('AP Configs', 'Ap_Config')
        self.ap_slots = NamedList('AP slots', 'AP slot config')
        self.ap_rf_5 = NamedList('AP RF 5GHz Data', 'AP RF 5GHz slot data')
        self.ap_rf_24 = NamedList('AP RF 2.4GHz Data', 'AP RF 2.4GHz slot data')
        self.ssid = NamedList('SSIDs', 'SSID Config')
        self.policy_profiles = NamedList('Policy profiles', 'Policy profile')
        self.ap_join_profiles = NamedList('AP join profiles', 'AP join profile')
        self.flex_profiles = NamedList('Flex profiles', 'Flex Profile')
        self.policy_tags = NamedList('Policy TAGs', 'Policy TAG')
        self.site_tags = NamedList('Site TAGs', 'Site TAG')
        self.rf_tags = NamedList('RF TAGs', 'RF TAG')
        self.rogue_aps = Ewlc_Rogue_Ap_All()
        self.eap = Ewlc_Advanced_Eap()
        self.mobility = Ewlc_Mobility_All()
        self.multicast = Ewlc_Multicast()
        self.https_server = Ewlc_Https_Server()
        self.client_stats = Ewlc_Client_Stats()
        self.svi_interfaces = NamedList('SVI Interfaces',
                                        'SVI_Interface')  # item type should be SVI Interface

    def add_subclass(self, object):
        if isinstance(object, NamedList):  # For Named LIST objects
            if object.item_name == 'Ap_Config': self.ap_configs = object
            if object.item_name == 'SSID Config': self.ssid = object
            if object.item_name == 'SVI_Interface': self.svi_interfaces = object
            if object.item_name == 'AP slot config': self.ap_slots = object
            if object.item_name == 'AP RF 5GHz slot data': self.ap_rf_5 = object
            if object.item_name == 'AP RF 2.4GHz slot data': self.ap_rf_24 = object
            if object.item_name == 'Policy profile': self.policy_profiles = object
            if object.item_name == 'AP join profile': self.ap_join_profiles = object
            if object.item_name == 'Flex Profile': self.flex_profiles = object
            if object.item_name == 'Policy TAG': self.policy_tags = object
            if object.item_name == 'Site TAG': self.site_tags = object
            if object.item_name == 'RF TAG': self.rf_tags = object
            if object.item_name == 'Nearby_Ap':  # special case for nearby APs
                if len(object) > 0:  # Add NearbyAPs only if list is not empty
                    if '0' in object.ap_slot:
                        self.ap_rf_24[object.name].nearby_aps = object
                    elif '1' in object.ap_slot:
                        self.ap_rf_5[object.name].nearby_aps = object
        else:  ##For NON - Named List objects
            if isinstance(object, Ewlc_Rogue_Ap_All): self.rogue_aps = object
            if isinstance(object, Ewlc_Mobility_All): self.mobility = object
            if isinstance(object, Ewlc_Multicast): self.multicast = object
            if isinstance(object, Ewlc_Advanced_Eap): self.eap = object
            if isinstance(object, Ewlc_Https_Server): self.https_server = object
            if isinstance(object, Ewlc_Client_Stats): self.client_stats = object

    def __str__(self):
        return 'WLC config for host: ' + self.hostname + ', platform: ' + self.platform + ', version is ' + self.software_version + ', collection time is ' + self.collection_time + ', parsing date is ' + self.parsing_date

    def __repr__(self):
        return 'WLC config for host: ' + self.hostname + ', platform: ' + self.platform + ', version is ' + self.software_version + ', collection time is ' + self.collection_time + ', parsing date is ' + self.parsing_date

    def show(self):
        show(self)

    def grep(self, keyword):
        grep(self, keyword)

# 9800 PARSING DICTIONARIES SECTION

ewlc_client_stats_parsing_dict = {
    'unique_client_stats_parsing_key': 'unique key is necessary',
    'Total Number of Clients':'total_number_of_clients',
    '802.11b':'protocol_client_count_802_11b',
    '802.11g':'protocol_client_count_802_11g',
    '802.11a':'protocol_client_count_802_11a',
    '802.11n-2.4GHz':'protocol_client_count_802_11n_2_4ghz',
    '802.11n-5 GHz':'protocol_client_count_802_11n_5_ghz',
    '802.11ac':'protocol_client_count_802_11ac',
    '802.11ax-5 GHz':'protocol_client_count_802_11ax_5_ghz',
    '802.11ax-2.4 GHz':'protocol_client_count_802_11ax_2_4_ghz',
    'Authenticating':'current_client_state_statistics_authenticating',
    'Mobility':'current_client_state_statistics_mobility',
    'IP Learn':'current_client_state_statistics_ip_learn',
    'Webauth Pending':'current_client_state_statistics_webauth_pending',
    'Run':'current_client_state_statistics_run',
    'Delete-in-Progress':'current_client_state_statistics_delete_in_progress',
    'Client Summary':'client_summary',
    'Current Clients':'current_clients',
    'Excluded Clients':'excluded_clients',
    'Disabled Clients':'disabled_clients',
    'Foreign Clients':'foreign_clients',
    'Anchor Clients':'anchor_clients',
    'Local Clients':'local_clients',
    'Total association requests received':'total_association_requests_received',
    'Total association attempts':'total_association_attempts',
    'Total FT/LocalAuth requests':'total_ft_localauth_requests',
    'Total association failures':'total_association_failures',
    'Total association response accepts':'total_association_response_accepts',
    'Total association response rejects':'total_association_response_rejects',
    'Total association response errors':'total_association_response_errors',
    'Total association failures due to blacklist':'total_association_failures_due_to_blacklist',
    'Total association drops due to multicast mac':'total_association_drops_due_to_multicast_mac',
    'Total association drops due to throttling':'total_association_drops_due_to_throttling',
    'Total association drops due to unknown bssid':'total_association_drops_due_to_unknown_bssid',
    'Total association drops due to parse failure':'total_association_drops_due_to_parse_failure',
    'Total association drops due to other reasons':'total_association_drops_due_to_other_reasons',
    'Total association requests wired clients':'total_association_requests_wired_clients',
    'Total association drops wired clients':'total_association_drops_wired_clients',
    'Total association success wired clients':'total_association_success_wired_clients',
    'Total peer association requests wired clients':'total_peer_association_requests_wired_clients',
    'Total peer association drops wired clients':'total_peer_association_drops_wired_clients',
    'Total peer association success wired clients':'total_peer_association_success_wired_clients',
    'Total 11r ft authentication requests received':'total_11r_ft_authentication_requests_received',
    'Total 11r ft authentication response success':'total_11r_ft_authentication_response_success',
    'Total 11r ft authentication response failure':'total_11r_ft_authentication_response_failure',
    'Total 11r ft action requests received':'total_11r_ft_action_requests_received',
    'Total 11r ft action response success':'total_11r_ft_action_response_success',
    'Total 11r ft action response failure':'total_11r_ft_action_response_failure',
    'Total AID allocation failures':'total_aid_allocation_failures',
    'Total AID free failures':'total_aid_free_failures',
    'Total roam attempts':'total_roam_attempts',
    'Total CCKM roam attempts':'total_roam_attempts_total_cckm_roam_attempts',
    'Total 11r roam attempts':'total_roam_attempts_total_11r_roam_attempts',
    'Total 11i fast roam attempts':'total_roam_attempts_total_11i_fast_roam_attempts',
    'Total 11i slow roam attempts':'total_roam_attempts_total_11i_slow_roam_attempts',
    'Total other roam type attempts':'total_roam_attempts_total_other_roam_type_attempts',
    'Total roam failures in dot11':'total_roam_failures_in_dot11',
    'Total WPA3 SAE attempts':'total_wpa3_sae_attempts',
    'Total WPA3 SAE successful authentications':'total_wpa3_sae_successful_authentications',
    'Total WPA3 SAE authentication failures':'total_wpa3_sae_authentication_failures',
    'Total incomplete protocol failures':'total_wpa3_sae_authentication_failures_total_incomplete_protocol_failures',
    'Total WPA3 SAE commit messages received':'total_wpa3_sae_commit_messages_received',
    'Total WPA3 SAE commit messages rejected':'total_wpa3_sae_commit_messages_rejected',
    'Total unsupported group rejections':'total_wpa3_sae_commit_messages_rejected_total_unsupported_group_rejections',
    'Total WPA3 SAE commit messages sent':'total_wpa3_sae_commit_messages_sent',
    'Total WPA3 SAE confirm messages received':'total_wpa3_sae_confirm_messages_received',
    'Total WPA3 SAE confirm messages rejected':'total_wpa3_sae_confirm_messages_rejected',
    'Total WPA3 SAE message confirm field mismatch':'total_wpa3_sae_confirm_messages_rejected_total_wpa3_sae_message_confirm_field_mismatch',
    'Total WPA3 SAE confirm message invalid length':'total_wpa3_sae_confirm_messages_rejected_total_wpa3_sae_confirm_message_invalid_length',
    'Total WPA3 SAE confirm messages sent':'total_wpa3_sae_confirm_messages_sent',
    'Total WPA3 SAE Open Sessions':'total_wpa3_sae_open_sessions',
    'Total SAE Message drops due to throttling':'total_sae_message_drops_due_to_throttling',
    'Total Flexconnect local-auth roam attempts':'total_flexconnect_local_auth_roam_attempts',
    'Total AP 11i fast roam attempts':'total_flexconnect_local_auth_roam_attempts_total_ap_11i_fast_roam_attempts',
    'Total 11i slow roam attempts1':'total_flexconnect_local_auth_roam_attempts_total_11i_slow_roam_attempts',
    'Total client state starts':'total_client_state_starts',
    'Total client state associated':'total_client_state_associated',
    'Total client state l2auth success':'total_client_state_l2auth_success',
    'Total client state l2auth failures':'total_client_state_l2auth_failures',
    'Total blacklisted clients on dot1xauth failure':'total_blacklisted_clients_on_dot1xauth_failure',
    'Total client state mab attempts':'total_client_state_mab_attempts',
    'Total client state mab failed':'total_client_state_mab_failed',
    'Total client state ip learn attempts':'total_client_state_ip_learn_attempts',
    'Total client state ip learn failed':'total_client_state_ip_learn_failed',
    'Total client state l3 auth attempts':'total_client_state_l3_auth_attempts',
    'Total client state l3 auth failed':'total_client_state_l3_auth_failed',
    'Total client state session push attempts':'total_client_state_session_push_attempts',
    'Total client state session push failed':'total_client_state_session_push_failed',
    'Total client state run':'total_client_state_run',
    'Total client deleted':'total_client_deleted',
    'Total add mobiles sent':'total_add_mobiles_sent',
    'Total delete mobiles sent':'total_delete_mobiles_sent',
    'Total client deferred delete mobiles':'total_client_deferred_delete_mobiles',
    'Total client deferred delete mobiles sent':'total_client_deferred_delete_mobiles_sent',
    'Total client deferred delete mobile timeouts':'total_client_deferred_delete_mobile_timeouts',
    'Total key exchange attempts':'total_key_exchange_attempts',
    'Total broadcast key exchange attempts':'total_broadcast_key_exchange_attempts',
    'Total broadcast key exchange failures':'total_broadcast_key_exchange_failures',
    'Total eapol key sent':'total_eapol_key_sent',
    'Total eapol key received':'total_eapol_key_received',
    'Total m1 sent':'total_m1_sent',
    'Total m3 sent':'total_m3_sent',
    'Total m5 sent':'total_m5_sent',
    'Total m2 received':'total_m2_received',
    'Total m4 received':'total_m4_received',
    'Total m6 received':'total_m6_received',
    'Total m1 resent':'total_m1_resent',
    'Total m3 resent':'total_m3_resent',
    'Total m5 resent':'total_m5_resent',
    'Total data path client create':'total_data_path_client_create',
    'Total data path client create success':'total_data_path_client_create_success',
    'Total data path client create failed':'total_data_path_client_create_failed',
    'Total data path deplumb client create':'total_data_path_deplumb_client_create',
    'Total data path deplumb client create success':'total_data_path_deplumb_client_create_success',
    'Total data path deplumb client create fail':'total_data_path_deplumb_client_create_fail',
    'Total data path client update':'total_data_path_client_update',
    'Total data path client update success':'total_data_path_client_update_success',
    'Total data path client update failed':'total_data_path_client_update_failed',
    'Total data path client delete':'total_data_path_client_delete',
    'Total data path client delete success':'total_data_path_client_delete_success',
    'Total data path client delete failed':'total_data_path_client_delete_failed',
    'Total data path client nack':'total_data_path_client_nack',
    'Total data path client delete nack':'total_data_path_client_delete_nack',
    'Total data path client unknown nack':'total_data_path_client_unknown_nack',
    'Total DMS requests received in action frame':'total_dms_requests_received_in_action_frame',
    'Total DMS responses sent in action frame':'total_dms_responses_sent_in_action_frame',
    'Total DMS requests received in Re-assoc Request':'total_dms_requests_received_in_re_assoc_request',
    'Associated State':'client_state_statistics_associated_state',
    'L2 State':'client_state_statistics_l2_state',
    'Mobility State':'client_state_statistics_mobility_state',
    'IP Learn State':'client_state_statistics_ip_learn_state',
    'L3 Auth State':'client_state_statistics_l3_auth_state',
    'Average Run State Latency (ms)':'average_run_state_latency_ms',
    'Average Run State Latency without user delay (ms)':'average_run_state_latency_without_user_delay_ms',
    'Latency Distribution (ms)':'latency_distribution_ms',
    '1 - 100':'latency_distribution_ms_1_100',
    '100 - 200':'latency_distribution_ms_100_200',
    '200 - 300':'latency_distribution_ms_200_300',
    '300 - 600':'latency_distribution_ms_300_600',
    '600 - 1000':'latency_distribution_ms_600_1000',
    '1000+':'latency_distribution_ms_1000_plus',
    'Webauth HTTP Statistics':'webauth_http_statistics',
    'Intercepted HTTP requests':'webauth_http_statistics_intercepted_http_requests',
    'IO Read events':'webauth_http_statistics_io_read_events',
    'Received HTTP messages':'webauth_http_statistics_received_http_messages',
    'IO write events':'webauth_http_statistics_io_write_events',
    'Sent HTTP replies':'webauth_http_statistics_sent_http_replies',
    'IO AAA messages':'webauth_http_statistics_io_aaa_messages',
    'SSL OK':'webauth_http_statistics_ssl_ok',
    'SSL Read would block':'webauth_http_statistics_ssl_read_would_block',
    'SSL write would block':'webauth_http_statistics_ssl_write_would_block',
    'Socket opens':'webauth_http_statistics_socket_opens',
    'Socket closes':'webauth_http_statistics_socket_closes',
    'Webauth HTTP status counts':'webauth_http_status_counts',
    'HTTP 200 OK':'webauth_http_status_counts_http_200_ok',
    'HTTP 201 Created':'webauth_http_status_counts_http_201_created',
    'HTTP 202 Accepted':'webauth_http_status_counts_http_202_accepted',
    'HTTP 203 Provisional Info':'webauth_http_status_counts_http_203_provisional_info',
    'HTTP 204 No Content':'webauth_http_status_counts_http_204_no_content',
    'HTTP 300 Multiple Choices':'webauth_http_status_counts_http_300_multiple_choices',
    'HTTP 301 Moved Permanently':'webauth_http_status_counts_http_301_moved_permanently',
    'HTTP 302 Moved Temporarily':'webauth_http_status_counts_http_302_moved_temporarily',
    'HTTP 303 Method':'webauth_http_status_counts_http_303_method',
    'HTTP 304 Not Modified':'webauth_http_status_counts_http_304_not_modified',
    'HTTP 400 Bad Request':'webauth_http_status_counts_http_400_bad_request',
    'HTTP 401 Unauthorized':'webauth_http_status_counts_http_401_unauthorized',
    'HTTP 402 Payment Required':'webauth_http_status_counts_http_402_payment_required',
    'HTTP 403 Forbidden':'webauth_http_status_counts_http_403_forbidden',
    'HTTP 404 Not Found':'webauth_http_status_counts_http_404_not_found',
    'HTTP 405 Method Not Allowed':'webauth_http_status_counts_http_405_method_not_allowed',
    'HTTP 406 None Acceptable':'webauth_http_status_counts_http_406_none_acceptable',
    'HTTP 407 Proxy-Auth Required':'webauth_http_status_counts_http_407_proxy_auth_required',
    'HTTP 408 Request Timeout':'webauth_http_status_counts_http_408_request_timeout',
    'HTTP 409 Conflict':'webauth_http_status_counts_http_409_conflict',
    'HTTP 410 Gone':'webauth_http_status_counts_http_410_gone',
    'HTTP 500 Internal Server Error':'webauth_http_status_counts_http_500_internal_server_error',
    'HTTP 501 Not Implemeneted':'webauth_http_status_counts_http_501_not_implemeneted',
    'HTTP 502 Bad Gateway':'webauth_http_status_counts_http_502_bad_gateway',
    'HTTP 503 Service Unavailable':'webauth_http_status_counts_http_503_service_unavailable',
    'HTTP 504 Gateway Timeout':'webauth_http_status_counts_http_504_gateway_timeout',
    'Webauth queue counters':'webauth_queue_counters',
    'Pending SSL handshakes':'webauth_queue_counters_pending_ssl_handshakes',
    'Pending HTTPS new requests':'webauth_queue_counters_pending_https_new_requests',
    'Pending AAA replies':'webauth_queue_counters_pending_aaa_replies',
    'Delete reasons':'delete_reasons',
    'No Operation':'delete_reasons_no_operation',
    'Unknown':'delete_reasons_unknown',
    'Deauthentication or disassociation request':'delete_reasons_deauthentication_or_disassociation_request',
    'Session Manager':'delete_reasons_session_manager',
    'L3 authentication failure':'delete_reasons_l3_authentication_failure',
    'Delete received from AP':'delete_reasons_delete_received_from_ap',
    'BSSID down':'delete_reasons_bssid_down',
    'AP down/disjoin':'delete_reasons_ap_down_disjoin',
    'Connection timeout':'delete_reasons_connection_timeout',
    'MAC authentication failure':'delete_reasons_mac_authentication_failure',
    'Datapath plumb':'delete_reasons_datapath_plumb',
    'Due to SSID change':'delete_reasons_due_to_ssid_change',
    'Due to VLAN change':'delete_reasons_due_to_vlan_change',
    'Admin deauthentication':'delete_reasons_admin_deauthentication',
    'QoS failure':'delete_reasons_qos_failure',
    'WPA key exchange timeout':'delete_reasons_wpa_key_exchange_timeout',
    'WPA group key update timeout':'delete_reasons_wpa_group_key_update_timeout',
    '802.11w MAX SA queries reached':'delete_reasons_802_11w_max_sa_queries_reached',
    'Client deleted during HA recovery':'delete_reasons_client_deleted_during_ha_recovery',
    'Client blacklist':'delete_reasons_client_blacklist',
    'Inter instance roam failure':'delete_reasons_inter_instance_roam_failure',
    'Due to mobility failure':'delete_reasons_due_to_mobility_failure',
    'Session timeout':'delete_reasons_session_timeout',
    'Idle timeout':'delete_reasons_idle_timeout',
    'Wired idle timeout':'delete_reasons_wired_idle_timeout',
    'Supplicant request':'delete_reasons_supplicant_request',
    'NAS error':'delete_reasons_nas_error',
    'Policy Manager internal error':'delete_reasons_policy_manager_internal_error',
    'Mobility WLAN down':'delete_reasons_mobility_wlan_down',
    'Mobility tunnel down':'delete_reasons_mobility_tunnel_down',
    '80211v smart roam failed':'delete_reasons_80211v_smart_roam_failed',
    'DOT11v timer timeout':'delete_reasons_dot11v_timer_timeout',
    'DOT11v association failed':'delete_reasons_dot11v_association_failed',
    'DOT11r pre-authentication failure':'delete_reasons_dot11r_pre_authentication_failure',
    'SAE authentication failure':'delete_reasons_sae_authentication_failure',
    'SAE Commit received in Associated State':'delete_reasons_sae_commit_received_in_associated_state',
    'DOT11 failure':'delete_reasons_dot11_failure',
    'DOT11 SAE invalid message':'delete_reasons_dot11_sae_invalid_message',
    'DOT11 unsupported client capabilities':'delete_reasons_dot11_unsupported_client_capabilities',
    'DOT11 association denied unspecified':'delete_reasons_dot11_association_denied_unspecified',
    'DOT11 max STA':'delete_reasons_dot11_max_sta',
    'DOT11 denied data rates':'delete_reasons_dot11_denied_data_rates',
    '802.11v Client RSSI lower than the association RSSI threshold':'delete_reasons_802_11v_client_rssi_lower_than_the_association_rssi_threshold',
    'invalid QoS parameter':'delete_reasons_invalid_qos_parameter',
    'DOT11 IE validation failed':'delete_reasons_dot11_ie_validation_failed',
    'DOT11 group cipher in IE validation failed':'delete_reasons_dot11_group_cipher_in_ie_validation_failed',
    'DOT11 invalid pairwise cipher':'delete_reasons_dot11_invalid_pairwise_cipher',
    'DOT11 invalid AKM':'delete_reasons_dot11_invalid_akm',
    'DOT11 unsupported RSN version':'delete_reasons_dot11_unsupported_rsn_version',
    'DOT11 invalid RSNIE capabilities':'delete_reasons_dot11_invalid_rsnie_capabilities',
    'DOT11 received invalid PMKID in the received RSN IE':'delete_reasons_dot11_received_invalid_pmkid_in_the_received_rsn_ie',
    'DOT11 invalid MDIE':'delete_reasons_dot11_invalid_mdie',
    'DOT11 invalid FT IE':'delete_reasons_dot11_invalid_ft_ie',
    'DOT11 QoS policy':'delete_reasons_dot11_qos_policy',
    'DOT11 AP have insufficient bandwidth':'delete_reasons_dot11_ap_have_insufficient_bandwidth',
    'DOT11 invalid QoS parameter':'delete_reasons_dot11_invalid_qos_parameter',
    'Client not allowed by assisted roaming':'delete_reasons_client_not_allowed_by_assisted_roaming',
    'IAPP disassociation for wired client':'delete_reasons_iapp_disassociation_for_wired_client',
    'Wired WGB change':'delete_reasons_wired_wgb_change',
    'Wired VLAN change':'delete_reasons_wired_vlan_change',
    'Wired client deleted due to WGB delete':'delete_reasons_wired_client_deleted_due_to_wgb_delete',
    'AVC client re-anchored at the foreign controller':'delete_reasons_avc_client_re_anchored_at_the_foreign_controller',
    'WGB Wired client joins as a direct wireless client':'delete_reasons_wgb_wired_client_joins_as_a_direct_wireless_client',
    'AP upgrade':'delete_reasons_ap_upgrade',
    'Client DHCP':'delete_reasons_client_dhcp',
    'Client EAP timeout':'delete_reasons_client_eap_timeout',
    'Client 8021x failure':'delete_reasons_client_8021x_failure',
    'Client device idle':'delete_reasons_client_device_idle',
    'Client captive portal security failure':'delete_reasons_client_captive_portal_security_failure',
    'Client decryption failure':'delete_reasons_client_decryption_failure',
    'Client interface disabled':'delete_reasons_client_interface_disabled',
    'Client user triggered disassociation':'delete_reasons_client_user_triggered_disassociation',
    'Client miscellaneous reason':'delete_reasons_client_miscellaneous_reason',
    'Unknown1':'delete_reasons_unknown',
    'Client peer triggered':'delete_reasons_client_peer_triggered',
    'Client beacon loss':'delete_reasons_client_beacon_loss',
    'Client EAP ID timeout':'delete_reasons_client_eap_id_timeout',
    'Client DOT1x timeout':'delete_reasons_client_dot1x_timeout',
    'Malformed EAP key frame':'delete_reasons_malformed_eap_key_frame',
    'EAP key install bit is not expected':'delete_reasons_eap_key_install_bit_is_not_expected',
    'EAP key error bit is not expected':'delete_reasons_eap_key_error_bit_is_not_expected',
    'EAP key ACK bit is not expected':'delete_reasons_eap_key_ack_bit_is_not_expected',
    'Invalid key type':'delete_reasons_invalid_key_type',
    'EAP key secure bit is not expected':'delete_reasons_eap_key_secure_bit_is_not_expected',
    'key description version mismatch':'delete_reasons_key_description_version_mismatch',
    'wrong replay counter':'delete_reasons_wrong_replay_counter',
    'EAP key MIC bit expected':'delete_reasons_eap_key_mic_bit_expected',
    'MIC validation failed':'delete_reasons_mic_validation_failed',
    'Error while PTK computation':'delete_reasons_error_while_ptk_computation',
    'Incorrect credentials':'delete_reasons_incorrect_credentials',
    'Client connection lost':'delete_reasons_client_connection_lost',
    'Reauthentication failure':'delete_reasons_reauthentication_failure',
    'Port admin disabled':'delete_reasons_port_admin_disabled',
    'Supplicant restart':'delete_reasons_supplicant_restart',
    'No IP':'delete_reasons_no_ip',
    'Call admission controller at anchor node':'delete_reasons_call_admission_controller_at_anchor_node',
    'Anchor no memory':'delete_reasons_anchor_no_memory',
    'Anchor invalid Mobility BSSID':'delete_reasons_anchor_invalid_mobility_bssid',
    'Anchor creation failure':'delete_reasons_anchor_creation_failure',
    'DB error':'delete_reasons_db_error',
    'Wired client cleanup due to WGB roaming':'delete_reasons_wired_client_cleanup_due_to_wgb_roaming',
    'Manually excluded':'delete_reasons_manually_excluded',
    '802.11 association failure':'delete_reasons_802_11_association_failure',
    '802.11 authentication failure':'delete_reasons_802_11_authentication_failure',
    '802.1X authentication timeout':'delete_reasons_802_1x_authentication_timeout',
    '802.1X authentication credential failure':'delete_reasons_802_1x_authentication_credential_failure',
    'Web authentication failure':'delete_reasons_web_authentication_failure',
    'Policy bind failure':'delete_reasons_policy_bind_failure',
    'IP theft':'delete_reasons_ip_theft',
    'MAC theft':'delete_reasons_mac_theft',
    'MAC and IP theft':'delete_reasons_mac_and_ip_theft',
    'QoS policy failure':'delete_reasons_qos_policy_failure',
    'QoS policy send to AP failure':'delete_reasons_qos_policy_send_to_ap_failure',
    'QoS policy bind on AP failure':'delete_reasons_qos_policy_bind_on_ap_failure',
    'QoS policy unbind on AP failure':'delete_reasons_qos_policy_unbind_on_ap_failure',
    'Static IP anchor discovery failure':'delete_reasons_static_ip_anchor_discovery_failure',
    'VLAN failure':'delete_reasons_vlan_failure',
    'ACL failure':'delete_reasons_acl_failure',
    'Redirect ACL failure':'delete_reasons_redirect_acl_failure',
    'Accounting failure':'delete_reasons_accounting_failure',
    'Security group tag failure':'delete_reasons_security_group_tag_failure',
    'FQDN filter definition does not exist':'delete_reasons_fqdn_filter_definition_does_not_exist',
    'Wrong filter type, expected postauth FQDN filter':'delete_reasons_wrong_filter_type_expected_postauth_fqdn_filter',
    'Wrong filter type, expected preauth FQDN filter':'delete_reasons_wrong_filter_type_expected_preauth_fqdn_filter',
    'Invalid group id for FQDN filter valid range  1..16':'delete_reasons_invalid_group_id_for_fqdn_filter_valid_range_1_16',
    'Policy parameter mismatch':'delete_reasons_policy_parameter_mismatch',
    'Reauth failure':'delete_reasons_reauth_failure',
    'Wrong PSK':'delete_reasons_wrong_psk',
    'Policy failure':'delete_reasons_policy_failure',
    'AP initiated delete for idle timeout':'delete_reasons_ap_initiated_delete_for_idle_timeout',
    'AP initiated delete for client ACL mismatch':'delete_reasons_ap_initiated_delete_for_client_acl_mismatch',
    'AP initiated delete for AP auth stop':'delete_reasons_ap_initiated_delete_for_ap_auth_stop',
    'AP initiated delete for association expired at AP':'delete_reasons_ap_initiated_delete_for_association_expired_at_ap',
    'AP initiated delete for 4-way handshake failed':'delete_reasons_ap_initiated_delete_for_4_way_handshake_failed',
    'AP initiated delete for DHCP timeout':'delete_reasons_ap_initiated_delete_for_dhcp_timeout',
    'AP initiated delete for reassociation timeout':'delete_reasons_ap_initiated_delete_for_reassociation_timeout',
    'AP initiated delete for SA query timeout':'delete_reasons_ap_initiated_delete_for_sa_query_timeout',
    'AP initiated delete for intra AP roam':'delete_reasons_ap_initiated_delete_for_intra_ap_roam',
    'AP initiated delete for channel switch at AP':'delete_reasons_ap_initiated_delete_for_channel_switch_at_ap',
    'AP initiated delete for bad AID':'delete_reasons_ap_initiated_delete_for_bad_aid',
    'AP initiated delete for request':'delete_reasons_ap_initiated_delete_for_request',
    'AP initiated delete for interface reset':'delete_reasons_ap_initiated_delete_for_interface_reset',
    'AP initiated delete for all on slot':'delete_reasons_ap_initiated_delete_for_all_on_slot',
    'AP initiated delete for reaper radio':'delete_reasons_ap_initiated_delete_for_reaper_radio',
    'AP initiated delete for slot disable':'delete_reasons_ap_initiated_delete_for_slot_disable',
    'AP initiated delete for MIC failure':'delete_reasons_ap_initiated_delete_for_mic_failure',
    'AP initiated delete for VLAN delete':'delete_reasons_ap_initiated_delete_for_vlan_delete',
    'AP initiated delete for channel change':'delete_reasons_ap_initiated_delete_for_channel_change',
    'AP initiated delete for stop reassociation':'delete_reasons_ap_initiated_delete_for_stop_reassociation',
    'AP initiated delete for packet max retry':'delete_reasons_ap_initiated_delete_for_packet_max_retry',
    'AP initiated delete for transmission deauth':'delete_reasons_ap_initiated_delete_for_transmission_deauth',
    'AP initiated delete for sensor station timeout':'delete_reasons_ap_initiated_delete_for_sensor_station_timeout',
    'AP initiated delete for age timeout':'delete_reasons_ap_initiated_delete_for_age_timeout',
    'AP initiated delete for transmission fail threshold':'delete_reasons_ap_initiated_delete_for_transmission_fail_threshold',
    'AP initiated delete for uplink receive timeout':'delete_reasons_ap_initiated_delete_for_uplink_receive_timeout',
    'AP initiated delete for sensor scan next radio':'delete_reasons_ap_initiated_delete_for_sensor_scan_next_radio',
    'AP initiated delete for sensor scan other BSSID':'delete_reasons_ap_initiated_delete_for_sensor_scan_other_bssid',
    'AAA server unavailable':'delete_reasons_aaa_server_unavailable',
    'AAA server not ready':'delete_reasons_aaa_server_not_ready',
    'No dot1x method configuration':'delete_reasons_no_dot1x_method_configuration',
    'Client Abort':'delete_reasons_client_abort',
    'Association connection timeout':'delete_reasons_association_connection_timeout',
    'MAC-AUTH connection timeout':'delete_reasons_mac_auth_connection_timeout',
    'L2-AUTH connection timeout':'delete_reasons_l2_auth_connection_timeout',
    'L3-AUTH connection timeout':'delete_reasons_l3_auth_connection_timeout',
    'Mobility connection timeout':'delete_reasons_mobility_connection_timeout',
    'static IP connection timeout':'delete_reasons_static_ip_connection_timeout',
    'SM session creation timeout':'delete_reasons_sm_session_creation_timeout',
    'IP-LEARN connection timeout':'delete_reasons_ip_learn_connection_timeout',
    'NACK IFID exists':'delete_reasons_nack_ifid_exists',
    'Radio Down':'delete_reasons_radio_down',
    'Guest-LAN invalid MBSSID':'delete_reasons_guest_lan_invalid_mbssid',
    'Guest-LAN no memory':'delete_reasons_guest_lan_no_memory',
    'Guest-LAN ceate request failed':'delete_reasons_guest_lan_ceate_request_failed',
    'EoGRE Reset':'delete_reasons_eogre_reset',
    'EoGRE Generic Join Failure':'delete_reasons_eogre_generic_join_failure',
    'EoGRE HA-Reconciliation':'delete_reasons_eogre_ha_reconciliation',
    'EoGRE Invalid VLAN':'delete_reasons_eogre_invalid_vlan',
    'EoGRE Invalid Domain':'delete_reasons_eogre_invalid_domain',
    'EoGRE Empty Domain':'delete_reasons_eogre_empty_domain',
    'EoGRE Domain Shut':'delete_reasons_eogre_domain_shut',
    'EoGRE Invalid Gateway':'delete_reasons_eogre_invalid_gateway',
    'EoGRE All Gateways down':'delete_reasons_eogre_all_gateways_down',
    'EoGRE Flex - no active gateway':'delete_reasons_eogre_flex_no_active_gateway',
    'EoGRE Rule Matching error':'delete_reasons_eogre_rule_matching_error',
    'EoGRE AAA Override error':'delete_reasons_eogre_aaa_override_error',
    'EoGRE client onboarding error':'delete_reasons_eogre_client_onboarding_error',
    'EoGRE Mobility Handoff error':'delete_reasons_eogre_mobility_handoff_error',
    'IP Update timeout':'delete_reasons_ip_update_timeout',
    'Mobility peer delete':'delete_reasons_mobility_peer_delete',
    'NACK IFID mismatch':'delete_reasons_nack_ifid_mismatch',
}

ewlc_http_server_parsing_dict = {
    'unique_https_server_parsing_key': 'unique key is necessary',
    'HTTP server status': 'http_server_status',
    'HTTP server port': 'http_server_port',
    'HTTP server active supplementary listener ports': 'http_server_active_supplementary_listener_ports',
    'HTTP server authentication method': 'http_server_authentication_method',
    'HTTP server auth-retry 0 time-window 0': 'http_server_auth_retry_0_time_window_0',
    'HTTP server digest algorithm': 'http_server_digest_algorithm',
    'HTTP server access class': 'http_server_access_class',
    'HTTP server IPv4 access class': 'http_server_ipv4_access_class',
    'HTTP server IPv6 access class': 'http_server_ipv6_access_class',
    'HTTP server base path': 'http_server_base_path',
    'HTTP File Upload status': 'http_file_upload_status',
    'HTTP server upload path': 'http_server_upload_path',
    'HTTP server help root': 'http_server_help_root',
    'Maximum number of concurrent server connections allowed': 'maximum_number_of_concurrent_server_connections_allowed',
    'Maximum number of secondary server connections allowed': 'maximum_number_of_secondary_server_connections_allowed',
    'Server idle time-out': 'server_idle_time_out',
    'Server life time-out': 'server_life_time_out',
    'Server session idle time-out': 'server_session_idle_time_out',
    'Maximum number of requests allowed on a connection': 'maximum_number_of_requests_allowed_on_a_connection',
    'Server linger time': 'server_linger_time',
    'HTTP server active session modules': 'http_server_active_session_modules',
    'HTTP secure server capability': 'http_secure_server_capability',
    'HTTP secure server status': 'http_secure_server_status',
    'HTTP secure server port': 'http_secure_server_port',
    'HTTP secure server ciphersuite': 'http_secure_server_ciphersuite',
    'HTTP secure server TLS version': 'http_secure_server_tls_version',
    'HTTP secure server client authentication': 'http_secure_server_client_authentication',
    'HTTP secure server PIV authentication': 'http_secure_server_piv_authentication',
    'HTTP secure server PIV authorization only': 'http_secure_server_piv_authorization_only',
    'HTTP secure server trustpoint': 'http_secure_server_trustpoint',
    'HTTP secure server peer validation trustpoint': 'http_secure_server_peer_validation_trustpoint',
    'HTTP secure server ECDHE curve': 'http_secure_server_ecdhe_curve',
    'HTTP secure server active session modules': 'http_secure_server_active_session_modules',
}

ewlc_multicast_parsing_dict = {
    'unique_multicast_parsing_key': 'unique key is necessary',
    'Multicast':'multicast',
    'AP Capwap Multicast':'ap_capwap_multicast',
    'AP Capwap IPv4 Multicast group Address':'ap_capwap_ipv4_multicast_group_address',
    'AP Capwap IPv6 Multicast group Address':'ap_capwap_ipv6_multicast_group_address',
    'Wireless Broadcast':'wireless_broadcast',
    'Wireless Multicast non-ip-mcast':'wireless_multicast_non_ip_mcast',
}

ewlc_mobility_parsing_dict = {
    'unique_mobility_parsing_key': 'unique key is necessary',
    'Wireless Management VLAN':'wireless_management_vlan',
    'Wireless Management IP Address':'wireless_management_ip_address',
    'Wireless Management IPv6 Address':'wireless_management_ipv6_address',
    'Mobility Control Message DSCP Value':'mobility_control_message_dscp_value',
    'Mobility Keepalive Interval/Count':'mobility_keepalive_interval_count',
    'Mobility Group Name':'mobility_group_name',
    'Mobility Multicast Ipv4 address':'mobility_multicast_ipv4_address',
    'Mobility Multicast Ipv6 address':'mobility_multicast_ipv6_address',
    'Mobility MAC Address':'mobility_mac_address',
    'Controllers configured in the Mobility Domain': {
        'attribute_name': 'mobility_members',
        'end_table_string': 'dummy',
        'list_name': 'Mobility members',
        'item_name': 'Mobility member',
        'item_class_name': Ewlc_Mobility_Member},
}

ewlc_advanced_eap_parsing_dict = {
    'unique_eap_timers_parsing_key': 'unique key is necessary',
    'EAP-Identity-Request Timeout (seconds)':'eap_identity_request_timeout_seconds',
    'EAP-Identity-Request Max Retries':'eap_identity_request_max_retries',
    'EAP Max-Login Ignore Identity Response':'eap_max_login_ignore_identity_response',
    'EAP-Request Timeout (seconds)':'eap_request_timeout_seconds',
    'EAP-Request Max Retries':'eap_request_max_retries',
    'EAPOL-Key Timeout (milliseconds)':'eapol_key_timeout_milliseconds',
    'EAPOL-Key Max Retries':'eapol_key_max_retries',
    'EAP-Broadcast Key Interval':'eap_broadcast_key_interval',
}

ewlc_rf_tag_parsing_dict = {
    'unique_rf_tag_parsing_key': 'unique key is necessary',
    'Tag Name':'tag_name',
    'Description':'description',
    '5ghz RF Policy':'rf_policy_5ghz',
    '2.4ghz RF Policy':'rf_policy_24ghz',
}

ewlc_site_tag_parsing_dict = {
    'unique_site_tag_parsing_key': 'unique key is necessary',
    'Site Tag Name':'site_tag_name',
    'Description':'description',
    'Flex Profile':'flex_profile',
    'AP Profile':'ap_profile',
    'Local-site':'local_site',
    'Fabric Control-Plane':'fabric_control_plane',
    'Image Download Profile':'image_download_profile',
}

ewlc_policy_tag_parsing_dict = {
    'unique_policy_tag_parsing_key': 'unique key is necessary',
    'Policy Tag Name':'policy_tag_name',
    'Description':'description',

    'Number of WLAN-POLICY maps':{
        'attribute_name':'wlan_policy_mappings',
        'end_table_string':'Number of RLAN-POLICY maps',
        'list_name':'WLAN-policy mappings',
        'item_name':'WLAN-policy mapping',
        'item_class_name': Ewlc_Wlan_Policy_Mapping}, #example for table parsing
    'Number of RLAN-POLICY maps':{
        'attribute_name':'rlan_policy_mappings',
        'end_table_string':'dummy',
        'list_name':'Remote-LAN-policy mappings',
        'item_name':'Remote-LAN-policy mapping',
        'item_class_name': Ewlc_Rlan_Policy_Mapping},
}

ewlc_rogue_ap_parsing_dict = {
    'unique_rogue_ap_parsing_key': 'unique key is necessary',
    'Total Number of Rogue APs':{'attribute_name':'rogue_aps_list','end_table_string':'dummy','list_name':'Rogue APs','item_name':'Rogue AP','item_class_name': Ewlc_Rogue_Ap}, #example for table parsing
    'Rogue Location Discovery Protocol':'rogue_location_discovery_protocol',
    'Validate rogue APs against AAA':'validate_rogue_aps_against_aaa',
    'Rogue Security Level':'rogue_security_level',
    'Rogue on wire Auto-Contain':'rogue_on_wire_auto_contain',
    'Rogue using our SSID Auto-Contain':'rogue_using_our_ssid_auto_contain',
    'Valid client on rogue AP Auto-Contain':'valid_client_on_rogue_ap_auto_contain',
    'Rogue AP timeout':'rogue_ap_timeout',
    'Default Rogue Detection Report Interval':'default_rogue_detection_report_interval',
    'Default Rogue AP minimum RSSI':'default_rogue_ap_minimum_rssi',
    'Default Rogue AP minimum transient time':'default_rogue_ap_minimum_transient_time',
}
ewlc_flex_profile_parsing_dict = {
    'unique_flex_profile_config_key': 'unique key is necessary',
    'Flex Profile Name':'flex_profile_name',
    'Description':'description',
    'Local Auth':'local_auth',
    'Radius Enable':'local_auth_radius_enable',
    'PEAP':'local_auth_peap',
    'LEAP':'local_auth_leap',
    'TLS':'local_auth_tls',
    'EAP fast profile':'local_auth_eap_fast_profile',
    'User List':'local_auth_user_list',
    'RADIUS:':'radius',
    'RADIUS server group name':'radius_radius_server_group_name',
    'Fallback Radio shut':'fallback_radio_shut',
    'ARP caching':'arp_caching',
    'Efficient Image Upgrade':'efficient_image_upgrade',
    'OfficeExtend AP':'officeextend_ap',
    'Join min latency':'join_min_latency',
    'Policy ACL':'policy_acl',
    'VLAN Name - VLAN ID mapping':{'attribute_name':'vlan_mappings','end_table_string':'HTTP-Proxy','list_name':'Flex VLAN mappings','item_name':'Flex VLAN mapping','item_class_name': Ewlc_Flex_Vlan_Mapping}, #example for table parsing
    'HTTP-Proxy IP Address':'http_proxy_ip_address',
    'HTTP-Proxy Port':'http_proxy_port',
    'Native vlan ID':'native_vlan_id',
    'Flex resilient':'flex_resilient',
    'CTS Policy:':'cts_policy',
    'Inline tagging':'cts_policy_inline_tagging',
    'SGACL enforcement':'cts_policy_sgacl_enforcement',
    'CTS Profile Name':'cts_policy_cts_profile_name',
}

ewlc_ap_profile_parsing_dict = {
    'unique_ap_join_profile_config_key':'unique key is needed',
    'AP Profile Name':'ap_profile_name',
    'Description':'description',
    'Stats Timer':'stats_timer',
    'Link Latency':'link_latency',
    'Data Encryption':'data_encryption',
    'LED State':'led_state',
    'NTP server':'ntp_server',
    'Jumbo MTU':'jumbo_mtu',
    '24ghz Report Interval':'d_24ghz_report_interval',
    '5ghz Report Interval':'d_5ghz_report_interval',
    'bssid stats status':'bssid_stats_status',
    'bssid stats frqncy interval':'bssid_stats_frqncy_interval',
    'bssid neighbor stats status':'bssid_neighbor_stats_status',
    'bssid neighbor stats interval':'bssid_neighbor_stats_interval',
    'POE config:':'poe_config',
    'PreStandard 802.3af Switch':'poe_config_prestandard_802_3af_switch',
    'Power Injector State':'poe_config_power_injector_state',
    'Power Injector Selection':'poe_config_power_injector_selection',
    'Injector Switch Mac':'poe_config_injector_switch_mac',
    'Device Management':'device_management',
    'Telnet':'device_management_telnet',
    'SSH':'device_management_ssh',
    'User Management':'user_management',
    'Username':'user_management_username',
    'TCP MSS':'tcp_mss',
    'Adjust MSS':'tcp_mss_adjust_mss',
    'TCP Adjust MSS':'tcp_mss_tcp_adjust_mss',
    'CAPWAP Timer':'capwap_timer',
    'Heartbeat Timeout':'capwap_timer_heartbeat_timeout',
    'Discovery Timeout':'capwap_timer_discovery_timeout',
    'Fast Heartbeat Timeout':'capwap_timer_fast_heartbeat_timeout',
    'Primary Discovery Timeout':'capwap_timer_primary_discovery_timeout',
    'Primed Join Timeout':'capwap_timer_primed_join_timeout',
    'Retransmit Timer':'retransmit_timer',
    'Count':'retransmit_timer_count',
    'Interval':'retransmit_timer_interval',
    'Login Credentials':'login_credentials',
    'Local Username':'login_credentials_local_username',
    'Dot1x Username':'login_credentials_dot1x_username',
    'Ap eap auth info':'ap_eap_auth_info',
    'Dot1x EAP Method':'ap_eap_auth_info_dot1x_eap_method',
    'LSC AP AUTH STATE':'ap_eap_auth_info_lsc_ap_auth_state',
    'Syslog':'syslog',
    'Facility Value':'syslog_facility_value',
    'Host':'syslog_host',
    'Log Level':'syslog_log_level',
    'Backup Controllers':'backup_controllers',
    'Fallback':'backup_controllers_fallback',
    'Primary Backup Name':'backup_controllers_primary_backup_name',
    'Primary Backup IP':'backup_controllers_primary_backup_ip',
    'Secondary Backup Name':'backup_controllers_secondary_backup_name',
    'Secondary Backup IP':'backup_controllers_secondary_backup_ip',
    'Hyperlocation':'hyperlocation',
    'Admin State':'hyperlocation_admin_state',
    'PAK RSSI Threshold Detection':'hyperlocation_pak_rssi_threshold_detection',
    'PAK RSSI Threshold Trigger':'hyperlocation_pak_rssi_threshold_trigger',
    'PAK RSSI Threshold Reset':'hyperlocation_pak_rssi_threshold_reset',
    'Halo BLE Beacon':'halo_ble_beacon',
    'Interval1':'halo_ble_beacon_interval',
    'TX Power':'halo_ble_beacon_tx_power',
    'Enabled':'halo_ble_beacon_enabled',
    'Apply Global':'halo_ble_beacon_apply_global',
    'Group NAS Id':'group_nas_id',
    'CDP':'cdp',
    'TFTP Downgrade':'tftp_downgrade',
    'IP Address':'tftp_downgrade_ip_address',
    'Filename':'tftp_downgrade_filename',
    'Time Limit':'time_limit',
    'Capwap window size':'capwap_window_size',
    'AP packet capture profile':'ap_packet_capture_profile',
    'AP trace profile':'ap_trace_profile',
    'Mesh profile name':'mesh_profile_name',
    'Method-list  name':'method_list_name',
    'Packet Sequence Jump DELBA':'packet_sequence_jump_delba',
    'Lag status':'lag_status',
    'Extended Module':'extended_module',
    'USB Module':'usb_module',
    'Persistent SSID Broadcast':'persistent_ssid_broadcast',
    'DHCP server':'dhcp_server',
    'Preferred Mode':'preferred_mode',
    'CAPWAP UDP-Lite':'capwap_udp_lite',
    'AWIPS':'awips',
    'Fallback to DHCP':'fallback_to_dhcp',
    'Client RSSI Statistics':'client_rssi_statistics',
    'Reporting':'client_rssi_statistics_reporting',
    'Reporting Interval':'client_rssi_statistics_reporting_interval',
    'Traffic Distribution Stats':'traffic_distribution_stats',
    'Traffic Distribution Stats Interval(sec)':'traffic_distribution_stats_interval_sec',
    'OEAP Mode Config':'oeap_mode_config',
    'Link Encryption':'oeap_mode_config_link_encryption',
    'Rogue Detection':'oeap_mode_config_rogue_detection',
    'Local Access':'oeap_mode_config_local_access',
}
ewlc_policy_profile_parsing_dict = {
    'unique_policy_profile_config_key':'unique key is needed',
    'Policy Profile Name':'policy_profile_name',
    'Description':'description',
    'Status':'status',
    'VLAN':'vlan',
    'Multicast VLAN':'multicast_vlan',
    'OSEN client VLAN':'osen_client_vlan',
    'Multicast Filter':'multicast_filter',
    'QBSS Load':'qbss_load',
    'Passive Client':'passive_client',
    'ET-Analytics':'et_analytics',
    'StaticIP Mobility':'staticip_mobility',
    'WLAN Switching Policy':'wlan_switching_policy',
    'Flex Central Switching':'wlan_switching_policy_flex_central_switching',
    'Flex Central Authentication':'wlan_switching_policy_flex_central_authentication',
    'Flex Central DHCP':'wlan_switching_policy_flex_central_dhcp',
    'Flex NAT PAT':'wlan_switching_policy_flex_nat_pat',
    'Flex Central Assoc':'wlan_switching_policy_flex_central_assoc',
    'WLAN Flex Policy':'wlan_flex_policy',
    'VLAN based Central Switching':'wlan_flex_policy_vlan_based_central_switching',
    'WLAN ACL':'wlan_acl',
    'IPv4 ACL':'wlan_acl_ipv4_acl',
    'IPv6 ACL':'wlan_acl_ipv6_acl',
    'Layer2 ACL':'wlan_acl_layer2_acl',
    'Preauth urlfilter list':'wlan_acl_preauth_urlfilter_list',
    'Postauth urlfilter list':'wlan_acl_postauth_urlfilter_list',
    'WLAN Timeout':'wlan_timeout',
    'Session Timeout':'wlan_timeout_session_timeout',
    'Idle Timeout':'wlan_timeout_idle_timeout',
    'Idle Threshold':'wlan_timeout_idle_threshold',
    'Guest LAN Session Timeout':'wlan_timeout_guest_lan_session_timeout',
    'WLAN Local Profiling':'wlan_local_profiling',
    'Subscriber Policy Name':'wlan_local_profiling_subscriber_policy_name',
    'RADIUS Profiling':'wlan_local_profiling_radius_profiling',
    'HTTP TLV caching':'wlan_local_profiling_http_tlv_caching',
    'DHCP TLV caching':'wlan_local_profiling_dhcp_tlv_caching',
    'CTS Policy':'cts_policy',
    'Inline Tagging':'cts_policy_inline_tagging',
    'SGACL Enforcement':'cts_policy_sgacl_enforcement',
    'Default SGT':'cts_policy_default_sgt',
    'WLAN Mobility':'wlan_mobility',
    'Anchor':'wlan_mobility_anchor',
    'AVC VISIBILITY':'avc_visibility',
    'IPv4 Flow Monitors':'ipv4_flow_monitors',
    'Ingress':'ipv4_flow_monitors_ingress',
    'wireless-avc-basic':'ipv4_flow_monitors_ingress_wireless_avc_basic',
    'Egress':'ipv4_flow_monitors_egress',
    'wireless-avc-basic1':'ipv4_flow_monitors_egress_wireless_avc_basic',
    'IPv6 Flow Monitors':'ipv6_flow_monitors',
    'Ingress1':'ipv6_flow_monitors_ingress',
    'Egress1':'ipv6_flow_monitors_egress',
    'NBAR Protocol Discovery':'nbar_protocol_discovery',
    'Reanchoring':'reanchoring',
    'Classmap name for Reanchoring':'classmap_name_for_reanchoring',
    'Reanchoring Classmap Name':'classmap_name_for_reanchoring_reanchoring_classmap_name',
    'QOS per SSID':'qos_per_ssid',
    'Ingress Service Name':'qos_per_ssid_ingress_service_name',
    'Egress Service Name':'qos_per_ssid_egress_service_name',
    'QOS per Client':'qos_per_client',
    'Ingress Service Name1':'qos_per_client_ingress_service_name',
    'Egress Service Name1':'qos_per_client_egress_service_name',
    'Umbrella information':'umbrella_information',
    'Cisco Umbrella Parameter Map':'umbrella_information_cisco_umbrella_parameter_map',
    'DHCP DNS Option':'umbrella_information_dhcp_dns_option',
    'Mode':'umbrella_information_mode',
    'Autoqos Mode':'autoqos_mode',
    'Call Snooping':'call_snooping',
    'Tunnel Profile':'tunnel_profile',
    'Profile Name':'tunnel_profile_profile_name',
    'Calendar Profile':'calendar_profile',
    'Fabric Profile':'fabric_profile',
    'Profile Name1':'fabric_profile_profile_name',
    'Accounting list':'accounting_list',
    'Accounting List':'accounting_list_accounting_list',
    'required':'accounting_list_required',
    'server address':'accounting_list_server_address',
    'Opt82':'opt82',
    'DhcpOpt82Enable':'opt82_dhcpopt82enable',
    'DhcpOpt82Ascii':'opt82_dhcpopt82ascii',
    'DhcpOpt82Rid':'opt82_dhcpopt82rid',
    'APMAC':'opt82_apmac',
    'SSID':'opt82_ssid',
    'AP_ETHMAC':'opt82_ap_ethmac',
    'APNAME':'opt82_apname',
    'POLICY TAG':'opt82_policy_tag',
    'AP_LOCATION':'opt82_ap_location',
    'VLAN_ID':'opt82_vlan_id',
    'Exclusionlist Params':'exclusionlist_params',
    'Exclusionlist':'exclusionlist_params_exclusionlist',
    'Exclusion Timeout':'exclusionlist_params_exclusion_timeout',
    'AAA Policy Params':'aaa_policy_params',
    'AAA Override':'aaa_policy_params_aaa_override',
    'NAC':'aaa_policy_params_nac',
    'AAA Policy name':'aaa_policy_params_aaa_policy_name',
    'WGB Policy Params':'wgb_policy_params',
    'Broadcast Tagging':'wgb_policy_params_broadcast_tagging',
    'Client VLAN':'wgb_policy_params_client_vlan',
    'Hotspot 2.0 Server name':'hotspot_2_0_server_name',
    'Mobility Anchor List':'mobility_anchor_list',
    'mDNS Gateway':'mdns_gateway',
    'mDNS Service Policy name':'mdns_gateway_mdns_service_policy_name',
    'User Defined (Private) Network':'user_defined_private_network',
    'User Defined (Private) Network Unicast Drop':'user_defined_private_network_unicast_drop',
    'Policy Proxy Settings':'policy_proxy_settings',
    'ARP Proxy State':'policy_proxy_settings_arp_proxy_state',
    'IPv6 Proxy State':'policy_proxy_settings_ipv6_proxy_state',
    'Airtime-fairness Profile':'airtime_fairness_profile',
    '2.4Ghz ATF Policy':'airtime_fairness_profile_2_4ghz_atf_policy',
    '5Ghz ATF Policy':'airtime_fairness_profile_5ghz_atf_policy',
}

ewlc_ssid_parsing_dict = {
    'unique_ssid_config_key':'unique key is needed',
    'WLAN Profile Name':'wlan_profile_name',
    'Identifier':'identifier',
    'Description':'description',
    'Network Name (SSID)':'network_name_ssid',
    'Status':'status',
    'Broadcast SSID':'broadcast_ssid',
    'Advertise-Apname':'advertise_apname',
    'Universal AP Admin':'universal_ap_admin',
    'Max Associated Clients per WLAN':'max_associated_clients_per_wlan',
    'Max Associated Clients per AP per WLAN':'max_associated_clients_per_ap_per_wlan',
    'Max Associated Clients per AP Radio per WLAN':'max_associated_clients_per_ap_radio_per_wlan',
    'OKC':'okc',
    'Number of Active Clients':'number_of_active_clients',
    'CHD per WLAN':'chd_per_wlan',
    'WMM':'wmm',
    'WiFi Direct Policy':'wifi_direct_policy',
    'Channel Scan Defer Priority:':'channel_scan_defer_priority',
    'Priority (default)':'channel_scan_defer_priority_priority_default',
    'Scan Defer Time (msecs)':'scan_defer_time_msecs',
    'Media Stream Multicast-direct':'media_stream_multicast_direct',
    'CCX - AironetIe Support':'ccx_aironetie_support',
    'Peer-to-Peer Blocking Action':'peer_to_peer_blocking_action',
    'Radio Policy':'radio_policy',
    'DTIM period for 802.11a radio':'dtim_period_for_802_11a_radio',
    'DTIM period for 802.11b radio':'dtim_period_for_802_11b_radio',
    'Local EAP Authentication':'local_eap_authentication',
    'Mac Filter Authorization list name':'mac_filter_authorization_list_name',
    'Mac Filter Override Authorization list name':'mac_filter_override_authorization_list_name',
    'Accounting list name':'accounting_list_name',
    '802.1x authentication list name':'d_802_1x_authentication_list_name',
    '802.1x authorization list name':'d_802_1x_authorization_list_name',
    'Security':'security',
    '802.11 Authentication':'security_802_11_authentication',
    'Static WEP Keys':'security_static_wep_keys',
    'Wi-Fi Protected Access (WPA/WPA2/WPA3)':'security_wi_fi_protected_access_wpa_wpa2_wpa3',
    'WPA (SSN IE)':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa_ssn_ie',
    'WPA2 (RSN IE)':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie',
    'WPA3 (WPA3 IE)':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie',
    'AES Cipher':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_aes_cipher',
    'CCMP256 Cipher':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_ccmp256_cipher',
    'GCMP128 Cipher':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_gcmp128_cipher',
    'GCMP256 Cipher':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa3_wpa3_ie_gcmp256_cipher',
    'Auth Key Management':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management',
    '802.1x':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_802_1x',
    'PSK':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_psk',
    'CCKM':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_cckm',
    'FT dot1x':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_ft_dot1x',
    'FT PSK':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_ft_psk',
    'Dot1x-SHA256':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_dot1x_sha256',
    'PSK-SHA256':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_psk_sha256',
    'SAE':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_sae',
    'OWE':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_owe',
    'SUITEB-1X':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_suiteb_1x',
    'SUITEB192-1X':'security_wi_fi_protected_access_wpa_wpa2_wpa3_auth_key_management_suiteb192_1x',
    'CCKM TSF Tolerance': 'security_cckm_tsf_tolerance_msecs',
    'CCKM TSF Tolerance (msecs)':'security_cckm_tsf_tolerance_msecs',
    'OWE Transition Mode':'security_owe_transition_mode',
    'OSEN':'security_osen',
    'FT Support':'security_ft_support',
    'FT Reassociation Timeout':'security_ft_support_ft_reassociation_timeout_secs',
    'FT Reassociation Timeout (secs)':'security_ft_support_ft_reassociation_timeout_secs',
    'FT Over-The-DS mode':'security_ft_support_ft_over_the_ds_mode',
    'PMF Support':'security_pmf_support',
    'PMF Association Comeback Timeout (secs)':'security_pmf_support_pmf_association_comeback_timeout_secs',
    'PMF Association Comeback Timeout':'security_pmf_support_pmf_association_comeback_timeout_secs',
    'PMF SA Query Time (msecs)':'security_pmf_support_pmf_sa_query_time_msecs',
    'PMF SA Query Time':'security_pmf_support_pmf_sa_query_time_msecs',
    'Web Based Authentication':'security_web_based_authentication',
    'Conditional Web Redirect':'security_conditional_web_redirect',
    'Splash-Page Web Redirect':'security_splash_page_web_redirect',
    'Webauth On-mac-filter Failure':'security_webauth_on_mac_filter_failure',
    'Webauth Authentication List Name':'security_webauth_authentication_list_name',
    'Webauth Authorization List Name':'security_webauth_authorization_list_name',
    'Webauth Parameter Map':'security_webauth_parameter_map',
    'Band Select':'band_select',
    'Load Balancing':'load_balancing',
    'Multicast Buffer':'multicast_buffer',
    'Multicast Buffers (frames)':'multicast_buffers_frames',
    'Multicast Buffer Size':'multicast_buffers_frames',
    'IP Source Guard':'ip_source_guard',
    'Assisted-Roaming':'assisted_roaming',
    'Neighbor List':'assisted_roaming_neighbor_list',
    'Prediction List':'assisted_roaming_prediction_list',
    'Dual Band Support':'assisted_roaming_dual_band_support',
    'IEEE 802.11v parameters':'ieee_802_11v_parameters',
    'Directed Multicast Service':'ieee_802_11v_parameters_directed_multicast_service',
    'BSS Max Idle':'ieee_802_11v_parameters_bss_max_idle',
    'Protected Mode':'ieee_802_11v_parameters_bss_max_idle_protected_mode',
    'Traffic Filtering Service':'ieee_802_11v_parameters_traffic_filtering_service',
    'BSS Transition':'ieee_802_11v_parameters_bss_transition',
    'Disassociation Imminent':'ieee_802_11v_parameters_bss_transition_disassociation_imminent',
    'Optimised Roaming Timer (TBTTS)':'ieee_802_11v_parameters_bss_transition_disassociation_imminent_optimised_roaming_timer_tbtts',
    'Optimised Roaming Timer':'ieee_802_11v_parameters_bss_transition_disassociation_imminent_optimised_roaming_timer_tbtts',
    'Timer (TBTTS)':'ieee_802_11v_parameters_bss_transition_disassociation_imminent_timer_tbtts',
    'Timer':'ieee_802_11v_parameters_bss_transition_disassociation_imminent_timer_tbtts',
    'Dual Neighbor List':'ieee_802_11v_parameters_bss_transition_dual_neighbor_list',
    'WNM Sleep Mode':'ieee_802_11v_parameters_wnm_sleep_mode',
    '802.11ac MU-MIMO':'d_802_11ac_mu_mimo',
    '802.11ax parameters':'d_802_11ax_parameters',
    'OFDMA Downlink':'d_802_11ax_parameters_ofdma_downlink',
    'OFDMA Uplink':'d_802_11ax_parameters_ofdma_uplink',
    'MU-MIMO Downlink':'d_802_11ax_parameters_mu_mimo_downlink',
    'MU-MIMO Uplink':'d_802_11ax_parameters_mu_mimo_uplink',
    'BSS Target Wake Up Time':'d_802_11ax_parameters_bss_target_wake_up_time',
    'BSS Target Wake Up Time Broadcast Support':'d_802_11ax_parameters_bss_target_wake_up_time_broadcast_support',
    'mDNS Gateway Status':'mdns_gateway_status',
    'WIFI Alliance Agile Multiband':'wifi_alliance_agile_multiband',
    'Device Analytics':'device_analytics',
    'Advertise Support':'device_analytics_advertise_support',
    'Share Data with Client':'device_analytics_share_data_with_client',
    'Client Scan Report (11k Beacon Radio Measurement)':'client_scan_report_11k_beacon_radio_measurement',
    'Request on Association':'client_scan_report_11k_beacon_radio_measurement_request_on_association',
    'Request on Roam':'client_scan_report_11k_beacon_radio_measurement_request_on_roam',
    'WiFi to Cellular Steering':'wifi_to_cellular_steering',
    'MPSK':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie_mpsk',
    'Randomized GTK':'security_wi_fi_protected_access_wpa_wpa2_wpa3_wpa2_rsn_ie_randomized_gtk',
    'OWE Transition Mode WLAN ID':'security_owe_transition_mode_wlan_id',
    'IPv4 ACL':'security_web_based_authentication_ipv4_acl',
    'IPv6 ACL':'security_web_based_authentication_ipv6_acl',
}

ewlc_ap_rf_24_parsing_dict = {
    'unique_ap_rf_24ghz_key':'unique key is needed',
    'Number of Slots':'number_of_slots',
    'AP Name':'ap_name',
    'MAC Address':'mac_address',
    'Slot ID':'slot_id',
    'Radio Type':'radio_type',
    'Subband Type':'subband_type',
    'Noise Information':'noise_information',
    'Noise Profile':'noise_information_noise_profile',
    'Channel   1':'noise_information_channel_1',
    'Channel   2':'noise_information_channel_2',
    'Channel   3':'noise_information_channel_3',
    'Channel   4':'noise_information_channel_4',
    'Channel   5':'noise_information_channel_5',
    'Channel   6':'noise_information_channel_6',
    'Channel   7':'noise_information_channel_7',
    'Channel   8':'noise_information_channel_8',
    'Channel   9':'noise_information_channel_9',
    'Channel  10':'noise_information_channel_10',
    'Channel  11':'noise_information_channel_11',
    'Channel  12':'noise_information_channel_12',
    'Channel  13':'noise_information_channel_13',
    'Channel  14':'noise_information_channel_14',
    'Interference Information':'interference_information',
    'Interference Profile':'interference_information_interference_profile',
    'Channel   11':'interference_information_channel_1',
    'Channel   21':'interference_information_channel_2',
    'Channel   31':'interference_information_channel_3',
    'Channel   41':'interference_information_channel_4',
    'Channel   51':'interference_information_channel_5',
    'Channel   61':'interference_information_channel_6',
    'Channel   71':'interference_information_channel_7',
    'Channel   81':'interference_information_channel_8',
    'Channel   91':'interference_information_channel_9',
    'Channel  101':'interference_information_channel_10',
    'Channel  111':'interference_information_channel_11',
    'Channel  121':'interference_information_channel_12',
    'Channel  131':'interference_information_channel_13',
    'Rogue Histogram (20)':'interference_information_rogue_histogram_20',
    'Channel   12':'interference_information_rogue_histogram_20_channel_1',
    'Channel   22':'interference_information_rogue_histogram_20_channel_2',
    'Channel   32':'interference_information_rogue_histogram_20_channel_3',
    'Channel   42':'interference_information_rogue_histogram_20_channel_4',
    'Channel   52':'interference_information_rogue_histogram_20_channel_5',
    'Channel   62':'interference_information_rogue_histogram_20_channel_6',
    'Channel   72':'interference_information_rogue_histogram_20_channel_7',
    'Channel   82':'interference_information_rogue_histogram_20_channel_8',
    'Channel   92':'interference_information_rogue_histogram_20_channel_9',
    'Channel  102':'interference_information_rogue_histogram_20_channel_10',
    'Channel  112':'interference_information_rogue_histogram_20_channel_11',
    'Channel  122':'interference_information_rogue_histogram_20_channel_12',
    'Channel  132':'interference_information_rogue_histogram_20_channel_13',
    'Load Information':'load_information',
    'Load Profile':'load_information_load_profile',
    'Receive Utilization':'load_information_receive_utilization',
    'Transmit Utilization':'load_information_transmit_utilization',
    'Channel Utilization':'load_information_channel_utilization',
    'Attached Clients':'load_information_attached_clients',
    'Coverage Information':'coverage_information',
    'Coverage Profile':'coverage_information_coverage_profile',
    'Failed Clients':'coverage_information_failed_clients',
    'Client Signal Strengths':'client_signal_strengths',
    'RSSI -100 dBm':'client_signal_strengths_rssi_100_dbm',
    'RSSI  -92 dBm':'client_signal_strengths_rssi_92_dbm',
    'RSSI  -84 dBm':'client_signal_strengths_rssi_84_dbm',
    'RSSI  -76 dBm':'client_signal_strengths_rssi_76_dbm',
    'RSSI  -68 dBm':'client_signal_strengths_rssi_68_dbm',
    'RSSI  -60 dBm':'client_signal_strengths_rssi_60_dbm',
    'RSSI  -52 dBm':'client_signal_strengths_rssi_52_dbm',
    'Client Signal to Noise Ratios':'client_signal_to_noise_ratios',
    'SNR    0 dB':'client_signal_to_noise_ratios_snr_0_db',
    'SNR    5 dB':'client_signal_to_noise_ratios_snr_5_db',
    'SNR   10 dB':'client_signal_to_noise_ratios_snr_10_db',
    'SNR   15 dB':'client_signal_to_noise_ratios_snr_15_db',
    'SNR   20 dB':'client_signal_to_noise_ratios_snr_20_db',
    'SNR   25 dB':'client_signal_to_noise_ratios_snr_25_db',
    'SNR   30 dB':'client_signal_to_noise_ratios_snr_30_db',
    'SNR   35 dB':'client_signal_to_noise_ratios_snr_35_db',
    'SNR   40 dB':'client_signal_to_noise_ratios_snr_40_db',
    'SNR   45 dB':'client_signal_to_noise_ratios_snr_45_db',
    'Radar Information':'radar_information',
    'Detected Channels':'radar_information_detected_channels',
    'Blacklist Times':'radar_information_blacklist_times',
    'Channel Assignment Information':'channel_assignment_information',
    'Current Channel Average Energy':'channel_assignment_information_current_channel_average_energy',
    'Previous Channel Average Energy':'channel_assignment_information_previous_channel_average_energy',
    'Channel Change Count':'channel_assignment_information_channel_change_count',
    'Last Channel Change Time':'channel_assignment_information_last_channel_change_time',
    'Recommended Best Channel':'channel_assignment_information_recommended_best_channel',
    'RF Parameter Recommendations':'rf_parameter_recommendations',
    'Power Level':'rf_parameter_recommendations_power_level',
    'RTS/CTS Threshold':'rf_parameter_recommendations_rts_cts_threshold',
    'Fragmentation Threshold':'rf_parameter_recommendations_fragmentation_threshold',
    'Antenna Pattern':'rf_parameter_recommendations_antenna_pattern',
}
ewlc_ap_rf_5_parsing_dict = {
    'unique_ap_rf_5ghz_key':'unique key is needed',
    'Number of Slots':'number_of_slots',
    'AP Name':'ap_name',
    'MAC Address':'mac_address',
    'Slot ID':'slot_id',
    'Radio Type':'radio_type',
    'Subband Type':'subband_type',
    'Noise Information':'noise_information',
    'Noise Profile':'noise_information_noise_profile',
    'Channel  34':'noise_information_channel_34',
    'Channel  36':'noise_information_channel_36',
    'Channel  38':'noise_information_channel_38',
    'Channel  40':'noise_information_channel_40',
    'Channel  42':'noise_information_channel_42',
    'Channel  44':'noise_information_channel_44',
    'Channel  46':'noise_information_channel_46',
    'Channel  48':'noise_information_channel_48',
    'Channel  52':'noise_information_channel_52',
    'Channel  56':'noise_information_channel_56',
    'Channel  60':'noise_information_channel_60',
    'Channel  64':'noise_information_channel_64',
    'Channel 100':'noise_information_channel_100',
    'Channel 104':'noise_information_channel_104',
    'Channel 108':'noise_information_channel_108',
    'Channel 112':'noise_information_channel_112',
    'Channel 116':'noise_information_channel_116',
    'Channel 120':'noise_information_channel_120',
    'Channel 124':'noise_information_channel_124',
    'Channel 128':'noise_information_channel_128',
    'Channel 132':'noise_information_channel_132',
    'Channel 136':'noise_information_channel_136',
    'Channel 140':'noise_information_channel_140',
    'Channel 144':'noise_information_channel_144',
    'Channel 149':'noise_information_channel_149',
    'Channel 153':'noise_information_channel_153',
    'Channel 157':'noise_information_channel_157',
    'Channel 161':'noise_information_channel_161',
    'Channel 165':'noise_information_channel_165',
    'Channel 169':'noise_information_channel_169',
    'Channel 173':'noise_information_channel_173',
    'Interference Information':'interference_information',
    'Interference Profile':'interference_information_interference_profile',
    'Channel  341':'interference_information_channel_34',
    'Channel  361':'interference_information_channel_36',
    'Channel  381':'interference_information_channel_38',
    'Channel  401':'interference_information_channel_40',
    'Channel  421':'interference_information_channel_42',
    'Channel  441':'interference_information_channel_44',
    'Channel  461':'interference_information_channel_46',
    'Channel  481':'interference_information_channel_48',
    'Channel  521':'interference_information_channel_52',
    'Channel  561':'interference_information_channel_56',
    'Channel  601':'interference_information_channel_60',
    'Channel  641':'interference_information_channel_64',
    'Channel 1001':'interference_information_channel_100',
    'Channel 1041':'interference_information_channel_104',
    'Channel 1081':'interference_information_channel_108',
    'Channel 1121':'interference_information_channel_112',
    'Channel 1161':'interference_information_channel_116',
    'Channel 1201':'interference_information_channel_120',
    'Channel 1241':'interference_information_channel_124',
    'Channel 1281':'interference_information_channel_128',
    'Channel 1321':'interference_information_channel_132',
    'Channel 1361':'interference_information_channel_136',
    'Channel 1401':'interference_information_channel_140',
    'Channel 1441':'interference_information_channel_144',
    'Channel 1491':'interference_information_channel_149',
    'Channel 1531':'interference_information_channel_153',
    'Channel 1571':'interference_information_channel_157',
    'Channel 1611':'interference_information_channel_161',
    'Channel 1651':'interference_information_channel_165',
    'Channel 1691':'interference_information_channel_169',
    'Channel 1731':'interference_information_channel_173',
    'Rogue Histogram (20/40/80)':'interference_information_rogue_histogram_20_40_80',
    'Channel  342':'interference_information_rogue_histogram_20_40_80_channel_34',
    'Channel  362':'interference_information_rogue_histogram_20_40_80_channel_36',
    'Channel  382':'interference_information_rogue_histogram_20_40_80_channel_38',
    'Channel  402':'interference_information_rogue_histogram_20_40_80_channel_40',
    'Channel  422':'interference_information_rogue_histogram_20_40_80_channel_42',
    'Channel  442':'interference_information_rogue_histogram_20_40_80_channel_44',
    'Channel  462':'interference_information_rogue_histogram_20_40_80_channel_46',
    'Channel  482':'interference_information_rogue_histogram_20_40_80_channel_48',
    'Channel  522':'interference_information_rogue_histogram_20_40_80_channel_52',
    'Channel  562':'interference_information_rogue_histogram_20_40_80_channel_56',
    'Channel  602':'interference_information_rogue_histogram_20_40_80_channel_60',
    'Channel  642':'interference_information_rogue_histogram_20_40_80_channel_64',
    'Channel 1002':'interference_information_rogue_histogram_20_40_80_channel_100',
    'Channel 1042':'interference_information_rogue_histogram_20_40_80_channel_104',
    'Channel 1082':'interference_information_rogue_histogram_20_40_80_channel_108',
    'Channel 1122':'interference_information_rogue_histogram_20_40_80_channel_112',
    'Channel 1162':'interference_information_rogue_histogram_20_40_80_channel_116',
    'Channel 1202':'interference_information_rogue_histogram_20_40_80_channel_120',
    'Channel 1242':'interference_information_rogue_histogram_20_40_80_channel_124',
    'Channel 1282':'interference_information_rogue_histogram_20_40_80_channel_128',
    'Channel 1322':'interference_information_rogue_histogram_20_40_80_channel_132',
    'Channel 1362':'interference_information_rogue_histogram_20_40_80_channel_136',
    'Channel 1402':'interference_information_rogue_histogram_20_40_80_channel_140',
    'Channel 1442':'interference_information_rogue_histogram_20_40_80_channel_144',
    'Channel 1492':'interference_information_rogue_histogram_20_40_80_channel_149',
    'Channel 1532':'interference_information_rogue_histogram_20_40_80_channel_153',
    'Channel 1572':'interference_information_rogue_histogram_20_40_80_channel_157',
    'Channel 1612':'interference_information_rogue_histogram_20_40_80_channel_161',
    'Channel 1652':'interference_information_rogue_histogram_20_40_80_channel_165',
    'Channel 1692':'interference_information_rogue_histogram_20_40_80_channel_169',
    'Channel 1732':'interference_information_rogue_histogram_20_40_80_channel_173',
    'Load Information':'load_information',
    'Load Profile':'load_information_load_profile',
    'Receive Utilization':'load_information_receive_utilization',
    'Transmit Utilization':'load_information_transmit_utilization',
    'Channel Utilization':'load_information_channel_utilization',
    'Attached Clients':'load_information_attached_clients',
    'Coverage Information':'coverage_information',
    'Coverage Profile':'coverage_information_coverage_profile',
    'Failed Clients':'coverage_information_failed_clients',
    'Client Signal Strengths':'client_signal_strengths',
    'RSSI -100 dBm':'client_signal_strengths_rssi_100_dbm',
    'RSSI  -92 dBm':'client_signal_strengths_rssi_92_dbm',
    'RSSI  -84 dBm':'client_signal_strengths_rssi_84_dbm',
    'RSSI  -76 dBm':'client_signal_strengths_rssi_76_dbm',
    'RSSI  -68 dBm':'client_signal_strengths_rssi_68_dbm',
    'RSSI  -60 dBm':'client_signal_strengths_rssi_60_dbm',
    'RSSI  -52 dBm':'client_signal_strengths_rssi_52_dbm',
    'Client Signal to Noise Ratios':'client_signal_to_noise_ratios',
    'SNR    0 dB':'client_signal_to_noise_ratios_snr_0_db',
    'SNR    5 dB':'client_signal_to_noise_ratios_snr_5_db',
    'SNR   10 dB':'client_signal_to_noise_ratios_snr_10_db',
    'SNR   15 dB':'client_signal_to_noise_ratios_snr_15_db',
    'SNR   20 dB':'client_signal_to_noise_ratios_snr_20_db',
    'SNR   25 dB':'client_signal_to_noise_ratios_snr_25_db',
    'SNR   30 dB':'client_signal_to_noise_ratios_snr_30_db',
    'SNR   35 dB':'client_signal_to_noise_ratios_snr_35_db',
    'SNR   40 dB':'client_signal_to_noise_ratios_snr_40_db',
    'SNR   45 dB':'client_signal_to_noise_ratios_snr_45_db',
    'Radar Information':'interference_information_radar_information',
    'Detected Channels':'interference_information_radar_information_detected_channels',
    'Blacklist Times':'interference_information_radar_information_blacklist_times',
    'Channel Assignment Information':'channel_assignment_information',
    'Current Channel Average Energy':'channel_assignment_information_current_channel_average_energy',
    'Previous Channel Average Energy':'channel_assignment_information_previous_channel_average_energy',
    'Channel Change Count':'channel_assignment_information_channel_change_count',
    'Last Channel Change Time':'channel_assignment_information_last_channel_change_time',
    'Recommended Best Channel':'channel_assignment_information_recommended_best_channel',
    'RF Parameter Recommendations':'rf_parameter_recommendations',
    'Power Level':'rf_parameter_recommendations_power_level',
    'RTS/CTS Threshold':'rf_parameter_recommendations_rts_cts_threshold',
    'Fragmentation Threshold':'rf_parameter_recommendations_fragmentation_threshold',
    'Antenna Pattern':'rf_parameter_recommendations_antenna_pattern',
}
ewlc_ap_config_parsing_dict = {
    'Cisco AP Name':'cisco_ap_name',
    'Cisco AP Identifier':'cisco_ap_identifier',
    'Country Code':'country_code',
    'Regulatory Domain Allowed by Country':'regulatory_domain_allowed_by_country',
    'AP Country Code':'ap_country_code',
    'AP Regulatory Domain':'ap_regulatory_domain',
    'Slot 0':'ap_regulatory_domain_slot_0',
    'Slot 1':'ap_regulatory_domain_slot_1',
    'MAC Address':'mac_address',
    'IP Address Configuration':'ip_address_configuration',
    'IP Address':'ip_address',
    'IP Netmask':'ip_netmask',
    'Gateway IP Address':'gateway_ip_address',
    'Fallback IP Address Being Used':'fallback_ip_address_being_used',
    'Domain':'domain',
    'Name Server':'name_server',
    'CAPWAP Path MTU':'capwap_path_mtu',
    'Capwap Active Window Size':'capwap_active_window_size',
    'Telnet State':'telnet_state',
    'SSH State':'ssh_state',
    'Cisco AP Location':'cisco_ap_location',
    'Site Tag Name':'site_tag_name',
    'RF Tag Name':'rf_tag_name',
    'Policy Tag Name':'policy_tag_name',
    'AP join Profile':'ap_join_profile',
    'Flex Profile':'flex_profile',
    'Primary Cisco Controller Name':'primary_cisco_controller_name',
    'Primary Cisco Controller IP Address':'primary_cisco_controller_ip_address',
    'Secondary Cisco Controller Name':'secondary_cisco_controller_name',
    'Secondary Cisco Controller IP Address':'secondary_cisco_controller_ip_address',
    'Tertiary Cisco Controller Name':'tertiary_cisco_controller_name',
    'Tertiary Cisco Controller IP Address':'tertiary_cisco_controller_ip_address',
    'Administrative State':'administrative_state',
    'Operation State':'operation_state',
    'NAT External IP Address':'nat_external_ip_address',
    'AP Certificate type':'ap_certificate_type',
    'AP Mode':'ap_mode',
    'AP VLAN tagging state':'ap_vlan_tagging_state',
    'AP VLAN tag':'ap_vlan_tag',
    'CAPWAP Preferred mode':'capwap_preferred_mode',
    'AP Submode':'ap_submode',
    'Office Extend Mode':'office_extend_mode',
    'Dhcp Server':'dhcp_server',
    'Remote AP Debug':'remote_ap_debug',
    'Logging Trap Severity Level':'logging_trap_severity_level',
    'Logging Syslog facility':'logging_syslog_facility',
    'Software Version':'software_version',
    'Boot Version':'boot_version',
    'Mini IOS Version':'mini_ios_version',
    'Stats Reporting Period':'stats_reporting_period',
    'LED State':'led_state',
    'PoE Pre-Standard Switch':'poe_pre_standard_switch',
    'PoE Power Injector MAC Address':'poe_power_injector_mac_address',
    'Power Type/Mode':'power_type_mode',
    'Number of Slots':'number_of_slots',
    'AP Model':'ap_model',
    'IOS Version':'ios_version',
    'Reset Button':'reset_button',
    'AP Serial Number':'ap_serial_number',
    'Management Frame Protection Validation':'management_frame_protection_validation',
    'AP User Name':'ap_user_name',
    'AP 802.1X User Mode':'ap_802_1x_user_mode',
    'AP 802.1X User Name':'ap_802_1x_user_name',
    'Cisco AP System Logging Host':'cisco_ap_system_logging_host',
    'Cisco AP Secured Logging TLS mode':'cisco_ap_secured_logging_tls_mode',
    'AP Up Time':'ap_up_time',
    'AP CAPWAP Up Time':'ap_capwap_up_time',
    'Join Date and Time':'join_date_and_time',
    'Join Taken Time':'join_taken_time',
    'Join Priority':'join_priority',
    'AP Link Latency':'ap_link_latency',
    'AP Lag Configuration Status':'ap_lag_configuration_status',
    'Lag Support for AP':'lag_support_for_ap',
    'Rogue Detection':'rogue_detection',
    'Rogue Containment auto-rate':'rogue_containment_auto_rate',
    'Rogue Containment of standalone flexconnect APs':'rogue_containment_of_standalone_flexconnect_aps',
    'Rogue Detection Report Interval':'rogue_detection_report_interval',
    'Rogue AP minimum RSSI':'rogue_ap_minimum_rssi',
    'Rogue AP minimum transient time':'rogue_ap_minimum_transient_time',
    'AP TCP MSS Adjust':'ap_tcp_mss_adjust',
    'AP TCP MSS Size':'ap_tcp_mss_size',
    'AP IPv6 TCP MSS Adjust':'ap_ipv6_tcp_mss_adjust',
    'AP IPv6 TCP MSS Size':'ap_ipv6_tcp_mss_size',
    'Hyperlocation Admin Status':'hyperlocation_admin_status',
    'Retransmit count':'retransmit_count',
    'Retransmit interval':'retransmit_interval',
    'Fabric status':'fabric_status',
    'FIPS status':'fips_status',
    'WLANCC status':'wlancc_status',
    'USB Module Type':'usb_module_type',
    'USB Module State':'usb_module_state',
    'USB Operational State':'usb_operational_state',
    'USB Override':'usb_override',
    'GAS rate limit Admin status':'gas_rate_limit_admin_status',
    'WPA3 Capability':'wpa3_capability',
    'EWC-AP Capability':'ewc_ap_capability'
}

ewlc_ap_slots_parsing_dict = {
    'AP Regulatory Domain':'ap_regulatory_domain',
    'Radio Type':'radio_type',
    'Radio Mode':'radio_mode',
    'Radio Subband': 'radio_subband',
    'ATF Mode':'atf_mode',
    'Administrative State':'administrative_state',
    'Operation State':'operation_state',
    'Station Configuration':'station_configuration',
    'Configuration':'station_configuration_configuration',
    'Medium Occupancy Limit':'station_configuration_medium_occupancy_limit',
    'CFP Period':'station_configuration_cfp_period',
    'CFP Maximum Duration':'station_configuration_cfp_maximum_duration',
    'BSSID':'station_configuration_bssid',
    'Operation Rate Set':'station_configuration_operation_rate_set',
    '802.11b 1M Rate':'station_configuration_operation_rate_set_802_11b_1m_rate',
    '802.11b 2M Rate':'station_configuration_operation_rate_set_802_11b_2m_rate',
    '802.11b 5.5M Rate':'station_configuration_operation_rate_set_802_11b_5_5m_rate',
    '802.11b 11M Rate':'station_configuration_operation_rate_set_802_11b_11m_rate',
    '802.11b 6M Rate':'station_configuration_operation_rate_set_802_11b_6m_rate',
    '802.11b 9M Rate':'station_configuration_operation_rate_set_802_11b_9m_rate',
    '802.11b 12M Rate':'station_configuration_operation_rate_set_802_11b_12m_rate',
    '802.11b 18M Rate':'station_configuration_operation_rate_set_802_11b_18m_rate',
    '802.11b 24M Rate':'station_configuration_operation_rate_set_802_11b_24m_rate',
    '802.11b 36M Rate':'station_configuration_operation_rate_set_802_11b_36m_rate',
    '802.11b 48M Rate':'station_configuration_operation_rate_set_802_11b_48m_rate',
    '802.11b 54M Rate':'station_configuration_operation_rate_set_802_11b_54m_rate',
    '802.11a 6M Rate':'station_configuration_operation_rate_set_802_11a_6m_rate',
    '802.11a 9M Rate':'station_configuration_operation_rate_set_802_11a_9m_rate',
    '802.11a 12M Rate':'station_configuration_operation_rate_set_802_11a_12m_rate',
    '802.11a 18M Rate':'station_configuration_operation_rate_set_802_11a_18m_rate',
    '802.11a 24M Rate':'station_configuration_operation_rate_set_802_11a_24m_rate',
    '802.11a 36M Rate':'station_configuration_operation_rate_set_802_11a_36m_rate',
    '802.11a 48M Rate':'station_configuration_operation_rate_set_802_11a_48m_rate',
    '802.11a 54M Rate':'station_configuration_operation_rate_set_802_11a_54m_rate',
    'MCS Set':'station_configuration_mcs_set',
    'MCS 0':'station_configuration_mcs_set_mcs_0',
    'MCS 1':'station_configuration_mcs_set_mcs_1',
    'MCS 2':'station_configuration_mcs_set_mcs_2',
    'MCS 3':'station_configuration_mcs_set_mcs_3',
    'MCS 4':'station_configuration_mcs_set_mcs_4',
    'MCS 5':'station_configuration_mcs_set_mcs_5',
    'MCS 6':'station_configuration_mcs_set_mcs_6',
    'MCS 7':'station_configuration_mcs_set_mcs_7',
    'MCS 8':'station_configuration_mcs_set_mcs_8',
    'MCS 9':'station_configuration_mcs_set_mcs_9',
    'MCS 10':'station_configuration_mcs_set_mcs_10',
    'MCS 11':'station_configuration_mcs_set_mcs_11',
    'MCS 12':'station_configuration_mcs_set_mcs_12',
    'MCS 13':'station_configuration_mcs_set_mcs_13',
    'MCS 14':'station_configuration_mcs_set_mcs_14',
    'MCS 15':'station_configuration_mcs_set_mcs_15',
    'MCS 16':'station_configuration_mcs_set_mcs_16',
    'MCS 17':'station_configuration_mcs_set_mcs_17',
    'MCS 18':'station_configuration_mcs_set_mcs_18',
    'MCS 19':'station_configuration_mcs_set_mcs_19',
    'MCS 20':'station_configuration_mcs_set_mcs_20',
    'MCS 21':'station_configuration_mcs_set_mcs_21',
    'MCS 22':'station_configuration_mcs_set_mcs_22',
    'MCS 23':'station_configuration_mcs_set_mcs_23',
    'MCS 24':'station_configuration_mcs_set_mcs_24',
    'MCS 25':'station_configuration_mcs_set_mcs_25',
    'MCS 26':'station_configuration_mcs_set_mcs_26',
    'MCS 27':'station_configuration_mcs_set_mcs_27',
    'MCS 28':'station_configuration_mcs_set_mcs_28',
    'MCS 29':'station_configuration_mcs_set_mcs_29',
    'MCS 30':'station_configuration_mcs_set_mcs_30',
    'MCS 31':'station_configuration_mcs_set_mcs_31',
    'Beacon Period':'station_configuration_beacon_period',
    'Multi Domain Capability Implemented':'station_configuration_multi_domain_capability_implemented',
    'Multi Domain Capability Enabled':'station_configuration_multi_domain_capability_enabled',
    'Country String':'station_configuration_country_string',
    'Multi Domain Capability':'multi_domain_capability',
    'Configuration1':'multi_domain_capability_configuration',
    'First Channel':'multi_domain_capability_first_channel',
    'Number of Channels':'multi_domain_capability_number_of_channels',
    'MAC Operation Parameters':'multi_domain_capability_mac_operation_parameters',
    'Configuration2':'multi_domain_capability_mac_operation_parameters_configuration',
    'Fragmentation Threshold':'multi_domain_capability_mac_operation_parameters_fragmentation_threshold',
    'Packet Retry Limit':'multi_domain_capability_mac_operation_parameters_packet_retry_limit',
    'RTS/CTS Threshold':'multi_domain_capability_mac_operation_parameters_rts_cts_threshold',
    'Tx Power':'multi_domain_capability_tx_power',
    'Number of Supported Power Levels':'multi_domain_capability_tx_power_number_of_supported_power_levels',
    'Tx Power Level 1':'multi_domain_capability_tx_power_tx_power_level_1',
    'Tx Power Level 2':'multi_domain_capability_tx_power_tx_power_level_2',
    'Tx Power Level 3':'multi_domain_capability_tx_power_tx_power_level_3',
    'Tx Power Level 4':'multi_domain_capability_tx_power_tx_power_level_4',
    'Tx Power Level 5':'multi_domain_capability_tx_power_tx_power_level_5',
    'Tx Power Level 6':'multi_domain_capability_tx_power_tx_power_level_6',
    'Tx Power Level 7':'multi_domain_capability_tx_power_tx_power_level_7',
    'Tx Power Level 8':'multi_domain_capability_tx_power_tx_power_level_8',
    'Tx Power Configuration':'multi_domain_capability_tx_power_tx_power_configuration',
    'Current Tx Power Level':'multi_domain_capability_tx_power_current_tx_power_level',
    'Tx Power Assigned By':'multi_domain_capability_tx_power_tx_power_assigned_by',
    'Phy OFDM Parameters':'multi_domain_capability_phy_ofdm_parameters',
    'Configuration3':'multi_domain_capability_phy_ofdm_parameters_configuration',
    'Current Channel':'multi_domain_capability_phy_ofdm_parameters_current_channel',
    'Channel Assigned By':'multi_domain_capability_phy_ofdm_parameters_channel_assigned_by',
    'Extension Channel':'multi_domain_capability_phy_ofdm_parameters_extension_channel',
    'Channel Width':'multi_domain_capability_phy_ofdm_parameters_channel_width',
    'Allowed Channel List':'multi_domain_capability_phy_ofdm_parameters_allowed_channel_list',
    'TI Threshold':'multi_domain_capability_phy_ofdm_parameters_ti_threshold',
    'DCA Channel List':'multi_domain_capability_phy_ofdm_parameters_dca_channel_list',
    'Antenna Type':'multi_domain_capability_phy_ofdm_parameters_antenna_type',
    'Internal Antenna Gain (in .5 dBi units)':'multi_domain_capability_phy_ofdm_parameters_internal_antenna_gain_in_5_dbi_units',
    'Diversity':'multi_domain_capability_phy_ofdm_parameters_diversity',
    '802.11n Antennas':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas',
    'A':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_a',
    'B':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_b',
    'C':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_c',
    'D':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_d',
    '802.11n Antennas1':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas',
    'MIMO':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_mimo',
    'Tx':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_tx',
    'Rx':'multi_domain_capability_phy_ofdm_parameters_802_11n_antennas_rx',
    'Performance Profile Parameters':'multi_domain_capability_performance_profile_parameters',
    'Interference Threshold':'multi_domain_capability_performance_profile_parameters_interference_threshold',
    'Noise Threshold':'multi_domain_capability_performance_profile_parameters_noise_threshold',
    'RF Utilization Threshold':'multi_domain_capability_performance_profile_parameters_rf_utilization_threshold',
    'Client Threshold':'multi_domain_capability_performance_profile_parameters_client_threshold',
    'Coverage Exception Level':'multi_domain_capability_performance_profile_parameters_coverage_exception_level',
    '802.11ax Parameters':'multi_domain_capability_802_11ax_parameters',
    'HE Capable':'multi_domain_capability_802_11ax_parameters_he_capable',
    'CleanAir Management Information':'multi_domain_capability_cleanair_management_information',
    'CleanAir Capable':'multi_domain_capability_cleanair_management_information_cleanair_capable',
    'CleanAir Management Administration State':'multi_domain_capability_cleanair_management_information_cleanair_management_administration_state',
    'CleanAir Management Operation State':'multi_domain_capability_cleanair_management_information_cleanair_management_operation_state',
    'Rapid Update Mode':'multi_domain_capability_cleanair_management_information_rapid_update_mode',
    'Spectrum Expert Connections counter':'multi_domain_capability_cleanair_management_information_spectrum_expert_connections_counter',
    'Radio Extended Configurations':'multi_domain_capability_radio_extended_configurations',
    'Beacon period':'multi_domain_capability_radio_extended_configurations_beacon_period',
    'Beacon range':'multi_domain_capability_radio_extended_configurations_beacon_range',
    'Multicast buffer':'multi_domain_capability_radio_extended_configurations_multicast_buffer',
    'Multicast data-rate':'multi_domain_capability_radio_extended_configurations_multicast_data_rate',
    'RX SOP threshold':'multi_domain_capability_radio_extended_configurations_rx_sop_threshold',
    'CCA threshold':'multi_domain_capability_radio_extended_configurations_cca_threshold'}

ewlc_nearby_aps_parsing_dict = {
    'EWLC Nearby AP': 'channel',
}

main_parsing_dict_ewlc = {
    '--- show ap config general ---': ewlc_ap_config_parsing_dict,
    '--- show ap config slots ---': ewlc_ap_slots_parsing_dict,
    '--- show ap auto-rf dot11 5ghz ---': ewlc_ap_rf_5_parsing_dict,
    '--- show ap auto-rf dot11 24ghz ---': ewlc_ap_rf_24_parsing_dict,
    '--- show wlan all ---': ewlc_ssid_parsing_dict,
    '--- show wireless profile policy all ---': ewlc_policy_profile_parsing_dict,
    '--- show ap profile all-profiles ---': ewlc_ap_profile_parsing_dict,
    '--- show wireless profile flex  all ---': ewlc_flex_profile_parsing_dict,
    '--- show wireless profile flex all ---': ewlc_flex_profile_parsing_dict, #without double space
    '--- show wireless wps rogue ap summary ---': ewlc_rogue_ap_parsing_dict,
    '--- show wireless tag policy all ---': ewlc_policy_tag_parsing_dict,
    '--- show wireless tag site all ---': ewlc_site_tag_parsing_dict,
    '--- show wireless tag rf all ---': ewlc_rf_tag_parsing_dict,
    '--- show advanced eap ---': ewlc_advanced_eap_parsing_dict,
    '--- show wireless mobility summary ---': ewlc_mobility_parsing_dict,
    '--- show wireless multicast ---': ewlc_multicast_parsing_dict,
    '--- show ip http server status ---': ewlc_http_server_parsing_dict,
    '--- show wireless stats client detail ---': ewlc_client_stats_parsing_dict,
    '----- show ap auto-rf dot11 24ghz -----': ewlc_nearby_aps_parsing_dict, #Special case for Nearby APs info

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


def test_parsing_dicts_ewlc():
    parsing_dict_checker(ewlc_nearby_aps_parsing_dict, Ewlc_Nearby_Ap())
    parsing_dict_checker(ewlc_multicast_parsing_dict, Ewlc_Multicast())
    parsing_dict_checker(ewlc_mobility_parsing_dict, Ewlc_Mobility_All())
    parsing_dict_checker(ewlc_advanced_eap_parsing_dict, Ewlc_Advanced_Eap())
    parsing_dict_checker(ewlc_rf_tag_parsing_dict, Ewlc_Rf_Tag())
    parsing_dict_checker(ewlc_ssid_parsing_dict, Ewlc_Ssid_Config())
    parsing_dict_checker(ewlc_flex_profile_parsing_dict, Ewlc_Flex_Profile())
    parsing_dict_checker(ewlc_ap_profile_parsing_dict, Ewlc_Ap_Join_Profile())
    parsing_dict_checker(ewlc_policy_tag_parsing_dict, Ewlc_Policy_Tag())
    parsing_dict_checker(ewlc_ap_config_parsing_dict, Ewlc_Ap_Config())
    parsing_dict_checker(ewlc_ap_rf_24_parsing_dict, Ewlc_Ap_Rf_24_Config())
    parsing_dict_checker(ewlc_ap_rf_5_parsing_dict, Ewlc_Ap_Rf_5_Config())
    parsing_dict_checker(ewlc_ap_slots_parsing_dict, Ewlc_Ap_Slot_Config())
    parsing_dict_checker(ewlc_http_server_parsing_dict, Ewlc_Https_Server())
    parsing_dict_checker(ewlc_client_stats_parsing_dict, Ewlc_Client_Stats())
    logging.debug('Checked eWLC parsing dictionaries test results for correct parsing')