import turtle as turtle
turtle.speed(0)
turtle.pencolor("red")
turtle.bgcolor("black")
turtle.pensize(1)
for i in range(1,200):
    turtle.forward(i)
    turtle.left(i-1)
    i=i+1
turtle.done()
