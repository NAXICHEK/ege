def f(c, e):
    if c < e or c == 24: return 0
    if c == e: return 1
    if c > 9:
        return f(c-1, e) + f(int(c**0.5), e) + f(int(str(c)[:-1]), e)
    return f(c-1, e) + f(int(c**0.5), e)
print(f(602, 7))