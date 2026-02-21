import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.fillcolor("blue") 
t.width(3)
t.speed(60)
for i in range(8):
	for j in range(8):
		t.forward(100)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
		t.left(45)
	t.left(45)
turtle.done()