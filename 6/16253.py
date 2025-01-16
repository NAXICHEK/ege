from turtle import *
screensize(3000, 3000)
k = 5
right(45)
for i in range(10):
    right(45)
    fd(203*k)
    right(45)
up()
backward(40*k)
right(45)
down()
for i in range(5):
    fd(20*k)
    left(90)
up()
for x in range(-200, 250):
    for y in range(-235, -200):
        setpos(x*k, y*k)
        dot(2, 'red')
done()