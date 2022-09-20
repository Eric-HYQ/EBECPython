"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 09/19/2022

Description:
    Ask the user to enter a number and determine if it a prime number,
    use -1 to end.

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
import math

"""Write new functions below this line (starting with unit 4)."""
def is_prime(number):
    # 1 and 2 are special
    # loop start from 2 and dont consider 1 and number itself, find any divisible inside
    # when find, break the loop
    # if not at final, print is prime
    timeLimit = math.ceil(number ** 0.5) + 1
    if number == 1:
        return False;
    elif number == 0:
        return False;
    elif number == 2:
        return True;
    else:
        for i in range(2, timeLimit):
            if (number % i) == 0:
                return False;
                break;
        return True;



def main():
    # like do wile loop
    number = int(input('Enter a positive integer (-1 to quit): '));
    while number != -1:
        if is_prime(number):
            print(f'  {number:d} is prime!');
        else:
            print(f'  {number:d} is not prime.');
        number = int(input('Enter a positive integer (-1 to quit): '));


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
