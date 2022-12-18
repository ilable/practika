ip = "192.168.3.1"
ip_split = ip.split(".")
print(ip_split[0],' '*10,ip_split[1],' '*10,ip_split[2],' '*10,ip_split[3])
print(bin(int(ip_split[0])),' ' * 2, bin(int(ip_split[1])),'  ' * 2, bin(int(ip_split[2])), "   " * 2, bin(int(ip_split[3])))