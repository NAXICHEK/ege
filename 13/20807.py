from ipaddress import *
net = ip_network('172.16.192.0/255.255.192.0', 0)
c = 0
for i in net:
    b = f'{i:b}'
    if b.count('1') % 5 != 0:
        c += 1
print(c)