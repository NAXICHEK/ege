from ipaddress import *
for i in range(33):
    net = ip_network(f'148.195.140.28/{i}', 0)
    print(net)