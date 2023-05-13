import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor('black')
judith = turtle.Turtle()
judith.color('white')
judith.pensize(2)
judith.speed(0)

def star(x, y, distance = 20, angle = 30, headingAngle = 90):
    judith.setheading(headingAngle)
    judith.penup()
    judith.setx(x)
    judith.sety(y)
    judith.pendown()
    judith.left(angle)
    judith.fd(distance)
    xco = judith.xcor()
    yco = judith.ycor()
    judith.right(90+angle)
    judith.fd(distance)
    xco = (xco + judith.xcor())/2
    yco = (yco + judith.ycor())/2
    judith.right(90+angle)
    judith.fd(distance)
    judith.penup()
    judith.setx(xco + distance*.3*math.cos(3.14*headingAngle/180))
    judith.sety(yco + distance*.3*math.sin(3.14*headingAngle/180))
    judith.pendown()
    judith.fd(distance)
    judith.left(90+angle)
    judith.fd(distance)
    judith.left(90+angle)
    judith.fd(distance)
    judith.setheading(headingAngle)

for i in range(1, 40):
    factor = random.randrange(1,5)
    x = random.randrange(-300, 300)
    y = random.randrange(-250, 250)
    ha = random. randrange(0, 90)
    star(x, y, distance=20/factor, headingAngle = ha)
wn.exitonclick()
