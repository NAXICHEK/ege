from turtle import *
tracer(0)
screensize(3000, 3000)
k = 20
for i in range(8):
    for j in range(4):
        fd(k*5)
        right(30)
        fd(k*6)
        right(150)
    right(60)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(2, 'red')
done()