import turtle

bob = turtle.Turtle()
print(bob)

def square(t, len):
    for i in range(4):
        t.fd(len)
        t.lt(90)
    
    turtle.mainloop()


square(bob, 10)
