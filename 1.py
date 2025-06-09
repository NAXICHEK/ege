f = '1234567890qwertyuiopasdfgh'
for i in range(len(f)):
    for j in range(i, len(f)):
        print(f[i:j+1])