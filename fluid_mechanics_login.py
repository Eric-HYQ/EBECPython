"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/06/2022

Description:
    Calculate Reynold number of water,
    besed on user's velocity, pipe diameter, and temperature

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
    # ask for the velocity, diameter and temperature
    temperature = float(input("Enter the temperature in °C as 5, 20, or 50: "));
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "));
    diameter = float(input("Enter the pipe's diameter (m): "));

    # calculate the Reynolds number for the situation
    if temperature == 5:
        viscosity = 1.52e-6;
    elif temperature == 20:
        viscosity = 1.00e-6;
    elif temperature == 50:
        viscosity = 5.54e-7;
    else:
        print("Please select temperature among the choices")
    reNumber = velocity * diameter / viscosity;

    # output the condition and result
    print(f'At {temperature:.1f}°C, the Reynolds number for flow at ' + 
            f'{velocity} m/s in a {diameter} m diameter pipe is {reNumber:.2e}.')





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
