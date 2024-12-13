import time
a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
b = 0
a = a[::-1]
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        for a7 in a:
                            for a8 in a:
                                for a9 in a:
                                    for a10 in a:
                                        for a11 in a:
                                            s = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
                                            b += 1
                                            print(b)
                                            if s == 'ИНФОРМАТИКА':
                                                print(b, time.process_time())
                                                break