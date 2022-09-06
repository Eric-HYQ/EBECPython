"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/06/2022

Description:
    Determine how much discount should the customer gets, 
    output discount and purchase amount after discount according to the quantity.

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
    # All of the output for cases with valid discount 
def outputAll(quantity, discount):
    print("  {:.0%} discount applied.".format(discount));
    totalPurchanse = 880 * quantity * (1 - discount);
    print("  The total price to purchase " + format(quantity, 'd') + 
                " packages is $" + format(totalPurchanse, ',.2f')+ ".");

def main():
    # ask for the quantity, determine the discount
    # then calculate and output the total amout of purchase after discount
    quantity = int(input("How many packages will be purchased: "));

    if quantity < 0:
        print("  Invalid Input!");
    elif quantity >= 0 and quantity < 4:
        print("  No discount applied.");
        totalPurchanse = 880 * quantity;
        print("  The total price to purchase " + format(quantity, 'd') + 
                " packages is $" + format(totalPurchanse, ',.2f')+ ".")
    elif quantity >= 4 and quantity < 40:
        discount = 0.1;
        outputAll(quantity, discount);
    elif quantity >= 40 and quantity < 200:
        discount = 0.15;
        outputAll(quantity, discount);
    elif quantity >= 200 and quantity < 1000:
        discount = 0.3;
        outputAll(quantity, discount);
    else: 
        discount = 0.42
        outputAll(quantity, discount);




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
