"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/03/2022

Description:
    Use the functions imported from vowels.py 
    to draw each of the vowels a single time but in a random order.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels as v
import random as r

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    # give initial steups and spaces
    # use loop to make it random
    # import vowel.py to draw elements
    start = Vec2D(-220, -30)
    nextLetter = Vec2D(60, 0) + Vec2D(12, 0);
    order = [0,1,2,3,4];
    r.shuffle(order);
    for i in order:
        if i == 0:
            v.draw_a(start);
        elif i == 1:
            v.draw_e(start);
        elif i == 2:
            v.draw_i(start);
        elif i == 3:
            v.draw_o(start);
        elif i == 4:
            v.draw_u(start);
        start = start + nextLetter;
    goto(start)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
