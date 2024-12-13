for i in range(1, 100, 2):
    binn = str(bin(i))
    binn = binn.replace('0b', '')
    if i % 5 == 0:
        binn = binn[:3] + binn
    else:
        ostatok = bin((i % 5)*5)
        ostatok = ostatok.replace('0b', '')
        binn += ostatok
    if int(binn, 2) < 313:
        print(i, int(binn, 2))
