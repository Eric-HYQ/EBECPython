"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/06/2022

Description:
    Determine what color should the number in, 
    output the color according to the pocket.

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


"""Write new functions below this line (starting with unit 4)."""
# output the color and pocket
def printColor(pocket, color):
    print("  Pocket number {:d} is {}.".format(pocket,  color));

def main():
    # ask for the pocket, determine what color should the pocket in
    pocket = int(input("Please choose a pocket number: "));
    color = ('green', 'red', 'black');

    if pocket == 0:
        print("  Pocket number 0 is green.");
    elif (pocket >= 1 and pocket <= 10) or (pocket >= 19 and pocket <= 28):
        if pocket % 2 != 0:
            printColor(pocket, color[1]);
        else:
            printColor(pocket, color[2]);
    elif (pocket >= 11 and pocket <= 18) or (pocket >= 29 and pocket <= 36):
        if pocket % 2 != 0:
            printColor(pocket, color[2]);
        else:
            printColor(pocket, color[1]);
    else: 
        print("  Invalid Input!");




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
