"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/06/2022

Description:
    Ask for a number of seconds and then 
    displays the total time entered in days, hours, minutes and seconds.

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
    # ask for the total seconds
    totalSecond = int(input("Please enter a time in seconds: "));

    # calculate each number for day, hour, minute and second
    days = totalSecond // 86400;
    hours = totalSecond % 86400 // 3600;
    minutes = totalSecond % 3600 // 60;
    seconds = totalSecond % 60;

    # need to determine when to use common and when use 'and'
    if days == 0 and hours == 0 and minutes == 0:
        print(f"  {totalSecond:,d} seconds is less than one minute.");
    else:
        print(f'  {totalSecond:,d} seconds equals ', end = '')
        if hours:
            if days:
                print(f'{days} day(s)', end = '')
                if minutes or seconds:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{hours} hour(s)', end = '')
            if seconds:
                if minutes:
                    print(f', {minutes} minute(s)', end = '')
                print(f' and {seconds} second(s)', end = '')
            else:
                if minutes:
                    print(f' and {minutes} minute(s)', end = '')
        else:
            if days:
                print(f'{days} day(s)', end = '')
                if minutes and seconds:
                    print(', ', end = '')
                elif minutes or seconds:
                    print(' and ', end = '')
            if seconds:
                if minutes:
                    print(f'{minutes} minute(s) and ', end = '')
                print(f'{seconds} second(s)', end = '')
            else:
                if minutes:
                    print(f'{minutes} minute(s)', end = '')
        print('.')





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
