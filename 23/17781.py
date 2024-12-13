def g(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sum(d)

def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c+1, e) + f(c+g(c), e)
print(f(2, 62)) # 207