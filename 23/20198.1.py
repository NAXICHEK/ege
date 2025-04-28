a = []
def f(c, e, k):
    if c > e+3: return 0
    if c == e: return 1
    a.append(k)
    if a[-2:] == ['a', 'a']:
        return f(c+5, e, 'b') + f(c*2, e, 'c')
    return f(c-1, e, 'a') + f(c+5, e, 'b') + f(c*2, e, 'c')
def d(cc, ee, s):
    if cc > ee+3 or 'aaa' in s: return 0
    if cc == ee and 'aaa' not in s: return 1
    return d(cc-1, ee, s + 'a') + d(cc+5, ee, s + 'b') + d(cc*2, ee, s + 'b')
print(f(5, 34, ''))
print(d(5, 34, ''))
