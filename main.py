import turtle
from math import atan, tan, cos, acos, sin, asin, pi, e, fabs
from WillsLib import myRange
def draw(equation, dims):
	TICK_MARK_LENGTH = 10
	FIELD_LINE_LENGTH = 18
	SPACE_FROM_LABEL = 15
	width = turtle.window_width()-55
	height = turtle.window_height()-30
	turtle.pu()
	turtle.goto(width/-2, 0)
	turtle.setheading(0)
	turtle.pd()
	turtle.forward(width)
	turtle.pu()
	turtle.goto(0, height/2)
	turtle.setheading(270)
	turtle.pd()
	turtle.forward(height)
	for i in range(21):
		turtle.pu()
		turtle.goto((width/-2)+((width/20)*i), TICK_MARK_LENGTH/2)
		turtle.seth(270)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
		turtle.pu()
		turtle.forward(SPACE_FROM_LABEL)
		turtle.write((-1*dims['x']/2)+(dims['x']/20)*i, False, "center")
	for i in range(21):
		turtle.pu()
		turtle.goto(TICK_MARK_LENGTH/2, (height/-2)+((height/20)*i))
		turtle.seth(180)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
		if i != 10:
			turtle.left(25)
			turtle.pu()
			turtle.forward(SPACE_FROM_LABEL)
			turtle.write((dims['y']/-2)+(dims['y']/20)*i, False, "center")
	turtle.pen(pencolor="green")
	for x in myRange(dims['x']/-2, (dims['x']/2)+1, dims['x']/20):
		for y in myRange(dims['y']/-2, dims['y']/2, dims['y']/20):
			print(x, y)
			turtle.pu()
			turtle.goto((width/dims['x'])*x, (width/dims['y'])*y)
			turtle.seth((180/pi)*(atan(equation(x, y))))
			turtle.forward(FIELD_LINE_LENGTH/2)
			turtle.pd()
			turtle.backward(FIELD_LINE_LENGTH)
eqn = eval("lambda x, y: "+input("Input your equation in proper python with x and y as variables: "))
dims = {}
dims['x'], dims['y'] = int(input("How wide should it be? ")), int(input("How high should it be? "))
turtle.speed(0)
turtle.hideturtle()
draw(eqn, dims)
input()