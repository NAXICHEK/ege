from ipaddress import *
net = ip_network(f'192.168.248.176/255.255.255.240', 0)
for i in net:
    b = f'{i:b}'
    if b.count('0') == b.count('1'):
        print(i)