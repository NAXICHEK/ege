from turtle import *
screensize(3000, 3000)
tracer(0)
k = 30
for i in range(3):
    forward(10*k)
    right(120)
up()
fd(10*k)
right(90)
fd(3*k)
down()
for i in range(4):
    fd(10*k)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(2, 'red')
done()