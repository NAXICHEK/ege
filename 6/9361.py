from turtle import *
tracer(0)
k = 20

backward(4*k)
right(90)
backward(3*k)
left(90)

right(30)
for _ in range(4):
    fd(14*k)
    right(120)
up()
for x in range(-20, 20):
    for y in range (-20, 20):
        setpos(x*k, y*k)
        dot(2, 'red')

done()
