from ipaddress import *
for i in range(16, 25):
    ip = ip_network(f'205.154.212.20/{i}', 0)
    print(ip)