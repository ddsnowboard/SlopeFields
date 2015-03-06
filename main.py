import turtle
from math import atan, tan, cos, acos, sin, asin, pi, e, fabs
def draw(equation, dims):
	TICK_MARK_LENGTH = 10
	FIELD_LINE_LENGTH = 18
	SPACE_FROM_LABEL = 15
	RESOLUTION = 20
	if RESOLUTION % 2 != 0:
		raise Exception("RESOLUTION must be even")
	xlen = dims['x']
	ylen = dims['y']
	deltax = xlen/RESOLUTION
	deltay = ylen/RESOLUTION
	width = turtle.window_width()-55
	height = turtle.window_height()-30
	xratio = width/xlen
	yratio = height/ylen
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
	for i in range(RESOLUTION+1):
		turtle.pu()
		turtle.goto((width/-2)+((width/RESOLUTION)*i), TICK_MARK_LENGTH/2)
		turtle.seth(270)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
		turtle.pu()
		turtle.forward(SPACE_FROM_LABEL)
		turtle.write(round((-1*dims['x']/2)+(dims['x']/RESOLUTION)*i, 2), False, "center")
	for i in range(RESOLUTION+1):
		turtle.pu()
		turtle.goto(TICK_MARK_LENGTH/2, (height/-2)+((height/RESOLUTION)*i))
		turtle.seth(180)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
		if i != RESOLUTION/2:
			turtle.left(25)
			turtle.pu()
			turtle.forward(SPACE_FROM_LABEL)
			turtle.write(round((dims['y']/-2)+(dims['y']/RESOLUTION)*i, 2), False, "center")
	turtle.pen(pencolor="green")
	for x in range(int(RESOLUTION/-2), int(RESOLUTION/2+1)):
		for y in range(int(RESOLUTION/-2), int(RESOLUTION/2+1)):
			currx = x * deltax
			curry = y * deltay
			turtle.pu()
			turtle.goto(currx * xratio, curry * yratio)
			try:
				turtle.seth((180/pi)*(atan(equation(x, y))))
			except ZeroDivisionError:
				turtle.seth(90)
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