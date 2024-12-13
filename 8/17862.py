a = '0123456789ab'
counter = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
             for a4 in a:
                  for a5 in a:
                      s = a1 + a2 + a3 + a4 + a5
                      if s[0] != '0' and s.count('7') == 1 and (s.count('9') + s.count('a') + s.count('b') <= 3):
                          counter += 1
print(counter)