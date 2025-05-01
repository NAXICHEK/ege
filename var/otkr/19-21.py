def f(a, m):
     if a >= 67: return  m % 2 == 0
     if m == 0: return 0
     h = [f(a+1, m-1),
          f(a+4, m-1),
          f(a*3, m-1),]
     return any(h) if (m-1) % 2 == 0 else all(h)
print([s for s in range(1, 67) if f(s, 2) and not f(s, 1)])
print([s for s in range(1, 67) if f(s, 3) and not f(s, 1)])
print([s for s in range(1, 67) if f(s, 4) and not f(s, 2)])