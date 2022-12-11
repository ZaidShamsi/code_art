import turtle

drawing_board = turtle.Screen()
pen = turtle.Turtle()


def draw_square(side_length):
    for i in range(4):
        pen.color('green')
        pen.forward(side_length)
        pen.right(90)

fibonacci_side_length = [1, 1, 2, 3, 5, 8]
size_factor = 15
fibonacci_side_length = [size_factor*side_length for side_length in fibonacci_side_length]
fibonacci_side_length_reverse = fibonacci_side_length.copy()
fibonacci_side_length_reverse.reverse()
fibonacci_side_length.extend(fibonacci_side_length_reverse)

pen.pensize(2)
pen.speed(10)
pen.color('green')
i = 0
for side_length in fibonacci_side_length:
    draw_square(side_length)
    if i > 2 and i < len(fibonacci_side_length)-3:
        pen.color('red')
    pen.right(180)
    pen.tilt(180)
    pen.circle(side_length, -90)
    pen.right(180)
    pen.tilt(180)
    i = i + 1


drawing_board.exitonclick()
