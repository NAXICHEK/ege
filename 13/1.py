from ipaddress import *
for mask in range(16,25):
    net = ip_network(f'216.54.187.235/{mask}',0)
    net2 = ip_network(f'216.54.174.128/{mask}',0)
    print(net,net2)
print(int("11110000",2))