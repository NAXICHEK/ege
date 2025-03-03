from turtle import *
screensize(3000, 3000)
tracer(0)
k = 10
up()
for i in range(11):
    fd(2*k)
    dot(5, 'black')
    backward(4*k)
    dot(5, 'black')
    fd(2*k)
    fd(2*k)
done()
