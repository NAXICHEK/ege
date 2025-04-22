from string import printable
for i in printable[:21]:
    r = int(f'82934{i}2',21) + int(f'2924{i}{i}7', 21) + int(f'67564{i}8', 21)
    if r % 20 == 0:
        print(r//20, i)