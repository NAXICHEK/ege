from ipaddress import *
for kapusta in range(256):
    d = 1
    for i in ip_network(f'116.242.{kapusta}.26/255.255.255.224', 0):
        if (f'{i:b}'[0:16].count('1') >= f'{i:b}'[16:].count('1')) == 0: d = 0
    if d: print(kapusta)