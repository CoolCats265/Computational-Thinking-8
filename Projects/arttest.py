# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.color("purple")
t.pendown()

for i in range(100):
    t.forward(40)
    t.left(80)
    t.forward(30)
    t.left(80)
    t.forward(37)
    t.left(85)
    t.forward(30)
    t.left(73)
    t.forward(40)

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
