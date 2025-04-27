from turtle import *
screensize(3000, 3000)
k = 10
tracer(0)

for i in range(9):
    fd(22*k)
    right(90)
    fd(6*k)
    right(90)
up()
fd(1*k)
right(90)
fd(5*k)
left(90)
down()
for i in range(9):
    fd(53*k)
    right(90)
    fd(75*k)
    right(90)
up()
for x in range(-200, 200):
    for y in range(-200, 200):
        setpos(x*k, y*k)
        dot(2, 'red')

update()
done()
