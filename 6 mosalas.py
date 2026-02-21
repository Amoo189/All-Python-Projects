import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(90)
t.width(5)
for i in range(6):
	for j in range(3):
		t.forward(200)
		t.left(60)
		t.left(60)
	t.left(60)
turtle.done()