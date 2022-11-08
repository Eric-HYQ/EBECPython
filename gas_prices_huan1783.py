"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/07/2022

Description:
    Read the data of average price of gas of each week, 
    then plot the data as a line graph

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

"""Write new functions below this line (starting with unit 4)."""
def read_data():
    # read the data file and process the data to prices number
    with open('2008_Weekly_Gas_Averages.txt', 'r') as fo:
        data = fo.readlines()
        dataNoTrans = [float(i) for i in data]
    return dataNoTrans

def main():
    # get the price data from the txt file
    # draw a line figure to show it
    # detail the figure by lim and ticks
    # save as pdf
    prices = read_data();
    weeks = range(1, 53)
    fig = plt.plot()
    plt.title('2008 Weekly Gas Prices')
    plt.plot(weeks, prices)
    plt.xlabel('Weeks (by number)')
    plt.ylabel('Average Price (dollars/gallon)')
    plt.xlim(1, 52)
    plt.ylim(1.5, 4.25)
    plt.xticks([10, 20, 30, 40, 50])
    plt.yticks([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    plt.grid()
    plt.savefig('gas_prices_huan1783.pdf')
    plt.show()
    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
