def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+2, e) + f(c+3, e) + f(c*2, e)
# 20 18 10
print(f(3, 18)+f(3,10)) # 60