"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: mm.n - Hello User
Date: 08/23/2022

Description:
    This program is used to ask for the user's name and then greet the user

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
    ## first ask for the user's name 
    userName = input("What is your name? ")

    ## greet the user with the name
    print('Hello ' + userName + '!')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
