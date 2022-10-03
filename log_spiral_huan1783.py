"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/03/2022

Description:
    Draw the logarithmic spiral.

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
from math import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    # define some values first, then use loop to draw along pixels
    # notice that the initial area start directly
    # not pendown until get to the first point, rather than (0,0)
    a = 4;
    b = 0.22;
    space = 10
    penup();
    goto(0,0);
    setheading(0);
    for i in range(0, 3 * 360 + 1, space):
        theta = radians(i);
        x = a * exp(b * theta) * cos(theta);
        y = a * exp(b * theta) * sin(theta);
        goto(x, y);
        pendown();


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
