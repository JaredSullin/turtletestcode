#Importing Turtle Library
import turtle

#Defining  functions
def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to (X,Y)
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling

def circle(x, y, radius, color):
    turtle.penup()             # Raise the pen
    turtle.goto(x, y -radius)  # Position the turtle
    turtle.fillcolor(color)    # Set the fill color
    turtle.pendown()           # Lower the pen
    turtle.begin_fill()        # Start filling
    turtle.circle(radius)      # Draw a circle
    turtle.end_fill()          # End filling

def line(startX, startY, endX, endY, color):
    turtle.penup()             # Raise the pen
    turtle.goto(startX, startY)# Move to the starting point
    turtle.pendown()           # Lower the pen
    turtle.pencolor(color)     # Set the pen color
    turtle.goto(endX, endY)    # Draw a square

