

def f(c, e):
    if c > e or c == 35: return 0
    if c == e: return 1
    return f(c+1, e)+f(c+2, e)+f(c*2, e)
print(f(7, 13)*f(13, 15)*f(15, 51))