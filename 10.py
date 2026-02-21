import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(4)
t.speed(90)
t.width(5)
t.shapesize(3,3,1)
for i in range(36):
	for j in range(10):
		t.forward(100)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)
		t.left(36)		
	t.left(36)
turtle.done