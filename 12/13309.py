for n in range(4, 1000):
    s = '7' * 15 + '5' * n + '4' * 20  # Располагаем '7' перед '5' для максимальных замен '75'
    while '75' in s or '74' in s:
        if '75' in s:
            s = s.replace('75', '744', 1)
        else:
            s = s.replace('74', '44', 1)
    if s.count('4') == 65:  # Проверяем достижение максимума '4'
        print(n)
        break
