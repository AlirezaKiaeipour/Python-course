import turtle

t = turtle.Pen()
turtle.bgcolor("yellow")
t.shape("turtle")
t.color("green")

h= 10
n=3
x=-6
y=6


for i in range(10):
    for j in range(n):
        t.forward(h)
        t.right(360/n)
    n+=1
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    h+=10
    x-=5
    y+=17




    


