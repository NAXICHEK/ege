from ipaddress import *
for i in range(33):
    net = ip_network(f'241.185.253.57/{i}', 0)
    print(net, 32 - i)