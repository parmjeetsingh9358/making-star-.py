import turtle

col=('yellow','red','green','orange','white')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(5)

for i in range(150):

	t.color(col[i%5])
	t.forward(i*4)
	t.left(150)
	t.width(2)