"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/03/2022

Description:
    Module that include functions can draw individual elements

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


def draw_a(start):
    lowMiddle = Vec2D(30, 0);
    end = Vec2D(60, 0);
    goto(start + lowMiddle);
    pendown();
    circle(30);
    penup()
    goto(start + Vec2D(60, 60));
    pendown();
    right(90);
    forward(60);
    penup();
    setheading(0);
    #return (start + end);



def draw_e(start):
    leftMiddle = Vec2D(0, 30);
    end = Vec2D(60, 0);
    goto(start + leftMiddle);
    pendown();
    forward(60);
    left(90);
    circle(30, 315);
    penup()
    goto(start + end);
    setheading(0);
    #return (start + end);



def draw_i(start):
    lowMiddle = Vec2D(30, 0);
    end = Vec2D(60, 0);
    goto(start + lowMiddle);
    pendown();
    left(90);
    forward(60);
    penup()
    goto(start + lowMiddle + Vec2D(0, 90));
    pendown();
    dot(9);
    penup();
    goto(start + end);
    setheading(0);
    #return (start + end);



def draw_o(start):
    lowMiddle = Vec2D(30, 0);
    end = Vec2D(60, 0);
    goto(start + lowMiddle);
    pendown();
    circle(30);
    penup()
    goto(start + end);
    setheading(0);
    #return (start + end);


def draw_u(start):
    leftHigh = Vec2D(0, 60);
    end = Vec2D(60, 0);
    goto(start + leftHigh);
    pendown();
    right(90);
    forward(30);
    circle(30, 180);
    backward(30);
    forward(60);
    penup();
    goto(start + end);
    setheading(0);
    #return (start + end);



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
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
