userInput_noOfTerms = 9
userInput_noOfTerms = userInput_noOfTerms - 3

num1 = 1
num2 = 1
sum = num1 + num2

fibonacciLst = [num1, num2, sum]

for i in range(0, userInput_noOfTerms):
    num1 = num2
    num2 = sum
    sum = num1 + num2
    fibonacciLst.append(sum)
print(fibonacciLst)

#1, 2, 3, 4, 5, 6,  7,  8,  9,
#1, 1, 2, 3, 5, 8, 13, 21, 34,
#total levels corresponding to userInput = 9
#number of branches in top level = 21
#number of twos in 21 = 8, number of ones = 5, 21 = 8 * 2 + 5,
#[2[1], 1[1], 2[2], 1[3], 2[3], 2[4], 1[5], 2[5], 2[6], 1[4], 2[7], 1[2], 2[8]]

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

for i in range(0, 9):
    
