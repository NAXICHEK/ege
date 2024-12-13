import turtle as t
t.tracer(0)
k = 20
t.color('red')
t.left(90)
t.right(60)
for _ in range(2):
    t.fd(10*k)
    t.right(120)
    t.fd(5*k)
    t.right(240)
t.right(120)
t.fd(3*k)
t.right(90)
t.fd((20*(3**0.5))*k)
t.right(90)
t.fd(8*k)
t.right(120)
for _ in range(2):
    t.fd(10*k)
    t.left(120)
    t.fd(5*k)
    t.left(240)
t.up()
for i in range(-100, 100):
    for j in range(-100, 100):
        t.setpos(i*k, j*k)
        t.dot(2, 'green')
t.done()