ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
words = ospf_route.split()
print ('Prefix\t',words[0])
print ('AD/Metric\t',words[1])
print ('Next-Hop\t',words[3][:-1])
print ('Last update\t',words[4][:-1])
print ('Outbound Interface\t',words[5])