"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 09.2 - World Series
Date: 10/31/2022

Description:
    Display the name of the team that won theWorld Series that year
    and the number of times that team has won theWorld Series.

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
def load_winners_data():
    # get all data from the txt
    # shape outputs, insert not played years
    # put'em all in two dictionary
    with open('WorldSeriesWinners.txt','r') as fo:
        s = fo.readlines();
        team = [i[:-1] for i in s];
        teamSet = list(set(team));
        year = list(range(1903,2022));
        del year[91];
        del year[1]
        times = [team.count(i) for i in teamSet]
        teamNumber = dict(zip(teamSet, times))
        yearTeam = dict(zip(year, team));
    return (teamNumber, yearTeam);

def main():
    # get the data and year from users
    # determine the year whether or not in range
    # in range, print search result
    [teamNumber, yearTeam] = load_winners_data();
    year = int(input('Enter a year in the range 1903 -- 2021: '))
    if year < 1903 or year > 2021:
        print(f'  Data for the year {year} is not included in this system.')
    elif year == 1904 or year == 1994:
        print(f'  The World Series wasn\'t played in the year {year}.')
    else:
        team = yearTeam[year];
        times = teamNumber[team];
        print(f'  The {team} won the World Series in {year}.')
        print(f'  They have won the World Series {times} times.')
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
