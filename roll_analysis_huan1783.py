"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/19/2022

Description:
    calculate and analyze the percentage of rolls that have each value between 2 and 12.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def roll_d6():
    # roll one dice
    d6 = r.randint(1,6);
    return d6

def get_2d6_rolls(times):
    # roll two dices and get a list of all results
    newList = [];
    for i in range(times):
        dice1 = roll_d6();
        dice2 = roll_d6();
        newList.append(dice1 + dice2);
    return newList
    

def main():
    # roll two dices and get a list of all results
    # calculate the percentage of all results
    times = 1000000;
    resultList = get_2d6_rolls(times);
    print('Roll  Frequency');
    for i in range(2,13):
        temp = resultList.count(i);
        percentage = temp / len(resultList);
        print(f'{i:>3d}   {percentage:>7.2%}')


    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()