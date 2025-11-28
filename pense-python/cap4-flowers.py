import turtle
import math

bob = turtle.Turtle()
print(bob)

def arc(t, r, a):
    circ = 2 * math.pi * r * a /360
    n = int(circ / 3) + 1
    step = a / n
    for i in range(n):
        t.fd(circ / n)
        t.lt(step)

def petala(t, r, a):
    for i in range(2):
        arc(t, r, a)
        t.lt(180 - a)

def flowers(t, n, r, a):
    for i in range(n):
        petala(t, r, a)
        t.lt(360 / n)
    
    turtle.mainloop()

flowers(bob, 3, 100, 100)
