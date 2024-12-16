f = open('17_18142.txt')
n = [int(x) for x in f]
m = min(i for i in n if str(i) == '8')
count = 0
mah = 0
for i in range(len(n)):
    try:
        c = 0
        if n[i] % 16 == m: c += 1
        if n[i+1] % 16 == m: c += 1
        if c == 1:
            count += 1
            mah = max(mah, n[i] + n[i+1])
    except IndexError:
        print('unluck')
print(count, mah)