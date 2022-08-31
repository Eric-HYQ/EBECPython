"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 08/31/2022

Description:
    According to the number of coolies that users want to make, 
    estimate how much butter, sugar, and flour should be added respectively.

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
    ## greet to ask for number of cookie
    numberOfCookie = int(input("How many cookies do you want to make? "));

    ## set calculate standard, unit as cup and piece(cookie only)
    standardButter = 1.25;
    standardSuger = 1.5;
    standardFlour = 2.5;
    standardNumberOfCookie = 48;

    ## calculate how much cups if ingredients needed for those cookies
    butter = standardButter / standardNumberOfCookie * numberOfCookie;
    sugar = standardSuger / standardNumberOfCookie * numberOfCookie;
    flour = standardFlour / standardNumberOfCookie * numberOfCookie;

    ## output the amounnt of ingredients
    print(f'To make {numberOfCookie:,d} cookies, you will need:');
    print(f'{butter: >10,.2f} cups of butter');
    print(f'{sugar: >10,.2f} cups of sugar');
    print(f'{flour: >10,.2f} cups of flour');
 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
