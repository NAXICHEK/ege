from turtle import *
screensize(3000)
tracer(0)
k = 5
for i in range(9):
    fd(27*k)
    right(90)
    fd(30*k)
    right(90)
up()
fd(3*k)
right(90)
fd(6*k)
left(90)
down()
for i in range(9):
    fd(77*k)
    right(90)
    fd(66*k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(2, 'red')
done()