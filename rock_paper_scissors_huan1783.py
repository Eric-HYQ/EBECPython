"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/03/2022

Description:
    Use a function that can return a random numebr with given digit number,
    then this function in a programthat gives the user a simple math quiz

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
import math as m

"""Write new functions below this line (starting with unit 4)."""
def get_computer_choice():
    # create a random choice from three possibilities
    allResults = ['rock', 'paper', 'scissors'];
    result = r.choice(allResults);
    return result;

def get_player_choice():
    # ask for and confirm a valid result from player
    userAnswer = input('Choose rock, paper, or scissors: ');
    condition = (userAnswer != 'rock') and (userAnswer != 'paper') and (userAnswer != 'scissors');
    while condition:
        print('You made an invalid choice. Please try again.');
        userAnswer = input('Choose rock, paper, or scissors: ');
        condition = (userAnswer != 'rock') and (userAnswer != 'paper') and (userAnswer != 'scissors');
    return userAnswer;

def get_winner(computer, player):
    if computer == 'rock':
        if player == 'rock':
            return 'tie';
        elif player == 'paper':
            return 'player';
        elif player == 'scissors':
            return 'computer';
    if computer == 'paper':
        if player == 'rock':
            return 'computer';
        elif player == 'paper':
            return 'tie';
        elif player == 'scissors':
            return 'player';
    if computer == 'scissors':
        if player == 'rock':
            return 'player';
        elif player == 'paper':
            return 'computer';
        elif player == 'scissors':
            return 'tie';

def main():
    # get two answers first
    # then compare and get a winner
    # print according to the winner
    computerAnswer = get_computer_choice();
    playerAnswer = get_player_choice();
    result = get_winner(computerAnswer, playerAnswer);
    while result == 'tie':
        print(f'  The computer chose {computerAnswer}, and you chose {playerAnswer}.');
        print('  It\'s a tie. Starting over.\n');
        computerAnswer = get_computer_choice();
        playerAnswer = get_player_choice();
        result = get_winner(computerAnswer, playerAnswer);
    if result == 'computer':
        print(f'  The computer chose {computerAnswer}, and you chose {playerAnswer}.');
        print(f'  {computerAnswer} beats {playerAnswer}');
        print('  You lost.  Better luck next time.');
    else:
        print(f'  The computer chose {computerAnswer}, and you chose {playerAnswer}.');
        print(f'  {playerAnswer} beats {computerAnswer}');
        print('  You won the game!');
    print('Thanks for playing.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()