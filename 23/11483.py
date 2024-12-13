def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+3, e) + f(c*3, e)
print(f(3, 9)*f(9, 27)*f(27, 31)) # 12516