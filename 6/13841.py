import turtle as t
k = 20
t.tracer(0)
for i in range(7):
    t.down()
    t.forward(10*k)
    for _ in range(4):
        t.seth(90)
        t.circle(2*k,-180)
    t.backward(10*k)
    for _ in range(4):
        t.seth(90)
        t.circle(-2*k, 180)
t.up()
for i in range(-15, 15):
    for j in range(-15, 15):
        t.setpos(i*k, j*k)
        t.dot(2, 'red')
t.done()