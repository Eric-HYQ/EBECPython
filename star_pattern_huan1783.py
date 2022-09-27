"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 09/26/2022

Description:
    Draw a star pattern that has a user specified number of points..

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    # a and b are angle A and angle B
    # starting angle is 270 + a for any points
    points = int(input("Enter the points you want: "));
    a = 360 / points;
    b = 2 * a;
    side_length = 60 # Also the radius of a circle enclosed by the star.
    setheading(270 + a);
    color('black', 'red');
    
    begin_fill()
    for _ in range(points):
        forward(side_length);
        left(180-a);
        forward(side_length);
        right(180-b);
    end_fill()



"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
