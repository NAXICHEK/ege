from ipaddress import *
c = 0
net = ip_network(f'123.222.111.192/255.255.255.248', 0)
for i in net:
    b = f'{i:b}'
    if b.count('0') % 3 != 0:
        c += 1
print(c)