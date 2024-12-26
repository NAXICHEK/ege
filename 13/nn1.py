from ipaddress import *

for i in range(33):
    net = ip_network(f'111.81.208.27/{i}', 0)
    print(net, net.netmask)