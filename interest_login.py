"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 01.2 - Interest
Date: 08/30/2022

Description:
    According to the primary value, annual interest rate, 
    annual compound times, and years that guests provide,
    estimate how much money the account should have after years.

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
    ## greet to tell guests what to do next
    print("Enter the following parameters.");

    ## ask for initial deposit, annual interest rate, years, and compound times
    ## true interest rate should be a percentage but enter without it
    initDeposite = float(input("  The initial deposit? "));
    annualInterestRate = float(input("  The annual interest rate in percent? ")) / 100;
    numberOfYear = float(input("  The number of years the account earn interest? "));
    annualCompoundTimes = float(input("  The number of times interest is compounded each year: "));

    ## calculate the cost
    calculateBrace = (1 + annualInterestRate / annualCompoundTimes);
    powerTimes = annualCompoundTimes * numberOfYear;
    finalValue = initDeposite * pow(calculateBrace, powerTimes);

    ## output the caculation of cost
   # print("\n");
    print("The balance of this account will be $" + 
            format(finalValue, ',.2f') + " after " +  
            format(numberOfYear, '.1f') + " years.");

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
