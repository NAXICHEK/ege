from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)
c = 0
for i in net:
    b = bin(int(i))[2:]
    if b.count('1') % 4 != 0:
        c += 1
print(c)