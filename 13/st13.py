from ipaddress import *
a = ip_address('157.220.185.237')
b = ip_address('157.220.184.230')
for i in range(33):
    net1 = ip_network(f'157.220.185.237/{i}', 0)
    if a in net1 and b in net1:
        c = 0
        for i in net1:
            if f'{i:b}'.count('1') == 15:
                c += 1
        print(c, i)