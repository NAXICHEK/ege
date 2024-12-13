

def f(a,x,b):
    if a <= x <= b:
        return True
    else:
        return False
mini = 0
for a in range(50):
    for b in range(a, 50):
        counter = 0
        for i in range(500):
            x =i/10
            if not(f(32, x, 68)) or (f(54, x, 76)) == (not(a,x,b)):
                counter += 1
        if counter == 1249998:
            mini = min(mini, b-a)
print(mini)