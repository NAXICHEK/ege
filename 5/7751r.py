for i in range(1000, 10001):
    a = i
    a1 = a//1000
    a2 = (a//100)%10
    a3 = (a//10)%10
    a4 = a%10
    b1 = a1+a2
    b2 = a3+a4
    s = str(min(b1,b2)) + str(max(b1,b2))
    if s == '117':
        print(i)