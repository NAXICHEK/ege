from ipaddress import *
counetr = 0
for j in range(256):
    try:
        net = ip_network(f'172.16.168.0/255.255.255.{j}', 0)
        c = 0
        for i in net:
            if f'{i:b}'.count('0') % 7 == 0:
                c += 1
        if c == 35:
            print(j)
    except ValueError:
        pass