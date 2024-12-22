from functools import lru_cache

a = ''
@lru_cache(None)
def f(c, e, l):
    global a
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c+1, e, 'a') + f(c*3, e, 'b') + f(c+5, e, 'c')
    a += l

print(f(3, 69, 'g') if 'cac' in a else print(0))