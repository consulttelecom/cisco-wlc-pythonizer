import itertools
import time
import pickle
from datetime import date
import logging
from collections import Counter
# This will help to get tool usage statistics
import aide
from pathlib import Path
import sys
home = str(Path.home())
sys.path.append(home)

from aireos_dicts_classes import Wlc_Config, test_parsing_dicts_aireos, grep, show

from ewlc_dicts_classes import Wlc_Ios_Xe_Config, test_parsing_dicts_ewlc

from best_practices import Best_Practice_Description, bp_check

from channel_utilization_utils import utilization_statistics, bad_utilization_aps, channel_utilization, channel_utilization_visual, utilization_time, utilization_clients_scatterplot, utilization_nearby_aps_scatterplot, utilization_same_channel_nearby_aps_scatterplot, utilization_rogue_aps_scatterplot

from rogue_aps_utils import print_rogues_per_ap, rogue_ap_rssi_histogram, rogue_ap_summary, rogue_ap_summary_site, rogue_ap_time, number_of_rogue_aps

from cisco_dnac_utils import dnac_get_wlc_configs

from ssh_collection import ssh_collect

from parsing_utils import parse_file, read_folder

logging.basicConfig(filename=home+'/wlc-pythonizer.log', filemode='w', level=logging.DEBUG)
test_parsing_dicts_aireos() #this function checks parsing dicts for correct attributes
test_parsing_dicts_ewlc()   #this function checks parsing dicts for correct attributes

__author__ = "Roman Podoynitsyn"
#a = parse_file('../testing/testing_config/test_config_AOS.log')
#wlc = a['WLC2504']
#print(wlc, wlc.ssid)

#b = parse_file('../testing/testing_config/test_config_9800.log')
#ewlc = b['vEWLC']
#print(dir(ewlc))
#print(ewlc.grep('wpa3'))
#print(ewlc.ssid)
#print(ewlc.https_server.show())
#print(ewlc.rogue_aps.rogue_aps_list)
#print(ewlc.ap_configs)
#print(ewlc.ap_rf_24)
