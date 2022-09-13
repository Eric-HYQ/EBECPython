"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/13/2022

Description:
    Use starting number, the average daily increase, and the number of days,
    to predicts the approximate size of a population of organisms

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
    # ask for the starting number, the average daily increase, and the number of days
    startingNumber = float(input('Starting population, in thousands: '));
    averageIncrease = int(input('Average daily increase, in percent: '));
    dayNumber = int(input('Number of days to multiply: '));

    # 
    currentNumber = startingNumber
    print('Day   Approx. Pop');
    for i in range(dayNumber+1):
        print(f'{i:>3,d}{currentNumber:>14,.3f}');
        currentNumber = currentNumber * (1 + averageIncrease / 100);



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
