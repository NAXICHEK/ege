from ipaddress import *
for i in range(33): # 27 28 29
    net = ip_network(f'153.202.16.37/{i}', 0)
    print(net)