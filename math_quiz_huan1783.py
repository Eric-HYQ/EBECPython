"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/03/2022

Description:
    Use a function that can return a random numebr with given digit number,
    then this function in a programthat gives the user a simple math quiz

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
import math as m

"""Write new functions below this line (starting with unit 4)."""
def random_number(d):
    # create a random numebr with given digit
    lowBound = m.pow(10, d-1);
    highBound = m.pow(10,d) - 1;
    result = r.randint(lowBound, highBound);
    return result;

def main():
    # use random_number to create math quiz
    # congts when get right answer and corrects when get wrong answer
    numebr1 = random_number(2);
    numebr2 = random_number(3);
    print(f'   {numebr1:d}\n+ {numebr2:d}');
    print('-' * 5);
    userAnswer = int(input('= '));
    if userAnswer == (numebr1 + numebr2):
        print('Correct -- Good Work!');
    else:
        print(f'Incorrect. The correct answer is {numebr1 + numebr2}.');


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()