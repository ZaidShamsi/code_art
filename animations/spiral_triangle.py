import turtle
import math

drawing_board = turtle.Screen()
# drawing_board.setup(width = 1.0, height = 1.0)

turtle.shape("circle")
turtle.shapesize(0.1, 0.1)
turtle.speed(0)
turtle.penup()
turtle.goto(-90, -90)
turtle.pendown()

# polygon parameters
# n is defined as the number of sides polygon have
# try, change and play with this n parameter
n = 3
polygon_side_length = 180
polygon_turn_angle = 360/n

# segemnt length is different from polygon side length
# segemnt is defined as the line that is traversed after the polygon is completely drawn
# segment length parameters
segment_length = polygon_side_length/10

# pt -> postion (x, y)
# initializing list to store the position co-ordinates
# these will be used to connect the dots
pt = []

# drawing the polygon
turtle.forward(polygon_side_length)
for i in range(n-1):
    turtle.left(polygon_turn_angle)
    turtle.forward(segment_length)
    pt.append(turtle.position())
    turtle.forward(polygon_side_length-segment_length)
turtle.left(polygon_turn_angle)

# spiral triangle logic
side_length = []
angle = []
for i in range(150):
    for j in range(n-1):
        side_length_1 = turtle.distance(pt[j])
        segment_length = side_length_1/10
        angle_1 = turtle.towards(pt[j])
        turtle.left(angle_1)
        turtle.forward(segment_length)
        pt[j] = turtle.position()
        turtle.forward(side_length_1-segment_length)
        turtle.right(angle_1)
    if side_length_1 < 1:
        print("Breaking out of the spiral loop at i = ", i, "as segment length is less than 1 now.")
        break

print("Done")

drawing_board.exitonclick()
