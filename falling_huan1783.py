"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 04.1 - Falling
Date: 09/19/2022

Description:
    Calculate the distance of falling at a series of time from 5s to 50s.

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
def falling_dist(time):
    g = 8.87; ## unit as m/s
    distance = 0.5 * g * time ** 2; ## unit m
    return distance;


def main():
    # print haeder and dash line
    # call for the fuction and calculate in series
    print('Time (s)  Distance (m)');
    print('-' * 22);
    for i in range(5, 51, 5):
        disTemp = falling_dist(i);
        print(f'{i:>8d}{disTemp:>14.1f}');


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
