from itertools import product

count = 0
# Четные цифры в семеричной системе
even_digits = {'0', '2', '4', '6'}

for x in product('0123456', repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        # Счетчик пар четных цифр
        c = 0
        # Флаг, чтобы проверить, что три четные цифры не стоят подряд
        valid = True
        for i in range(len(s) - 1):
            if s[i] in even_digits and s[i + 1] in even_digits:
                c += 1
            # Проверяем, что три четные цифры не стоят подряд
            if i < len(s) - 2:
                if s[i] in even_digits and s[i + 1] in even_digits and s[i + 2] in even_digits:
                    valid = False
                    break
        # Если есть хотя бы две пары четных цифр и нет трех четных цифр подряд
        if c >= 2 and valid:
            count += 1

print(count)