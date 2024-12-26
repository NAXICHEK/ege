from ipaddress import *
for i in range(33):
    net = ip_network(f'76.155.48.2/{i}', 0)
    print(net)