import turtle

x = list(range(0,400))

window = turtle.Screen()
window.screensize()
window.setup(width = 1.0, height = 1.0)
judith = turtle.Turtle()
judith.pensize(6)
judith.pencolor('brown')

'''trunk'''
judith.setheading(90)
judith.pu()
judith.setx(-250)
judith.sety(-250)
judith.pd()
judith.write('Fractal Tree', align = 'center', font = ('Arial',14,'italic'))
judith.pu()
judith.setx(-250)
judith.sety(-200)
judith.pd()
judith.fd(100)
prevX = judith.xcor()
prevY = judith.ycor()
prevH = judith.heading()

def fractalY1(x, y, heading, distance=30, angle=20):
    judith.pu()
    judith.setx(x)
    judith.sety(y)
    judith.setheading(heading)
    judith.pd()
    judith.lt(angle)
    judith.fd(distance)
    return judith.xcor(), judith.ycor(), judith.heading()

def fractalY2(x, y, heading, distance=30, angle=-20):
    judith.pu()
    judith.setx(x)
    judith.sety(y)
    judith.setheading(heading)
    judith.pd()
    judith.lt(angle)
    judith.fd(distance)
    return judith.xcor(), judith.ycor(), judith.heading()

def completY(x, y, heading, distance=30):
    i1 = fractalY1(x, y, heading, distance)
    i2 = fractalY2(x, y, heading, distance)
    return i1, i2

x[0] = completY(prevX, prevY, prevH)
for i in range(0, 62, 2):
    if i > 5 and i < 13:
        judith.pencolor('green')
        judith.speed(0)
        judith.pensize(4)
        x[i+1] = completY(*x[int(i/2)][0], distance = 35)
        x[i+2] = completY(*x[int(i/2)][1], distance = 35)
    elif i >= 13:
        judith.speed(0)
        judith.pencolor('magenta')
        judith.pensize(3)
        x[i+1] = completY(*x[int(i/2)][0], distance = 10)
        x[i+2] = completY(*x[int(i/2)][1], distance = 10)
    else:
        judith.speed(0)
        x[i+1] = completY(*x[int(i/2)][0], distance = 50)
        x[i+2] = completY(*x[int(i/2)][1], distance = 50)

window.exitonclick()
