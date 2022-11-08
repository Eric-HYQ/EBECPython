"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/07/2022

Description:
    uses matplotlib to draw a plot of sine and cosine from 0 to 2*pi on the same axes.

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
import matplotlib.pyplot as plt
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():
    # get the price data from the txt file
    # draw a line figure to show it
    # detail the figure by lim and ticks
    # save as pdf
    x = np.linspace(0, 2*np.pi, num = 5000)
    sin = np.sin(x)
    cos = np.cos(x)
    fig = plt.plot()
    plt.plot(x, sin, color = 'r')
    plt.plot(x, cos, color = 'b')
    #plt.xlim(0, 2*np.pi)
    #plt.ylim(-1, 1)
    plt.xticks([np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
    plt.yticks([-1, 1])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    plt.savefig('sin_cos_huan1783.pdf')
    plt.show()




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
