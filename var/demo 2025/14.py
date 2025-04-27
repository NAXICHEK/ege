from string import printable

for x in printable[:19]:
    r = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if r % 18 == 0:
        print(r//18, x)