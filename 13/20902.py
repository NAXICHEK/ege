from ipaddress import *
c = 0
net = ip_network('172.16.80.0/255.255.248.0', 0)
for i in net:
    b = f'{i:b}'
    if b.count('1') % 2 != 0: c += 1
print(c)