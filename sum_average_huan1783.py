"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/12/2022

Description:
    Ask user to enter a series of non-negative numbers
    Calculate and display their sum and average
    Use a negative number as terminal

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


def main():
    # ask for the input series of numbers
    # delete the terminal number
    numberList = [];
    number = 0;
    while number >= 0:
        number = float(input('Enter a non-negative number (negative to quit): '));
        numberList.append(number);
    numberList.pop(-1);

    # use length of the list to print
    listLength = len(numberList)
    if len(numberList) == 0:
        print("  You didn't enter any numbers.");
    else:
        print(f'  You entered {len(numberList):d} numbers.');
        print(f'  Their sum is {sum(numberList):.3f} and their average is {sum(numberList)/len(numberList):.3f}.');





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
