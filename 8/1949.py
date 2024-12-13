k=0
for x1 in "ПЕСКАР":
    for x2 in "ПЕСКАРЬ":
        for x3 in "ПЕСКАРЬ":
            for x4 in "ПЕСКАРЬ":
                for x5 in "ПЕСКАРЬ":
                    for x6 in "ПЕСКАРЬ":
                        for x7 in "ПЕСКАРЬ":
                            s=x1+x2+x3+x4+x5+x6+x7
                            if s.count("П")==1 and s.count("Е")==1 and s.count("С")==1 and s.count("К")==1 and s.count("А")==1 and s.count("Р")==1 and s.count("Ь")==1:
                                if s.count("ЬЕ") == 0 and s.count("ЬА") == 0 and s.count("ЬР") == 0:
                                    k += 1
print(k)