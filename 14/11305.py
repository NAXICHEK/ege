from time import process_time

def vsemprivetsvamistaskot(n, osnovanie):
    a = []
    while n > 0:
        a.append(n % osnovanie)
        n // osnovanie
    return a
dv9 = '0123456789abcdefghijklmnopqrs'
for x in range(100):
    a = vsemprivetsvamistaskot(x, 29)
    x29 = ''
    for i in a:
        x29 = x29 + i
    x29 = int(x29)
    a = vsemprivetsvamistaskot(47*x29*42696, 29) + vsemprivetsvamistaskot(8*x29*22, 29)
    if a % 28 == 0:
        print(x, process_time())
