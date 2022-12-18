access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(intf_vlan_mapping, access_template, *port_security):
    for line in access_template:
        if "access" in line:
            print(line)
        


generate_access_config(access_config, access_mode_template, port_security_template)
