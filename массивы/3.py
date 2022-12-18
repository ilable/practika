config = "switchport trunk allowed vlan 1,3,10,20,30,100"
words = config.split()
vlans_str = words[-1]
result = vlans_str.split(",")
print(result)