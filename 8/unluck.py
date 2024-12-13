num = 0
counter = 0

for i in range(99999):
    num = int(num)
    num += 1
    num = str(num)
    odin = num.count('1')
    if len(str(num)) == 5 and odin == 1 and '7' not in num and '8' not in num and '9' not in num and '0' not in num:
        counter += 1
        print(num)
    else:
        counter = counter

print(counter)