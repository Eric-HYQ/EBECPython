"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 09.3 - Course Info
Date: 10/31/2022

Description:
    User enter a course number, 
    displays that courses instructor, room number, and meeting time.

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
def get_course_data():
    # get all data from the txt
    # put'em all in two dictionary
    keyList = ['room', 'instructor', 'time']
    cs101 = ['3004', 'Django','9:00 a.m.']
    cs102 = ['4501', 'Idle','10:00 a.m.']
    cs103 = ['6755', 'Rich','11:00 a.m.']
    nt110 = ['1244', 'Marshal','12:00 p.m.']
    cm241 = ['1411', 'Pickle','2:00 p.m.']
    course = {'CS101':dict(zip(keyList, cs101)), 
                'CS102':dict(zip(keyList, cs102)),
                'CS103':dict(zip(keyList, cs103)),
                'NT110':dict(zip(keyList, nt110)),
                'CM241':dict(zip(keyList, cm241))}
    return course

def main():
    # get the data and course number from users
    # determine the course whether or not in range
    # in range, print search result
    courseInfo = get_course_data();
    courseNumber = input('Enter a course number: ');
    d = courseInfo.get(courseNumber, 0)
    if d == 0:
        print(f'  {courseNumber} is an invalid course number.');
    else:
        print('    Instructor: {instructor:s}\n          Room: {room:s}\n          Time: {time:s}'.format(**d))
    
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
