from turtle import *
tracer(0)
screensize(3000, 3000)
k = 30
for i in range(2):
    fd(24*k)
    right(90)
    fd(10*k)
    right(90)
fd(3*k)
left(90)
fd(13*k)
right(90)
for i in range(2):
    fd(9*k)
    right(90)
    fd(32*k)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(2, 'red')
update()
done()