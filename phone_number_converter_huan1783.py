"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 08.2 - Phone Number Converter
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
def convert_number(s):
    # transfor the input into digit
    # first create two mapping lists for letters and number
    # find each letter of s in letter list
    # get coresponding digit number 
    s = s.upper();
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '22233344455566677778889999'
    for i in range(12):
        position = letter.find(s[i]);
        if position != -1:
            s = s.replace(s[i], number[position]);
    return s

def main():
    s = input("Enter a telephone number: ");
    sDigit = convert_number(s);
    print(f'The phone number is {sDigit}');


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
