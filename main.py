import turtle
from math import atan, tan, cos, acos, sin, asin, pi, e
# Make the dimensions editable. 
def draw(equation):
	TICK_MARK_LENGTH = 10
	FIELD_LINE_LENGTH = 18
	turtle.pu()
	turtle.goto(turtle.window_width()/-2, 0)
	turtle.setheading(0)
	turtle.pd()
	turtle.forward(turtle.window_width())
	turtle.pu()
	turtle.goto(0, turtle.window_height()/2)
	turtle.setheading(270)
	turtle.pd()
	turtle.forward(turtle.window_height())
	for i in range(1, 21):
		turtle.pu()
		turtle.goto((turtle.window_width()/-2)+((turtle.window_width()/20)*i), TICK_MARK_LENGTH/2)
		turtle.seth(270)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
	for i in range(1, 21):
		turtle.pu()
		turtle.goto(TICK_MARK_LENGTH/2, (turtle.window_height()/2)-((turtle.window_height()/20)*i), )
		turtle.seth(180)
		turtle.pd()
		turtle.forward(TICK_MARK_LENGTH)
	for x in range(-10, 11):
		for y in range(-10, 11):
			turtle.pu()
			turtle.goto((turtle.window_width()/20)*x, (turtle.window_height()/20)*y)
			turtle.seth((180/pi)*(atan(equation(x, y))))
			turtle.forward(FIELD_LINE_LENGTH/2)
			turtle.pd()
			turtle.backward(FIELD_LINE_LENGTH)
eqn = eval("lambda x, y: "+input("Input your equation in proper python with x and y as variables: "))
turtle.speed(0)
draw(eqn)