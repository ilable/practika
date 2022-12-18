from tabulate import tabulate
trunk_mode_template = [
"switchport mode trunk", "switchport trunk native vlan 999",
"switchport trunk allowed vlan"
]
trunk_config = {
"FastEthernet0/1": [10, 20, 30] ,
"FastEthernet0/2": [11, 30] ,
"FastEthernet0/4": [17]
}

keyer = {}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    for line in intf_vlan_mapping:
        for line2 in trunk_template:
            keyer[line] = trunk_template
            if "switchport trunk allowed vlan" in line2:
                keyer[line][-1] = "switchport trunk allowed vlan", intf_vlan_mapping.get(line)
    print(keyer)




generate_trunk_config(trunk_config, trunk_mode_template)
