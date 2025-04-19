from ipaddress import *
for svetyashke in range(130):
    print(1) if [x for x in ip_network(f'217.109.{svetyashke}.94/255.255.254.0', 0) if (f'{x:b}'[0:16].count('0') >= f'{x:b}'[16:].count('0')) == 0]==1 else print(svetyashke)