from ipaddress import *
c = 0
net = ip_network(f'172.140.68.0/255.255.248.0', 0)
for i in net:
    if f'{i:b}'.count('0') > 15:
        c += 1
print(c)