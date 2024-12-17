f = open('17_18617.txt')
g = [int(x) for x in f]
maxi = max(x for x in g)
mini = min(x for x in g)
maxii = 0
c = 0
def pervoe_uslovie(a, b):
    return (((a % 3) == (maxi % 3)) or ((b % 3) == (maxi % 3))) and (((a % 7) == (mini % 7)) or ((b % 7) == (mini % 7)))
for i in range(len(g)-1):
    if pervoe_uslovie(g[i], g[i+1]):
        c += 1
        maxii = max(maxii, g[i] + g[i+1])
print(c)
print(maxii)