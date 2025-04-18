from ipaddress import *
for i in range(32, 0, -1):
    net = ip_network(f'143.131.211.37/{i}', 0)
    c = 0
    for j in net:
        if f'{j:b}'.count('1') == 10:
            c += 1
    if c == 15:
        print(i)