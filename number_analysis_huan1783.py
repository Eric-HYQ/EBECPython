"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/19/2022

Description:
    get ten numbers from user and calculate the highest, lowest, sum, and avg

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
def get_number_list():
    # collects ten floating point numbers and returns them as a list
    newList = [];
    for i in range(10):
        newItem = float(input(f'  number  {i+1} of 10: '));
        newList.append(newItem);
    return newList
    

def main():
    # get user's number and list
    # calculate it to get four required numebrs
    print('Enter 10 numbers:');
    userList = get_number_list();
    total = sum(userList);
    high = max(userList);
    low = min(userList);
    avg = total / len(userList);
    print(f'Highest number: {high:.2f}\nLowest number: {low:.2f}\nTotal: {total:.2f}\nAverage: {avg:.2f}')




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()