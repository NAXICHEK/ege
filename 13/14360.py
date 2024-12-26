from ipaddress import *
for i in range(33):
    net = ip_network(f'153.202.16.37/{i}', 0)
m = 0
for i in range(27, 30):
    b = '1' * i + '0' * (32-i)
    m = max(m, int(b[16:24], 2) + int(b[24:], 2))
print(m)

# b = int('1'*29 + '0'*3)
# # 1111111111111111.11111111.11111000
# print(int('11111000', 2))
# print(255+248)