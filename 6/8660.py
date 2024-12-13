from turtle import *
tracer(0)
k = 20

right(225)
for i in range(6):
    forward(15*k)
    right(60)
    forward(7*k)
    right(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(2, 'red')
done()