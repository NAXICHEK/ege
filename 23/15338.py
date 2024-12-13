def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1, e) + f(c*2, e)
print(f(4,8)*f(8,10)*f(10,15)) # 2