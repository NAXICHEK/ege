import turtle as t
t.tracer(0)
k = 20 #коэффициент для увеличения масштаба
for i in range(5):
    t.seth(0)
    t.circle(5*k,180)
    t.seth(90)
    t.circle(5*k,180)
    t.seth(180)
    t.circle(5*k,180)
    t.seth(270)
    t.circle(5*k,180)
t.penup()
for x in range(-15,6,1):
    for y in range(-5,16):
        t.goto(x*k , y*k )
        t.dot(2, 'red')
t.penup()
t.done()