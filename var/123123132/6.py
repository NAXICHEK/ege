from turtle import *
tracer(0)
k = 10
screensize(3000, 3000)

for i in range(8):
    fd(16*k)
    right(90)
    fd(22*k)
    right(90)
up()
fd(5*k)
right(90)
fd(5*k)
left(90)
down()
for i in range(8):
    fd(52*k)
    right(90)
    fd(77*k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4, 'red')
done()