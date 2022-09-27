"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 09/26/2022

Description:
    Write the message “Mississippi turtles” on the screen

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
    setup(600, 400)
    width(9)
    color("purple")


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
    return (start + end);


def draw_i(start):
    goto(start);
    pendown();
    left(90);
    forward(60);
    penup()
    goto(start + Vec2D(0, 90));
    pendown();
    dot(9);
    penup();
    goto(start);
    setheading(0);
    return start;


def draw_l(start):
    goto(start);
    pendown();
    left(90);
    forward(120);
    penup()
    goto(start);
    setheading(0);
    return start;


def draw_M(start):
    goto(start);
    pendown();
    left(90);
    forward(90); # four lines, one arch
    left(180);
    circle(15, -180);
    left(180)
    forward(90); # and the line below, move the turtle back to arch
    left(180);
    forward(90);
    left(180);
    circle(15, -180);
    left(180);
    forward(90);
    penup();
    setheading(0);
    return start + Vec2D(60, 0);


def draw_p(start):
    end = Vec2D(60, 0);
    goto(start);
    pendown();
    left(90);
    forward(120);
    backward(30);
    left(180);
    circle(30);
    penup();
    goto(start + end);
    setheading(0);
    return (start + end);


def draw_r(start):
    end = Vec2D(30, 0);
    goto(start);
    pendown();
    left(90);
    forward(60);
    backward(30);
    left(180);
    circle(30, -90);
    penup();
    goto(start + end);
    setheading(0);
    return (start + end);


def draw_s(start):
    end = Vec2D(30, 0);
    goto(start);
    pendown();
    forward(15);
    circle(15, 180);
    left(180);
    circle(15, -180);
    left(180);
    forward(15);
    penup();
    goto(start + end);
    setheading(0);
    return (start + end);


def draw_t(start):
    end = Vec2D(60, 0);
    lowMid = Vec2D(30, 0);
    highAcross = Vec2D(0, 90);
    goto(start + lowMid);
    pendown();
    left(90);
    forward(120);
    penup();
    goto(start + highAcross);
    setheading(0);
    pendown();
    forward(60);
    penup();
    goto(start + end);
    return (start + end);

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
    return (start + end);


def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    penup();
    setheading(0);
    start = Vec2D(-250, 60);
    nextLetter = Vec2D(18, 0);

    temp = draw_M(start);
    temp = temp + nextLetter;
    temp = draw_i(temp);
    temp = temp + nextLetter;
    temp = draw_s(temp);
    temp = temp + nextLetter;
    temp = draw_s(temp);
    temp = temp + nextLetter;
    temp = draw_i(temp);
    temp = temp + nextLetter;
    temp = draw_s(temp);
    temp = temp + nextLetter;
    temp = draw_s(temp);
    temp = temp + nextLetter;
    temp = draw_i(temp);
    temp = temp + nextLetter;
    temp = temp + Vec2D(0, -60); # move to p
    temp = draw_p(temp);
    temp = temp + nextLetter;
    temp = draw_p(temp);
    temp = temp + nextLetter;
    temp = temp + Vec2D(0, 60);
    temp = draw_i(temp);

    temp = Vec2D(-250, -138);
    temp = draw_t(temp);
    temp = temp + nextLetter;
    temp = draw_u(temp);
    temp = temp + nextLetter;
    temp = draw_r(temp);
    temp = temp + nextLetter;
    temp = draw_t(temp);
    temp = temp + nextLetter;
    temp = draw_l(temp);
    temp = temp + nextLetter;
    temp = draw_e(temp);
    temp = temp + nextLetter;
    temp = draw_s(temp);
    temp = temp + nextLetter;
    goto(temp);


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
