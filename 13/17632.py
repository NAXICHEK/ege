from ipaddress import *
net = ip_network(f'112.160.0.0/255.240.0.0', 0)
c = 0
for i in net:
    if f'{i:b}'.count('1') % 5 == 0:
        c += 1
print(c)