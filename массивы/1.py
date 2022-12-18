line = "ip nat inside source list ACL interface FastEthernet0/1"
words = line.split()
words[7] = 'GigabitEthernet'
line2 = words[0] + ' ' + words[1] + ' ' + words[2] + ' ' + words[3] + ' ' + words[4] + ' ' + words[5] + ' ' + words[6] + ' ' + words[7]
print (line2)
