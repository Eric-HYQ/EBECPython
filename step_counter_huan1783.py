"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.6 - Step Counter
Date: 10/24/2022

Description:
    reads the steps.txt file, then calculates and displays the average
    number of steps taken for each month

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
def m_avg(l,d,n):
    n1 = sum(d[:n-1])
    n2 = sum(d[:n])
    ave = sum(l[n1:n2]) / d[n-1]
    return ave

def main():
    # read the number file created in last assignment
    # get the word and split by change line
    # convert all into digits, calculate some stats data
    print('The average steps taken each month were: ')
    dayStepI = [];
    with open('steps.txt','r') as fo:
        s = fo.read();
        dayStepS = s.split('\n')
        dayStepS.pop();
        length = len(dayStepS);
        for i in range(length):
            dayStepI.append(int(dayStepS[i]));
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    jan = sum(dayStepI[0:days[0]]) / days[0];
    print(f'   January : {jan:.2f}')
    print(f'  February : {m_avg(dayStepI, days, 2):.2f}')
    print(f'     March : {m_avg(dayStepI, days, 3):.2f}')
    print(f'     April : {m_avg(dayStepI, days, 4):.2f}')
    print(f'       May : {m_avg(dayStepI, days, 5):.2f}')
    print(f'      June : {m_avg(dayStepI, days, 6):.2f}')
    print(f'      July : {m_avg(dayStepI, days, 7):.2f}')
    print(f'    August : {m_avg(dayStepI, days, 8):.2f}')
    print(f' September : {m_avg(dayStepI, days, 9):.2f}')
    print(f'   October : {m_avg(dayStepI, days, 10):.2f}')
    print(f'  November : {m_avg(dayStepI, days, 11):.2f}')
    print(f'  December : {m_avg(dayStepI, days, 12):.2f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
