import yaml, itertools
from aireos_dicts_classes import NamedList

def setInDict(dataDict, maplist, value):
    # Recursive function for SETTING value in nested dictionary from list of keys
    first, rest = maplist[0], maplist[1:]
    if rest:
        try:
            if not isinstance(dataDict[first], dict):
                # if the key is not a dict, then make it a dict
                dataDict[first] = {}
        except KeyError:
            # if key doesn't exist, create one
            dataDict[first] = {}

        setInDict(dataDict[first], rest, value)
    else:
        dataDict[first] = value

def compare(object_instance1, object_instance2, prev_steps_list=[], result=None, name='', printout = False):
    diffs = 0  # Counter for all diffs found
    analyzed_attributes = 0  # Counter for all attributes analyzed
    if hasattr(object_instance1, 'objname') == False:
        print('ERROR: Compare should be used only for customized classes!!!')
        return None, diffs, analyzed_attributes
    # print('Compare called for ',object_instance1)#,' with result ',result,' and steps list ',prev_steps_list)
    prev_steps_list.append(object_instance1.objname + name)
    if result == None:  # Make result empty if it is not passed as input
        res = {}
    else:
        res = result
    if type(object_instance1) == type(object_instance2):
        if type(object_instance1) == NamedList or type(object_instance2) == NamedList:
            if object_instance1.item_name == object_instance2.item_name:  # should be called only for Named Lists containing SAME item types
                for x, y in list(itertools.product(object_instance1, object_instance2)):
                    index = 0
                    # List matching dictionary SHOULD be defined which attributes should be the same for pair of items to compare (MORE FLEXIBILITY)
                    if type(x) == NamedList:
                        if x.name == y.name:
                            sub_result, subdiffs, sub_attrs = compare(x, y, prev_steps_list, res, ' ' + x.name)
                            diffs = diffs + subdiffs
                            analyzed_attributes = analyzed_attributes + sub_attrs
                    index += 1
            else:  # if called for Named Lists containing different item types
                print('ERROR: Compare is called for different types of objects')
                res = None
            # print('%%% Going one level UP - LIST comparison is over')
            prev_steps_list.pop()
        else:
            for attr, value in object_instance1.__dict__.items():
                analyzed_attributes += 1
                if hasattr(value, 'objname') == True:
                    sub_result, sub_diffs, sub_attrs = compare(value, getattr(object_instance2, attr), prev_steps_list,
                                                               res)
                    diffs = diffs + sub_diffs
                    analyzed_attributes = analyzed_attributes + sub_attrs
                else:
                    if value != getattr(object_instance2, attr):
                        diffs += 1
                        prev_steps_list.append(attr)  # Add name of attribute in dictionary tree
                        setInDict(res, prev_steps_list, [value, getattr(object_instance2, attr)])
                        prev_steps_list.pop()  # Remove the name of attribute as we move to next attribute
            prev_steps_list.append('Subdiffs')  # To save the sub-result in dictionary tree
            setInDict(res, prev_steps_list, [diffs, analyzed_attributes])
            prev_steps_list.pop()  # To remove Subdiffs attribute from dictionary tree
            prev_steps_list.pop()  # When the comparison is over, go one level up in object tree

    else:
        print('ERROR: Compare is called for different types of objects')
        res = None
    prev_steps_list = []
    if printout:
        print(yaml.dump(res)) #Uncomment to pretty print of compare output
    return res, diffs, analyzed_attributes


def config_diversity(config_list, printout=False):
    # This function calculates overall diversity metric in configuration for a list of config objects
    # Diversity metric is defined as the number of attributes with different values divided by overall number of config attributes
    different_values = 0
    overall_config_items = 0
    if isinstance(config_list, list) == False:
        print('This function works only with LIST of config objects')
        return None
    for item in config_list:
        if hasattr(item, 'objname') == False:
            print('ERROR: This function should be used only for customized classes')
            return None
    for item in config_list:
        if item.objname != config_list[0].objname:
            print('This function works only with config objects of the same type')
            return None
    for item in config_list:
        result, diffs, attributes_number = compare(config_list[0], item)
        different_values = different_values + diffs
        overall_config_items = overall_config_items + attributes_number
    if overall_config_items > 0:
        if printout:
            print('Diversity metric is equal ', round(100 * different_values / float(overall_config_items)), ' %')
            print('This metric is calculated for ', len(config_list), ' config items of type ', config_list[0].objname)
        return different_values * len(config_list) / float(overall_config_items)

def mac_changer(mac):
    #This function changes MAC address format from 9800 to old ('084f.a91d.2a00'->'08:4f:a9:1d:2a:00')
    mac_new = mac.replace('.','')
    for index in [2,5,8,11,14]:
        mac_new = mac_new[:index] + ':' + mac_new[index:]
    return mac_new

def ap_name_bssid(wlc_config):
    #This function returns list of (AP name, BSSID) tuples. Really useful for Ekahau site survey when AP names are not broadcasted
    return [(ap.cisco_ap_name, mac_changer(ap.cisco_ap_identifier)) for ap in wlc_config.ap_configs]
