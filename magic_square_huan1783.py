"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/19/2022

Description:
    judge to determine if each square a Lo Shu Magic Square

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
def print_square(iniList):
    # print the square in 3 by 3
    print('Your square is:')
    rows, cols = 3,3
    for r in range(rows):
        print(' ', end='');
        for c in range(cols):
            n = iniList[r][c]
            print(f'{n:2d}', end='')
        print()

def is_magic(iniList):
    # to judge if a square Magic one
    # two criteria
    testList = [1,2,3,4,5,6,7,8,9];
    newList = iniList[0] + iniList[1] + iniList[2];
    if newList.sort() == testList:
        print(iniList)
        if sum(iniList[0]) == 15:
            if sum(iniList[1]) == 15:
                if sum(iniList[2]) == 15:
                    c0 = iniList[0][0] + iniList[1][0] + iniList[2][0];
                    if c0 == 15:
                        c1 = iniList[0][1] + iniList[1][1] + iniList[2][1];
                        if c1 == 15:
                            c2 = iniList[0][2] + iniList[1][2] + iniList[2][2];
                            if c2 == 15:
                                diag1 = iniList[0][0] + iniList[1][1] + iniList[2][2];
                                if diag1 == 15:
                                    diag2 = iniList[0][2] + iniList[1][1] + iniList[2][0];
                                    if diag2 == 15:
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def print_result(iniList):
    print_square(iniList)
    if is_magic(iniList):
        print('It is a Lo Shu magic square!\n')
    else:
        print('It is not a Lo Shu magic square.\n')

def main():
    # get a 2-d list
    # peint it first
    # then judge it and print the result
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    list2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]];
    list3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]];
    print_result(list1)
    print_result(list2)
    print_square(list3)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()