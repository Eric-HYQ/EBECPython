"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/24/2022

Description:
    Convert the user input into Pig Latin

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
def pig(s):
    # transfor the input into pig latin
    # first make all lower case and split by words
    # add suffix and delete the first letter
    # recombine and capitalize the sentence
    sTemp = s.lower();
    sList = sTemp.split();
    suffix = 'ay';
    for i in range(len(sList)):
        sList[i] = sList[i] + sList[i][0] + suffix;
        sList[i] = sList[i][1:];
    sNew = ' '.join(sList)
    sNew = sNew.capitalize();
    return sNew

def main():
    s = input("Enter a string: ");
    sPig = pig(s);
    print(f'Pig latin: {sPig}');


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
