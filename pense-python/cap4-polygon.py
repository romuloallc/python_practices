import turtle

bob = turtle.Turtle()
print(bob)

def polygon(t, len, n):
    for i in range(n):
        t.fd(len)
        t.lt(360/n)
    
    turtle.mainloop()


polygon(bob, 50, 8)
