def p(x):
    return x > 1 != 0 and all(x % i for i in range(2, int(x**0.5)+1))
f = open('17_9993.txt')
g = [int(x) for x in f]
m = max([x for x in g if str(x)[-2:] == '17'])
c = 0
mmm = 0
for i in range(len(g)):
    try: # травим
        a = g[i]
        b = g[i+1]
        if ((p(a) == True) and (p(b) == False)) or ((p(a) == False) and (p(b) == True)):
            if abs(a+b) % m == 0:
                c += 1
                mmm = max(mmm, a*b)
    except IndexError:
        print('''Теплое место, но улицы ждут
Отпечатков наших ног.
Звездная пыль - на сапогах.
Мягкое кресло, клетчатый плед,
Не нажатый вовремя курок.
Солнечный день - в ослепительных снах.
Группа крови - на рукаве,
Мой порядковый номер - на рукаве,
Пожелай мне удачи в бою, пожелай мне:
Не остаться в этой траве,
Не остаться в этой траве.
Пожелай мне удачи, пожелай мне удачи!
И есть чем платить, но я не хочу
Победы любой ценой.
Я никому не хочу ставить ногу на грудь.
Я хотел бы остаться с тобой,
Просто остаться с тобой,
Но высокая в небе звезда зовет меня в путь.
Группа крови - на рукаве,
Мой порядковый номер - на рукаве,
Пожелай мне удачи в бою, пожелай мне:
Не остаться в этой траве,
Не остаться в этой траве.
Пожелай мне удачи, пожелай мне удачи!
''')
print(c)
print(mmm)