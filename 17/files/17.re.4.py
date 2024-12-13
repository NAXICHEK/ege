s = []
f = open('17.bare.txt')
for l in f:
    s.append(int(l))
count = 0
d = 0
for i in range(len(s) - 1):
    for k in range(i + 1, len(s)):
        if (s[i] - s[k]) % 60 == 0:
            count += 1
            if d < abs(s[k] - s[i]):
                d = abs(s[k] - s[i])
print(count, d)