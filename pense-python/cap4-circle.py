import turtle
import math

bob = turtle.Turtle()
print(bob)

def circle(t, r):
    circ = 2 * (math.pi) * r
    for i in range(int(circ)+1):
        t.fd(circ)
        t.lt(360/circ)
    
    turtle.mainloop()


circle(bob, 5)
