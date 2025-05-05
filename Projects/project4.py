# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 150
x2 = -200
y2 = 50
x3 = -200
y3 = -50
x4 = -200
y4 = -150
# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("fall")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("kitten",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("sodacan",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# Sprite 1 is probably the second fastest, higher range than Sprite 3 and most likely spits out a number higher than 9, but has a lower range than Sprite 2
# Sprite 2 has a higher range than Sprites 1 and 2, and will usually put out numbers bigger than 9
# Sprite 3 will most likely get numbers lower than nine, and has a lower range than Sprites 1 and 2
# Sprite 4 always will give you nine, which is probably going to be bigger than Sprite 3 but will rarely be bigger than Sprites 1 and 2
for i in range(40):
	x1 += random.randint(4, 17)
	x2 += random.randint(6, 18)
	x3 += random.randint(2, 14)
	x4 += 9
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("Basketball wins!")
elif x2 >= x3 and x2>= x4:
	print("Cat wins!")
elif x3 >= x4:
	print("Fish wins!")
else:
	print("Soda Can wins!")




turtle.exitonclick()




