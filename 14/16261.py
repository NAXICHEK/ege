m = 0
for i in '0123456789abcdefghijk':
    for j in '0123456789abcdefghijk':
        r = int(f'943697{i}21',21) - int(f'2{j}9253',21)
        if r % 20 == 0:
            m = max(m, int(i, 21) - int(j, 21))
            print(r//20, m, i, j, int(i, 21) - int(j, 21))