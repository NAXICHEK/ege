from ipaddress import *
for i in range(33):
    net = ip_network(f'222.190.122.24/{i}', 0)
    print(net)
#21 22
print(2**(32-21)-3)