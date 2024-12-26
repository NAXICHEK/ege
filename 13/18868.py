from ipaddress import *
net = ip_network(f'222.121.128.0/255.255.224.0')
c = 0
for i in net:
    b = f'{i:b}'
    if b[-1] == b[-2]:
        c += 1
print(c)