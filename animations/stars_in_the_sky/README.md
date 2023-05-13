# The idea

Imagine a night sky filled with sparkling stars. This is what I had in my mind and I wanted to replicate it in Python. (A nice idea to kick start I think :))

# Here's what the code is doing

1. Firstly, I created a black drawing screen for my turtle. I called my turtle 'Judith'. 
2. In Python's turtle module we have the capability to
    1.  Capture Judith's traverse path (we have the control over to capture certain traversed path and leave some as undiscovered for others :))
    2.  Instruct Judith in which direction to move and how far to move.
    3.  All the turtle methods used can be found in the ![documentation](https://docs.python.org/3/library/turtle.html)
4. Secondly, I defined a function called star (this is the crux of the code). Let's understand this function. To create a star we will be using equilateral triangles. Keeping things simple, Turtle is at x=0, y=0.
    1. Judith's head is kept in North direction via 'setheading(90 degrees)'. She is moved to desired location via 'setx, sety' and her head is oriented left 30 degrees vis 'left(30)'. Now Judith is facing 30 degrees West of North.
    2. Judith is marched forward distance=20 units. Here Judith's x,y co-ordinates are remembered. We will be using it to find the starting point for our next triangle to complete the star.
    3. Now, Judith is turned right 30 degrees + 90 degrees. She is facing East now. She is marched forward 20 units. Here, mid-point is found between previous x,y co-ordinates and current x,y co-ordinates. This is the reference point for the starting point of the next triangle.
    4. Mid-point between $x_1,y_1$ and $x_2,y_2$, $$x = {{x_1+x_2} \over 2}, y = {{y_1+y_2} \over 2}$$
    5. Rest all is bread-and-butter, turn and move to complete the second triangle.
6. Finally, I called this star function in for loop to create many stars.
      1. I am generating random x,y (initial locations) to have stars distributed in the sky.
      2. I defined a variable called 'factor' to get the feel that some stars are distant so they are appearing small.
      3. I defined a variable called 'heading angle' so that not all stars are headed 90 degrees, some should be tilted as well.

![star_function_explained](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/46e6702b-b70f-465b-901b-9f857bdaea04)


## Output

![stars_in_the_sky](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/58a678e6-129f-42f8-887e-8a4be1d1a1bc)
