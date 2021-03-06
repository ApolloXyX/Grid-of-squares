"""
Program: CS 115 Lab 3c_1
Author: Your name here.
Description: This program draws a few rectangles and fills them.
"""
from graphics import *
from random import seed, randint


def random_color():
    '''Produces a random color.

    Returns:
        str: a string representing a color.
    '''
    # Note: Don't worry about the details of this function right now.
    colors = ['blue', 'blue2', 'blue3', 'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3', 'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3', 'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3', 'pink', 'pink1', 'pink2', 'pink3']
    return colors[randint(0, len(colors) - 1)]


def main():
    seed()  # Initialize random number generator

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60
    # num_rows = int(input('Number of rows: '))  # commented out for now
    num_columns = int(input('Number of columns: '))

    window = GraphWin('Lab 3B', 800, 800)

    for i in range(num_columns):
       # Calculate x-coordinate of the top left point of the current square.
       #   For example:
       #   When i is zero (the first time through the loop), x should be top_left_x.
       #   When i is 1, x should be top_left_x + width.
       #   When i is 2, x should be top_left_x + 2 * width
       #   etc.
       #x =  TODO: equation based on top_left_x, width, and i
       x = top_left_x + width*(i+1)

       # Calculate the y-coordinate of the top left point of the current square.
       #   For example:
       #   When y is zero, the value should be top_left_y.
       #   Hint: Be careful! You may want to draw on a piece of paper.
       #y =  TODO: equation based on top_left_y
       y = top_left_y

       top_left_point = Point(x, y)
       bottom_right_point = Point(x + width, y + height)

       # Create a square using top_left_point and bottom_right_point
       # TODO: your code here (see prior code for example)
       top_left_point = Point(x,y)
       bottom_right_point = Point(x + width, y + height)
       enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)



       # Fill the square with a random color
       # TODO: your code here (see prior code for example)
       enclosing_rectangle.setFill(random_color())

       # Draw the square in the window
       # TODO: your code here (see prior code for example)
       enclosing_rectangle.draw(window)




    top_left_point = Point(top_left_x, top_left_y)
    bottom_right_point = Point(top_left_x + width, top_left_y + height)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setFill(random_color())
    enclosing_rectangle.draw(window)

    for i in range(10):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        print('x =', x_c_point, 'y =', y_c_point)

    window.getMouse()
    window.close()


main()