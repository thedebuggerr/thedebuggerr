import turtle as t 
t.bgcolor("black")
t.pencolor("red")
t.pensize(0)
t.speed(0)

for i in range(1,451):
    t.backward(10-i)
    t.right(101)
    i=i+1
t.done()