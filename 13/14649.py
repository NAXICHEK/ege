from ipaddress import *
c = 0
for kapusta in range(256):
    net = ip_network(f'116.242.{kapusta}.26/255.255.255.224', 0)
    d = 1
    for i in net:
        b = f'{i:b}'
        if (b[0:16].count('1') >= b[16:].count('1')) == 0:
            d = 0
    if d:
        print(kapusta)