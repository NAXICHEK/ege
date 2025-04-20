from ipaddress import *
for i in range(33):
    net = ip_network('175.184.52.103/'+str(i), 0)
    print(net)