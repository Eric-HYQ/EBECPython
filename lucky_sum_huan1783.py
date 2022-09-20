"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 04.2 - Lucky sum
Date: 09/19/2022

Description:
    According to two numebrs that user input,
    calculate the sum of all numbers that are not divisible by 3.

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
def lucky_sum(num1, num2):
    # give in either order
    # set n1 as the smaller one
    luckySum = 0;
    if num1 <= num2:
        n1 = num1;
        n2 = num2;
    elif num1 > num2:
        n1 = num2;
        n2 = num1;
    for i in range(n1, n2+1):
        if (i % 3) != 0:
            luckySum += i;
    return luckySum;


def main():
    # get input numbers and call for the funciton
    # print the toal result
    number1 = int(input('Enter the first integer: '));
    number2 = int(input('Enter the second integer: '));
    total = lucky_sum(number1, number2);
    print(f'The sum of the lucky numbers is {total:,d}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
