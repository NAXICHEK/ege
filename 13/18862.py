from ipaddress import *
net = ip_network(f'172.140.68.0/255.255.248.0', 0)
c = 0
for i in net:
    b = f'{i:b}'
    if b.count('0') > 15:
        c += 1
print(c)