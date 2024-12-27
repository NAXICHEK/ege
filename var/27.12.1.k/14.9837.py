for x in range(24):
    r = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
    if r % 22 == 0:
        print(r//22, x)
        break