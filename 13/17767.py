from ipaddress import *
c = 0
net = ip_network(f'228.172.236.0/255.255.240.0', 0)
for i in net:
    if f'{i:b}'.count('1') % 5 != 0:
        c += 1
print(c)