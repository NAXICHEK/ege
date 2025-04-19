from ipaddress import *
net = ip_network('172.16.128.0/255.255.192.0', 0)
c = 0
for i in net:
    if f'{i:b}'.count('1') % 2 != 0:
        c += 1
print(c)