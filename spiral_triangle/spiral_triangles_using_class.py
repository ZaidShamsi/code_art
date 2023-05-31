import turtle
import numpy as np

drawing_board = turtle.Screen()
drawing_board.setup(width = 1.0, height = 1.0)

turtle.shape("circle")
turtle.shapesize(0.1, 0.1)
turtle.speed(0)

class Triangle():
    """This is hardcoded to be a triangle. It can be any polygon as long as you change the n."""

    n = 3

    def __init__(self, polygon_side_length):
        self.polygon_side_length = polygon_side_length
        self.polygon_turn_angle = 360/self.n
        self.segment_length = self.polygon_side_length/10


    def draw_equilateral(self, orientation = 1):
        # orientation -> clockwise is 1/anti-clockwise is -1
        # pt -> postion (x, y)
        # initializing list to store the position co-ordinates
        # these will be used to draw the spiral
        pt = []

        # drawing the polygon
        turtle.forward(self.polygon_side_length)

        for i in range(self.n-1):
            turtle.left(orientation * self.polygon_turn_angle)
            turtle.forward(self.segment_length)
            pt.append(turtle.position())
            turtle.forward(self.polygon_side_length-self.segment_length)
        turtle.left(orientation * self.polygon_turn_angle)

        return pt

    def draw_spiral(self, pt):
        # spiral triangle logic
        for i in range(150):
            for j in range(self.n-1):
                side_length_1 = turtle.distance(pt[j])
                segment_length = side_length_1/10
                angle_1 = turtle.towards(pt[j])
                turtle.setheading(angle_1)
                turtle.forward(segment_length)
                pt[j] = turtle.position()
                turtle.forward(side_length_1-segment_length)
                # turtle.right(angle_1)
            if side_length_1 < 10 or side_length_1 > 2*self.polygon_side_length:
                print("Breaking out of the spiral loop at i = ", i, "as segment length is less than 1 now.")
                break

triangle_1 = Triangle(120)

# playaround with the num, say change it to 7
for i in np.linspace(0, 360, num=5):
    turtle.setheading(i)
    pt =  triangle_1.draw_equilateral(orientation = 1)
    triangle_1.draw_spiral(pt)


print("Done")

drawing_board.exitonclick()
