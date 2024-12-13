import turtle as t
t.tracer(0)
k = 18
t.screensize(3000, 2000)
t.down()
for i in range(5):
    t.right(45)
    t.forward(10*k)
    t.right(45)
for i in range(6):
    t.forward(20*k)
    t.right(90)
t.up()
for i in range(-50, 50):
    for j in range(-50, 50):
        t.setpos(i*k, j*k)
        t.dot(2, 'red')
t.done()
# 436