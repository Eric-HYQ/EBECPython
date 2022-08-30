"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 01.1 - Road Trip
Date: 08/30/2022

Description:
    According to the distance, fuel price, and fuel effciency that guests provide,
    estimate how much money is needed for fuel during road trip.

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
    ## greet to tell guests what this program do
    print("Road trip fuel cost estimator:");

    ## ask for single distance, gas price, and fuel efficient
    singleDistance = float(input("  How far away is your destination (miles)? "));
    avgFuelPrice = float(input("  What is the average price of gas (dollars per gallon)? "));
    fuelEfficiency = float(input("  What is the fuel efficiency of your vehicle (mpg)? "));

    ## calculate the cost
    costRound = int((2 * singleDistance) * avgFuelPrice / fuelEfficiency);

    ## output the caculation of cost
   # print("\n");
    print("\nThe fuel cost for this trip is approximately $" + format(costRound, 'd') + ".");

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
