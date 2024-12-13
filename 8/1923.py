k = 0
g = "ЕАУ"
for x1 in "ЕСАУЛ":
    for x2 in "ЕСАУЛ":
        for x3 in "ЕСАУЛ":
            for x4 in "ЕСАУЛ":
                for x5 in "ЕСАУЛ":
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count("Е") == 1 and s.count("С") == 1 and s.count("А") == 1 and s.count("У") == 1 and s.count(
                            "Л") == 1:
                        fl = True
                        for i in range(len(s) - 1):
                            if (s[i] in g) and (s[i + 1] in g):
                                fl = False
                        if fl:
                             k += 1

print(k)