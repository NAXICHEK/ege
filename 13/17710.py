from ipaddress import *
net = ip_network(f'214.187.224.0/255.255.224.0', 0)
c = 0
for i in net:
    b = f'{i:b}'
    if b.count('1') % 6 != 0:
        if b[-4:] == '1000':
            c += 1
print(c)