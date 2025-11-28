import turtle
import math

bob = turtle.Turtle()
print(bob)

def pie(t, len, angle):
    t.fd(len)
    t.lt(180 - (angle / 2))
    base = 2 * len * math.sin(math.radians(angle / 2))
    t.fd(base)
    t.lt(180 - (angle / 2))
    t.fd(len)
    t.lt(180 + angle)


def polygon(t, len, n):
    angle = 360 / n
    for i in range(n):
        pie(t, len, angle)


polygon(bob, 50, 8)

turtle.done()
