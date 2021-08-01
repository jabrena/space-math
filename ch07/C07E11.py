from ce_turtl import *


def part(total, length, breadth, col):
    angleInc = 360/total
    #turtle.width( breadth )
    turtle.pensize(breadth)
    #turtle.color( col )
    turtle.color(0, 0, 255)
    for i in range(total):
        turtle.forward(length)
        turtle.left(angleInc)


def rosette(total, length, width, color, angleInc):
    # added forced type int for python3
    for i in range(int(360/angleInc)):
        part(total, length, width, color)
        turtle.left(angleInc)

# set up the turtle
# turtle.setup( 500, 500, 100, 100 ) # specify width, height, position on screen


turtle.clear()
turtle.speed(0)  # draw as fast as possible

# call the functions
#title("Rosette - original from website no longer active")
rosette(10, 40, 1, "blue", 36)
# rosette(5,80,1,"red",36)
# turtle.exitonclick()

turtle.show()
