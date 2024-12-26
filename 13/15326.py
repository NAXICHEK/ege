from ipaddress import *
net = ip_network(f'105.224.200.224/255.255.255.224', 0)
c = 0
for i in net:
    if f'{i:b}'.count('1') % 4 == 0:
        c += 1
print(c)