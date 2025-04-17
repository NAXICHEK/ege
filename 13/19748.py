from ipaddress import *
for i in range(1, 33):
    net1 = ip_network(f'157.220.185.237/{i}', 0)
    net2 = ip_network(f'157.220.184.230/{i}', 0)
    if net1 == net2:
        c = 0
        print(net1)
net1 = ip_network(f'157.220.185.237/23', 0)
c = 0
for j in net1:
    b = f'{j:b}'
    if b.count('1') == 15:
        c += 1
print(c)