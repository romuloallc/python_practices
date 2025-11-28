import turtle
import math

bob = turtle.Turtle()
print(bob)

def arc(t, r, a):
    circ = 2 * math.pi * r
    for i in range(int(circ)+1):
        t.fd(a/circ)
        t.lt(a/circ)
    
    turtle.mainloop()


arc(bob, 5, 270)
