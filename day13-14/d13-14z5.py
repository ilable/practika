access = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17}

trunk = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]}

a = []


def get_int_vlan_map(config_filename):
    if config_filename == access:
        a.append(config_filename)
        a.append(trunk)
    elif config_filename == trunk:
        a.append(config_filename)
        a.append(access)
    print(a)


get_int_vlan_map(access)
