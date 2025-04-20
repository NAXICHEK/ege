from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0', 0)
c = 0
for i in net:
    b = f'{i:b}'
    if  b[16:].count('0') % 2 != 0:
        if b[:16].count('1') <= b[16:].count('0'):
            c += 1
print(c)