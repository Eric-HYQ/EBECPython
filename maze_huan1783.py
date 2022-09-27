"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 05.1 - Maze
Date: 09/26/2022

Description:
    Move the turtle to outside of the maze.

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
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)


def main():
    # the line width is w, which is 12 in this maze
    # draw the lines step by step
    # sent the turtle out the maze
    w = 12;
    forward(w);
    right(90);
    forward(3*w);
    right(90);
    forward(4*w);
    left(90);
    forward(2*w);
    left(90);
    forward(6*w);
    left(90);
    forward(4*w);
    right(90);
    forward(2*w);
    left(90);
    forward(4*w);
    right(90);
    forward(2*w);
    left(90);
    forward(6*w);
    right(90);
    forward(4*w);
    left(90);
    forward(4*w);
    right(90);
    forward(2*w);
    left(90);
    forward(4*w);
    right(90);
    forward(6*w);
    right(90);
    forward(10*w);
    right(90);
    forward(4*w);
    left(90);
    forward(2*w);
    left(90);
    forward(4*w);
    right(90);
    forward(5*w);
    left(90);
    forward(2*w);



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
