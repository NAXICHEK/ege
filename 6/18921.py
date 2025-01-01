from turtle import *
tracer(0)
screensize(3000, 3000)
k = 25

for i in range(13):
    fd(13*k)
    right(90)
    fd(5*k)
up()
right(90)
fd(7*k)
left(90)
fd(10*k)
down()
for i in range(23):
    fd(8*k)
    left(90)
    fd(11*k)
    left(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'red')
done()