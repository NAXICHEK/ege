def f(c, e, s):
    if c > e + 1000: return 0
    if c == e: return 1
    if s == 'a': return f(c*2, e, 'b') + f(c*3, e, 'c')
    if s != 'a': return f(c-1, e, 'a') + f(c*2, e, 'b') + f(c*3, e, 'c')
print(f(3, 15, ' '))