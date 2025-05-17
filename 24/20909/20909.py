f = open('24_20909.txt').read()
f = f.replace('AB', '!')
f = f.split('!')
m = 0
for i in range(len(f)):
    d = 0
    sp = []
    for j in range(len(f)-i):
        le = len(f[i+j])
        sp.append([f[i+j], le])
        d += le
        if j >= 99: break
    m = max(m, d)
    if d == 541:
        for s in sp:
            print(s)
        print(len(sp)*2)
        break
print(m) # 541
# 741
# 2
# 7
#BAAABDABAB!!!!! # 2
# !ABDBBBBAFABBBBAABABBAABABDBABBCBDAAAA # 7