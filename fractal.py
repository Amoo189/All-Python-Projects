'''def F(n):
    if n <= 2:
        return 1
    return F(n-1)+F(n+1)
print(F(10))'''

'''def F2(n):
    a = [0] * n
    a[0] = 1
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a
print(F2(70)) '''

from turtle import *
shape('turtle')
penup()
hideturtle()
goto(-460, 20)
pendown()
pensize(1)
color('blue')
#write('Saleh Amoo')
Turtle()
speed(20)
def draw(size, step):
    if step == 0:
        forward(size)
        return
    draw(size/3, step-1)
    left(60)
    draw(size/3, step-1)
    right(120)
    draw(size/3, step-1)
    left(60)
    draw(size/3, step-1)
for I in range(3):
    draw(300, 3)
    right(120)
hideturtle()
done()