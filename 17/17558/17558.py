f = open('17_17558.txt')
numbers = [int(xyi) for xyi in f]
counter = 0
krat32 = 0
d = []
for i in range(len(numbers)-1):
    if numbers[i] % 32 == 0:
        krat32 += 1
for i in range(len(numbers)-1):
    pi = numbers[i]
    vi = numbers[i + 1]
    # if ((pi >= 0) and (vi < 0)) or ((pi < 0) and (vi >= 0)):
    if (pi < 0) or (vi < 0):
        if  (pi+vi) < krat32:
            counter += 1
            d.append(pi+vi)
print(counter, max(d))