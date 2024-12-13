for i in range(int(289_123_456 ** 0.25), int(389_123_456 ** 0.25)):
    for j in range(2, i):
        if not i % j:  # Проверка на простое число
            break
    else:
        print(i ** 4, i ** 3)