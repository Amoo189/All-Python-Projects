import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.width(5)
t.speed(90)
for i in range(24):
	for j in range(12):
		t.forward(100)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
	t.left(45)
t.goto(100,-60)
turtle.done()