fibonacciNum = input("Choose a fibonacci number from the fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21, 33): ")


'''
import turtle

x = list(range(0, 100))

wn = turtle.Screen()
#wn.screensize()
#wn.setup(width = 1.0, height = 1.0)

pam = turtle.Turtle()
pam.pu()
pam.setx(0)
pam.sety(-250)
pam.pd()
pam.write('Fibonacci Tree', align = 'center', font = ('Arial', 14, 'italic'))
pam.speed(0)
pam.penup()
pam.sety(-200)
pam.pendown()

'''branches'''
def verticalBranch(x, y, heading = 90, distance = 50):
    pam.pu()
    pam.setx(x)
    pam.sety(y)
    pam.setheading(heading)
    pam.pd()
    pam.fd(distance)
    return pam.xcor(), pam.ycor()

def leftBranch(x, y, heading = 90, distance = 50, angle = 45):
    pam.pu()
    pam.setx(x)
    pam.sety(y)
    pam.setheading(heading)
    pam.pd()
    pam.lt(angle)
    pam.fd(distance)
    return pam.xcor(), pam.ycor()

def rightBranch(x, y, heading = 90, distance = 50, angle = 45):
    pam.pu()
    pam.setx(x)
    pam.sety(y)
    pam.setheading(heading)
    pam.pd()
    pam.rt(angle)
    pam.fd(distance)
    return pam.xcor(), pam.ycor()

def bothBranches(x, y, heading = 90, distance = 50*2**0.5, angle = 45):
    l = leftBranch(x, y, heading, distance, angle)
    r = rightBranch(x, y, heading, distance, angle)
    return l, r

pam.pensize(21)
verticalBranch(pam.xcor(), pam.ycor(), distance = 70)

wn.exitonclick()
'''
