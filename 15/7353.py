def funkciya_kotoraya_vozvrashataet_true_ili_false(x, y):
    return x % y == 0

def b(x):
    return 70 <= x <= 80
count = 0
for a in range(1, 1000):
    c = 0
    for x in range(1000):
        if funkciya_kotoraya_vozvrashataet_true_ili_false(x, a) or ((b(x))<= (not funkciya_kotoraya_vozvrashataet_true_ili_false(x, 18))):
            c += 1
    if c == 1000:
        count += 1
print(count)