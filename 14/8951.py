for i in range(6, 37):
    r = 7**500 - int('53', i)
    if r % 6 == 0:
        print(i) # 8