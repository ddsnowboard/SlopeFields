import turtle
def drawCoordinates():
	TICK_MARK_LENGTH = 10
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
		
# eqn = eval("lambda x: "+input("Input your equation in proper python with x as variable: "))
turtle.speed(0)
drawCoordinates()