count = 0
a = []
max_ending_238 = 0
f = [int(x) for x in open('17.55.r.txt')]
g = [str(x) for x in f]
for number in g:
    if number[-3:] == '238':
        a.append(int(number))
print(a)
print(max(a))
