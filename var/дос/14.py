for x in range(30):
    r = int(f'82934{x}2',21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if r % 20 == 0:
        print(r//20)