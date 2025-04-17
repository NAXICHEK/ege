from ipaddress import *
for i in range(1, 33):
    net1 = ip_network(f'200.154.190.12/{i}', 0)
    net2 = ip_network(f'200.154.184.0/{i}', 0)
    if net1 == net2:
        print(i)
net1 = ip_network(f'200.154.190.12/21', 0)
for i in net1:
    b = f'{i:b}'
    print(b.count('1'))