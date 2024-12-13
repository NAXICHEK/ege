from ipaddress import *
ip= ip_address("145.192.94.230")
for  mask in range(1,31):
    net = ip_network(f"{ip}/{mask}",0)
    print(net)
# 11111111.11111111.11110000.00000000
print(int('11110000', 2))