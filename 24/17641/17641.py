f = open('24_17641.txt').readline()
f = f.replace('+*', '!')
f = f.replace('*+', '!')
f = f.replace('**', '!')
f = f.replace('++', '!')
t = f.split('!')
c = 0
for i in t:
    for j in range(len(i)):
        for jj in range(len(i)):
            s = i[j:jj]
            if len(s) > 0:
                if '-' in s:
                    d = []

                n, k = s[0], s[-1]
                if n != '+' and n != '*' and n != '!' and k != '+' and k != '*' and k != '!':
                    try:
                        g = eval(s)
                        if g == 0:
                            if len(s) == 140:
                                print(s)
                            c = max(c, len(s))

                    except SyntaxError:
                        pass
print(c)