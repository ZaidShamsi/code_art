# Idea

I might have stumbled on some articles or blogs about Mathematics in Nature, that could have initiated this work. But more so to my frequent visits to the countryside in the past two years, I can see it's influence in my photography and here as well :D. 

# Here's what the code is doing

Imagine a tree, it has a trunk, branches, leaves and flowers. The tree that I have drawn (see [Output](#output) is having two branches from each node. I am using Python's turtle module. All the methods of turtle module can be found in the [documentation](https://docs.python.org/3/library/turtle.html). Few of the methods that I have used are below:

1. left or lt: This method is used turn Judith's head (I called my turtle Judith) left by the required degrees. Similarly, right method is used to turn right.
2. penup or pu: When this method is applied Judith's traversed path will not be captured. Similary, pendown or pd is used to reverse the effect of penup.
3. setheading is used to orient the turtle's head in the specified direction (direction is provided in terms of degrees measured from x axis)
4. xcor, ycor methods are used to get x,y co-ordinates of turtle's current location.
5. setx, sety methods are used to move Judith to the desired location.

Let's get back to the code:

1. Firstly, I created a drawing board for my turtle.
2. Then I drew a trunk. Now, this end point should be remembered (see illustrated image below) because from here I need to draw two branches. I have defined two functions
    1. fractalY1: This will draw the right branch from a node and return the branch's end point co-ordinates. This end point is a new node. 
    2. fractalY2: This will draw the left branch from a node and return the branch's end point co-ordinates. This end point is a new node.
    3. The input argument `distance` governs the length of each branch.
3. All these nodes' x,y co-ordinates are stored in the list named `x`
4. Finally, I created a for loop and in it, I am calling these functions. I used if-elif-else block to create the look and feel of trunk, branches and leaves (branches length progressively decreased).

![fractal_tree_explained](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/4b2a6bba-efe1-4282-be00-6e015035a5f5)


# Output

![fractal_tree](https://github.com/ZaidShamsi/my_python_scripts/assets/103277308/b06bed20-d08e-4e2c-b0f8-cd5a20257420)
