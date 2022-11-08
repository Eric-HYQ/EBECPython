"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 10.1 -Monthly Sales
Date: 11/07/2022

Description:
    Collect monthly sales data from the user and stores it in a list

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
def month_data(n, ml):
    # given the month and month list, return a list from user contains the monthly sale
    l = [];
    for i in range(n):
        temp = int(input(f'Enter the sales for {ml[i]}: '));
        l.append(temp);
    return l

def main():
    # list the month and color
    # get user input of sale data
    # draw a pie figure with title, color, and labels as output
    mList = ['January', 'February', 'March', 'April','May', 'June', 'July', 
                'August', 'September', 'October', 'November', 'December']
    colors = ['#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11',
                '#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A']
    n = 12;
    saleData = month_data(n, mList);
    fig, ax = plt.subplots()
    plt.title('Monthly Sales Values')
    ax.pie(saleData, colors = colors, labels = mList)
    plt.show()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
