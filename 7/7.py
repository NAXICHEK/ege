# razreshenie 4194304
for i in range(1000000000):
    a = i * 24
    if a == 12 * 1024 * 1024 * 8:
        print(i)
        break
a2 = ((4194304/4)*8)/1024/1024/8
print(a2)