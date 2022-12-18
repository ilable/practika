trunk_mode_template = [
"switchport mode trunk", "switchport trunk native vlan 999",
"switchport trunk allowed vlan"
]
trunk_config = {
"FastEthernet0/1": [10, 20, 30] ,
"FastEthernet0/2": [11, 30] ,
"FastEthernet0/4": [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    for line in intf_vlan_mapping:
        print(line)
        for line2 in trunk_template:
            if "switchport trunk allowed vlan" in line2:
                print(line2, intf_vlan_mapping[line])
            else:
                print(line2)





generate_trunk_config(trunk_config, trunk_mode_template)
