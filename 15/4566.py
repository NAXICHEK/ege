def f(a,x,b):
    if a<=x <=b:
        return True
    else:
        return False
mini=1000
for a in range(50):
    for b in range(a,50):
        count=0
        for i in range(500):
            x=i/10
            if f(10,x,22) <= (not(f(30,x,36)) or f(a,x,b)):
                count+=1
        if count==500:
            mini=min(mini,b-a)

print(mini)