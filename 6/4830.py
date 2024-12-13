from turtle import *
tracer(0)
down()
k = 5
rt(45)
for i in range(25):
    fd(55*k)
    rt(90)
up()
for i in range(-100, 100):
    for j in range(-100, 100):
        setpos(i*k, j*k)
        dot(2, 'red')
done()