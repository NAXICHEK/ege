from turtle import *

f = open('27A_18675.txt')

data = []

for l in f:
    s = l.strip().replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))
print(data)