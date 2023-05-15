# Wish

I usually doodle it and I wanted to recreate it in Python (see [output](#spiral-triangle)). 

# Here's what the code is doing

1. I created a drawing board using turtle module's `Screen` method. I changed my turtle's shape to circle using `shape` method. I moved the turtle to x=-90, y=-90 using `penup`, `goto`, `pendown` method. I have used `speed()` method with `0` argument, as `0` makes the turtle move fastest possible. 
2. Then, I defined polygon parameters. `n` denotes the number of sides in a polygon. `n=3` denotes that it's a triangle. `polygon_turn_angle` is exterior angle of the polygon.
3. See illustred image [Construction of Spiral triangle](#construction-of-spiral-triangle) to get the definition of `polygon_side_length`, `segment_length` variables.
4. Initially, triangle's first side is drawn using turtle module's `forward` method. **The trick to draw the spiral triangle is**, when I am drawing the second side of triangle, I am not drawing it in one go. 
    1. Firstly, I drew the `segment_length`. Here I used turtle's `position` method to get current location's x,y co-ordinates. I stored this in the list `pt`. 
    2. Then I continued and marched forward `polygon_side_length-segment_length` distance to complete the second side of triangle. 
    3. Similar actions are done when drawing the third side.
5. To draw the first inward line segment (`side_length_1`) of the spiral, I utilized that point whose x,y co-ordinates I stored in `pt` list while drawing second side of the triangle. After drawing the third side of the triangle: 
    1. I utilized turtle module's `towards` method to get the angle towards the point on the second side of triangle. 
    2. Then I used `left` method to orient the turtle's head towards that point on the second side of triangle. 
    3. Finally I used `forward` method to march and complete the spiral `side_length_1`. Step 4's actions are executed in between to get the information of point on this `side_length_1` as this will help to draw the next 'side_length_1'.
    4. I am doing this over and over in `for` loop. I used `if` conditional to `break` out of the `for` loop if spiral's `side_length_1` becomes < 1.

### Construction of spiral triangle

![spiral_triangle_construction](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/02e61e1f-4122-4d04-8f83-d184ccfec8cd)


# Spiral triangle

![spiral_triangle_output](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/53cdc3ba-c96a-47db-8c38-220a5164a6bc)


