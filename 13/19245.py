from ipaddress import *
net = ip_network(f'218.194.82.148/255.255.255.192', 0)
for i in net:
    print(i)