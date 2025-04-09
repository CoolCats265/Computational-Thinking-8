import turtle
t = turtle.Turtle()
t.penup()
# Teleport turtle
t.goto(-25, -25)
t.pendown()

# Change colors
colors = ["powderblue", "aquamarine", "yellowgreen", "peachpuff"]
# Repeat 200 times
for i in range(200):
    t.color(colors[ i % 4 ])
    t.forward(145 + i)
    t.left(119)
    t.forward(120)
    t.left(100)
    t.speed(10)

turtle.exitonclick()