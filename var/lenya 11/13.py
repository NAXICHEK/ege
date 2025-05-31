from ipaddress import *
net = ip_network('98.71.255.248/255.248.0.0', 0)
for i in net:
    b = f'{i:b}'
    if b.count('1') % 5 == 0:
        print(i)