"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 09/19/2022

Description:
    Ask the user to enter a valid score five times,
    display a letter grade after each score is entered

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
def get_valid_score():
    # ask the user to enter a score within 0 and 100
    score = float(input('Enter a score: '));
    while (score > 100) or (score < 0):
        print('  Invalid Input. Please try again.');
        score = float(input('Enter a score: '));
    return score;

def calc_average(scoreList):
    # accept a list of scores and return the average of the scores.
    avgScore = sum(scoreList) / len(scoreList);
    return avgScore;

def determine_grade(score):
    # accept a score as an argument and return a letter grade for the score
    # de as decimal, control the decimal of output
    s = ['A', 'B', 'C', 'D', 'F'];
    if score <= 100 and score >= 92:
        return s[0];
    elif score < 92 and score >= 82:
        return s[1];
    elif score < 82 and score >= 73:
        return s[2];
    elif score < 73 and score >= 64:
        return s[3];
    else:
        return s[4];

def main():
    # use three functions to print output
    scoreList = [];
    while len(scoreList) < 5:
        score = get_valid_score();
        scoreList.append(score);
        gradeTemp = determine_grade(score);
        print(f'  The letter grade for {score:.1f} is {gradeTemp}.');
    finalAvg = calc_average(scoreList);
    print(f'\nResults:\n  The average score is {finalAvg:.2f}.');
    letterGrade = determine_grade(finalAvg);
    print(f'  The letter grade for {finalAvg:.2f} is {letterGrade}.');




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
