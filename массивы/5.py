command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
words1 = command1.split()
words2 = command2.split()
vlans_str1 = words1[-1]
vlans_str2 = words2[-1]
vlans1 = vlans_str1.split(",")
vlans2 = vlans_str2.split(",")
result = list(set(vlans1) & set(vlans2))
print(result)