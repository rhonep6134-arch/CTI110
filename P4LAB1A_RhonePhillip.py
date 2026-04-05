import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.pensize(3)

side = 100

# ----------- DRAW FILLED SQUARE (FOR LOOP) -----------
t.color("white")
t.fillcolor("tan")  # house body color
t.begin_fill()

for i in range(4):
    t.forward(side)
    t.left(90)

t.end_fill()

# ----------- MOVE TO TOP -----------
t.left(90)
t.forward(side)
t.right(90)

# ----------- DRAW FILLED TRIANGLE (WHILE LOOP) -----------
t.fillcolor("red")  # roof color
t.begin_fill()

count = 0
while count < 3:
    t.forward(side)
    t.left(120)
    count += 1

t.end_fill()

t.hideturtle()
screen.exitonclick()
t.fillcolor("tan")
t.begin_fill()
# draw shape
t.end_fill()
t.fillcolor("red")
t.begin_fill()
# draw shape
t.end_fill()
