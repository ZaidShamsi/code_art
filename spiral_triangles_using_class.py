import turtle
import math

drawing_board = turtle.Screen()
# drawing_board.setup(width = 1.0, height = 1.0)

turtle.shape("circle")
turtle.shapesize(0.1, 0.1)
turtle.speed(0)

class Triangle():
    """docstring for Triangle."""

    n = 3

    def __init__(self, polygon_side_length):
        self.polygon_side_length = polygon_side_length
        self.polygon_turn_angle = 360/self.n
        self.segment_length = self.polygon_side_length/10

    def pen_position(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    def draw_equilateral(self, orientation = 1):
        # orientation -> clockwise/anti-clockwise; up/down; 1/-1
        # pt -> postion (x, y)
        # initializing list to store the position co-ordinates
        # these will be used to connect the dots
        pt = []
        eq_pt = []

        # drawing the polygon
        eq_pt.append(turtle.position())
        turtle.forward(self.polygon_side_length)
        eq_pt.append(turtle.position())
        for i in range(self.n-1):
            turtle.left(orientation * self.polygon_turn_angle)
            turtle.forward(self.segment_length)
            pt.append(turtle.position())
            turtle.forward(self.polygon_side_length-self.segment_length)
            eq_pt.append(turtle.position())
        turtle.left(orientation * self.polygon_turn_angle)

        return pt, eq_pt

    def draw_spiral(self, pt):
        # spiral triangle logic
        side_length = []
        angle = []
        for i in range(150):
            for j in range(self.n-1):
                side_length_1 = turtle.distance(pt[j])
                segment_length = side_length_1/10
                angle_1 = turtle.towards(pt[j])
                turtle.left(angle_1)
                turtle.forward(segment_length)
                pt[j] = turtle.position()
                turtle.forward(side_length_1-segment_length)
                turtle.right(angle_1)
            if side_length_1 < 10:
                print("Breaking out of the spiral loop at i = ", i, "as segment length is less than 1 now.")
                break

triangle_1 = Triangle(120)
pt, eq_pt =  triangle_1.draw_equilateral(orientation = 1)
triangle_1.draw_spiral(pt)

print("Done")

drawing_board.exitonclick()
