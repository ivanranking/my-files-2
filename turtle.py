import turtle

turtle.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
 turtle.pencolor(colors[i % 6])
turtle.width(i / 100 + 1)
turtle.forward(i)
turtle.left(59)

turtle.done()
