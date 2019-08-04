# PolygonOrRosette.py
# Billy Ridgeway
# Practices "if/else" statements.

import turtle       # Imports the turtle library.
t = turtle.Pen()    # Creates a new pen called t.

# Ask the user for the number of sides or circles, default to 6.
number = int(turtle.numinput("Number of sides or circles",
                             "How many sides or circles in your shape?", 6))

# Ask the user whether they want a polygon or a rosette.
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosette:")

for x in range(number):     # Sets the variable 'x' to the number of sides or circles.
    if shape == 'r':        # Checks to see if the user wanted a rosette.
        t.circle(100)       # Draws a circle.
    else:                   # If the user didn't enter 'r', the program defaults to a polygon.
        t.forward (150)     # Moves the pen forward 150 pixels/draws one side of the polygon.
    t.left(360/number)      # Moves the pen left by the quotient of 360 divided by the number entered by the user.
