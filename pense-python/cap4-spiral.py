import turtle
import math

bob = turtle.Turtle()
print(bob)

def circles(t, n, r):
    grade = r / n
    for i in range(n):
        step = grade * (i + 1)
        t.goto(0 , -step)
        t.circle(step)    


def gradio(t, n, angle, r):
    t.pendown()
    for i in range(n):
        t.fd(r)
        t.goto(0, 0)
        t.lt(angle)
    circles(t, n, r)

def spiral(t, n, r):
    angle = (360 / n)
    gradio(t, n, angle, r)

    t.goto(0, 0)
    t.color("red") 

    for i in range(n * r):
        theta = (i / (n * r)) * math.pi * 2
        radius = (r / (n * r)) * i
        x = (radius) * math.sin(theta)
        y = (radius) * math.cos(theta)
        t.goto(x, y)


spiral(bob, n=5, r=200)


turtle.done()
