from turtle import *
k = 20
screensize(4000, 4000)
tracer(0)
for i in range(2):
    fd(28*k)
    right(90)
    fd(18*k)
    right(90)
up()
fd(14*k)
right(90)
fd(10*k)
left(90)
down()
for i in range(2):
    fd(30*k)
    right(90)
    fd(7*k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(2, 'red')
update()
done()