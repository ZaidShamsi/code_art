# Fibonacci Spiral heart

## Wish

I might have seen it on pinterest or instagram and thought to recreate it with Python (see [output](#output))

## turtle.circle() method

- As you would have deduced correctly, this method will draw a circle. If you want to draw a semi-circle or a quadrant of a circle you can still use this very same method. 
- `turtle.circle` takes two arguments --> `turtle.circle(raidus, extent)`. Here extent can be defined as by how much degrees you want the arc to be drawn.
- So, if you want to draw a quadrant, `turtle.circle(radius, 90)` will do it. For a semi-circle, `turtle.circle(raidus, 180)` would suffice. 
- Now there are two orientations of drawing a circle: clockwise and anti-clockwise. The second argument in `turtle.circle` method and turtle's heading angle governs the orientation and position (see [turtle circle orientation](#turtle-circle-orientation)).

### turtle circle orientation


![turtle_circle_orientation](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/c81b30c6-c80b-4b5d-a610-2631a44eeaf8)


## Here's what the code is doing

1. I created a function that draws a square. I named it `draw_square`
2. I am calling `draw_square` function in a `for` loop. Because `draw_square` leaves the turtle headed in East. I am calling:
    1. `turtle.right(180)` to head turtle in West (see [turtle circle orientation](#turtle-circle-orientation) for reasoning behind it).
    2. `turtle.tilt(180)` to flip it. `tilt` does not change orientation where the turtle is headed.
    3. `turtle.circle(radius, -90)` to draw quadrant of circle.
    4. Then again I am calling `turtle.right(180)` and `turtle.tilt(180)`. The purpose is same as stated in Pt 2.1-2.3 (If you happen to try this code, try commenting out `right` and `tilt` methods to see how the code behaves. It is just silly me trying to make my code work :))
3. I have used `if-else` block to change the color. Red is for heart.

### draw_square function

Notice that after the function is called to draw square, turtle is left headed in East.

![draw_square](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/c9a7adab-6d4d-45f5-aae8-324c1e193f30)


## Output

![fibonacci_spiral_heart](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/35d9ac18-e3e7-4ccc-9997-607c98c6fbd0)

## Future work

- I have hardcoded the fibonacci series, I can attempt to write a function that generates fibonacci series based on the number of elements taken as input from the user (it will certainly effect the orientation in which the heart will display in the output, it will then be at discretion of user's input).
- `enumerate` method can be used in `for` loop.
