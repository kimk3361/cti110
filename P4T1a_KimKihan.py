# Turtle Graphics: Repeating Squares
# October 18, 2019
# CTI-110 P4T1a
# Kihan Kim

import turtle
turtle.speed(0)
turtle.hideturtle()
num_squares = 100
side = 7

for x in range(num_squares):
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    
    side += 3


# Import turtle
# Set turtle speed
# Hide turtle
# Initialize variable to control loop
# Initialize accumulator variable
# Draw square with loop
