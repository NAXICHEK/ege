r = 0
def f(c, e):
    global r
    if c < e: return 0
    if c == e: return 1
    if r <= 2:
        return f(c-1, e) + f(c+5, e) + f(c*2, e)
        r += 1
    return f(c+5, e) + f(c*2, e)
print(f(5, 34), r)