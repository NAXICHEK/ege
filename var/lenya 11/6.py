from turtle import *
screensize(3000, 3000)
tracer(0)
k = 15
fd(30*k)
left(60)
fd(24*k)
right(240)
fd(54*k)
left(120)
fd(24*k)
left(60)
up()
fd(30*k)
right(90)
fd(20*k)
left(90)
down()
for i in range(17):
    fd(6*k)
    left(90)
    fd(80*k)
    left(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(5, 'red')
done()