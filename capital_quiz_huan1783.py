"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 10/31/2022

Description:
    Ask the users to enter the capital for a particular state.

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
def get_state_data():
    # get all data from the txt
    # seperate city and states, process them
    # put'em all in a dictionary
    with open('state_capitals.txt','r') as fo:
        s = fo.readlines();
        sList = [i.split(', ') for i in s];
        city = [i[0] for i in sList];
        state = [i[1][:-1] for i in sList];
        d = dict(zip(state, city));
    return d

def one_ques(d, cor, total):
    # each iteral of question
    # calculate and pop the correct item
    getKey = r.choice(list(d.keys()));
    answer = input(f"What is the capital of {getKey} (enter 0 to quit)? ");
    total += 1;

    if answer == '0':
        return [0, d, cor, total]
    elif answer == d[getKey].lower() or answer == d[getKey]:
        print('  That is correct!')
        d.pop(getKey)
        cor += 1;
        return [1, d, cor, total]
    else:
        print(f'  That is incorrect.\n  The capital of {getKey} is {d[getKey]}.');
        return [getKey, d, cor, total]



def main():
    # combine all the function
    stateCapital = get_state_data();
    temp = stateCapital.copy();
    correct = 0;
    total = 0;
    wrongDic = {};
    [ans, temp, correct, total] = one_ques(temp, correct, total);
    while ans != 0:
            [ans, temp, correct, total] = one_ques(temp, correct, total);
    print(f'You answered {correct} out of {total-1} questions correctly.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
