from turtle import *
tracer(0)
k = 20
for i in range(2):
    forward(3*k)
    left(90)
    backward(10*k)
    left(90)
up()
backward(10*k)
right(90)
forward(8*k)
left(90)
down()
for i in range(2):
    forward(16*k)
    right(90)
    forward(8*k)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(2, 'red')
done()