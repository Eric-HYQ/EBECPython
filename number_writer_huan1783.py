"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.4 - Number Writer
Date: 10/24/2022

Description:
    asks the user howmany numbers it should generate and then writes that
    many random numbers to a file named random_numbers.txt

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
import random as r

"""Write new functions below this line (starting with unit 4)."""


def main():
    # create one file
    # get the word count and create random numebrs
    # write in the text file with one number each line
    writeIn = int(input('How many numbers would you like? '));
    with open('random_numbers.txt','w') as fo:
        for i in range(writeIn):
            number = r.randint(1019, 1215);
            fo.write(f'{number}\n');

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
