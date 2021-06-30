import turtle as turtle
turtle.bgcolor('black')
turtle.pensize(1)
turtle.speed(0)

for i in range(10):
    for colours in ("red","magenta","blue","cyan","green","yellow","white"):
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.done()

