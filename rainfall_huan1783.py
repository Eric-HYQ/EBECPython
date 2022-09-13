"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/12/2022

Description:
    Use the years and months inches of rainfall
    show the total inches of rainfall and average for each month

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
    # ask for the number of years and determine whether continue or not
    # define initial list anf month names
    years = int(input('Enter the number of years: '));
    rainfallList = [];
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    # nested loops and if control to select non-negative rain
    # collect all months and calculate
    if years <= 0:
        print('Invalid input; years must be greater than 0.');
    else:
        for i in range(years):
            print(f'  For year No. {i+1:d}');
            for j in range(12):
                inchOfRainfallSingle = float(input(f'    Enter the rainfall for {monthList[j]}.: '));
                while inchOfRainfallSingle <= 0:
                    print('    Invalid input; rainfall cannot be negative.');
                    inchOfRainfallSingle = float(input(f'    Enter the rainfall for {monthList[j]}.: '));
                rainfallList.append(inchOfRainfallSingle);
        monthNumber = years * 12;
        print(f'There are {monthNumber:d} months.');
        print(f'The total rainfall was {sum(rainfallList):.2f} inches.');
        print(f'The monthly average rainfall was {sum(rainfallList) / monthNumber:.2f} inches.')



    






"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
