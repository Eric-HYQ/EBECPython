"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.5 - Number Reader
Date: 10/24/2022

Description:
    reads the random numbers from the random_numbers.txt
    calculate and display some data about the numbers in the file

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
    # read the number file created in last assignment
    # get the word and split by change line
    # convert all into digits, calculate some stats data
    with open('random_numbers.txt','r') as fo:
        s = fo.read();
        sList = s.split('\n')
        sList.pop();
        length = len(sList);
        for i in range(length):
            sList[i] = int(sList[i]);
    print(f'{length:,d} numbers were read from the file.');
    print(f'Min: {min(sList):,d}\nMax: {max(sList):,d}\nSum: {sum(sList):,d}\nAvg: {sum(sList)/length:,.1f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
