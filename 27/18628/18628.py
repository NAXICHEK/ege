from turtle import *

f = open('27A_18628.txt')

data = []

for l in f:
    s = l.strip().replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append()

print(len(data))
print(data)