from string import printable
for x in printable[:25]:
    r = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if r % 24 == 0:
        print(x, r//24)