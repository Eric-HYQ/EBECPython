"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.3 - File Stats
Date: 10/24/2022

Description:
    Use keypad letter mapping to convert the letter into digit phone number

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
    # read in all the text
    # get the word count and line count respectively
    # print them out and also calculate the average word per line
    with open('frontiero_v_richardson.txt','r') as fo:
        total = fo.read();
        wordCount = len(total.split());
        lineCount = len(total.split('\n')) - 1;
    print(f'Total number of words: {wordCount}');
    print(f'Total number of lines: {lineCount}');
    print(f'Average number of words per line: {wordCount/lineCount:.1f}')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
