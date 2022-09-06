"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/06/2022

Description:
    Determine whether a leap year is entered by user, 
    output number of days in that February according to the result.

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
    # Two branches of conditions can make a year leap year
    #   divisible by 400
    #   divisible by 4 but not 100
    #
    # ask for the year first
    # store the year and days of Feb in dic to print
    targetYear = int(input("Enter a year: "));
    yearFrbDic = {"year": targetYear, 
                    "leapFeb": 29,
                    "notLeapFeb": 28};

    # determine whether the year a leap year
    condition1 = (targetYear % 400 == 0);
    condition2 = (targetYear % 4 == 0 and targetYear % 100 != 0);

    if condition1 or condition2:
        print("The year {year} is a leap year.".format(**yearFrbDic));
        print("February of {year} has {leapFeb} days.".format(**yearFrbDic));
    else:
        print("The year {year} is not a leap year.".format(**yearFrbDic));
        print("February of {year} has {notLeapFeb} days.".format(**yearFrbDic));



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
