from turtle import *
k = 30
screensize(3000, 3000)
tracer(0)
right(90)
for i in range(7):
    right(45)
    fd(11*k)
    right(45)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(2, 'red')
update()
done()