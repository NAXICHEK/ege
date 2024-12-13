a = sorted('ЗИМА')
c = 0
for a1 in sorted('ЗМ'):
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in sorted('ИА'):
                    a = a1+a2+a3+a4+a5
                    c+=1
print(c)