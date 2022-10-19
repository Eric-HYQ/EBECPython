"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/18/2022

Description:
    find all items in initial list and put them in a new one, display the new one

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
def multiples_of(base, iniList):
    # find out each item that is the numtople of base
    mulList = [];
    for i in range(len(iniList)):
        if iniList[i] % base == 0:
            mulList.append(iniList[i]);
    return mulList

def main():
    # given list and multiple
    # find out each item that is the numtople of base
    # dispay both old one and new one
    iniList = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406];
    base = 13;
    print(f'Original list of numbers:\n  {iniList}');
    newList = multiples_of(base, iniList);
    print(f'Numbers in the list that are multiples of {base}:\n  {newList}')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()