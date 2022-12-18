mac = "D45D:6401:01BC"
mac_hex = mac.split(":")
mac_string = mac_hex[0] + mac_hex[1] +mac_hex[2]
int = int(mac_string, 16)
result = bin(int)
print(result)