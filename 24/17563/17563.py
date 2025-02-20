import re
from itertools import product, repeat

# Функция для удаления незначащих нулей и нулей между знаками
def clean_sequence(s):
    # Удаляем незначащие нули в начале чисел
    s = re.sub(r'\b0+(\d+)', r'\1', s)
    # Удаляем нули между знаками - или *
    s = re.sub(r'([-*])0+([-*])', r'\1\2', s)
    return s

# Чтение файла
f = open('24_17563.txt').readline()

# Очистка последовательности
f = clean_sequence(f)

# Далее ваш оригинальный код
g = []
d = 0
for i in range(2, 10):
    for x in product('-*', repeat=i):
        s = ''.join(x)
        if s in f:
            f = f.replace(s, '!')
f = f.split('!')
for i in f:
    try:
        a = eval(i)
        if a > -100000000000:
            d = max(d, len(i))
            if len(i) == 44:
                print(i)
        else:
            pass
    except SyntaxError:
        pass
print(d)