"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 10.3 - COVID 19 Cases
Date: 11/07/2022

Description:
    Reads the contents of the file and calculates the total number of cases for each week, 
    then create a bar chart plotting the total cases for each week

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
import matplotlib.pyplot as plt
import numpy as np

"""Write new functions below this line (starting with unit 4)."""
def read_data():
    # read the data file and process the data
    # make them to float, then add all prior to it
    with open('indiana_covid-19_data_fall_2022.txt', 'r') as fo:
        data = fo.readlines()
        dataNoTrans = [i[:-1] for i in data]
        dataNoSpace = [i.split() for i in dataNoTrans]
        caseWeekPDF = [float(i[2]) for i in dataNoSpace]
        caseWeekCDF = []
        for i in range(len(caseWeekPDF)):
            caseWeekCDF.append(sum(caseWeekPDF[:i+1])/1000)
    return caseWeekCDF

def main():
    # get the price data from the txt file
    # draw a line figure to show it
    # detail the figure by lim and ticks
    # save as pdf
    cases = read_data();
    weeks = range(len(cases))
    weekLabel = ['2020-01', '2020-05', '2020-09', '2021-01', '2021-05', 
                    '2021-09', '2022-01', '2022-05', '2022-09']
    tickx = np.array([1,2,3,4,5,6,7,8,9])*18-23
    fig = plt.plot()
    plt.title('Weekly Positive COVID-19 Cases in Indiana')
    plt.bar(weeks, cases, width = 7)
    plt.xlabel('Date')
    plt.ylabel('Number of Cases (in thousands)')
    plt.xlim(-10, 155)
    plt.ylim(0, 2025)
    plt.xticks(tickx, weekLabel, rotation=30)
    plt.yticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250])
    plt.savefig('covid_19_cases_huan1783.pdf',  bbox_inches = 'tight')
    plt.show()




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
