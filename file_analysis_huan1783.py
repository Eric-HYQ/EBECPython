"""
Author: Yuqing Huang, huan1783@purdue.edu
Assignment: 09.4 - File Analysis
Date: 10/31/2022

Description:
    processes the two provided text files (python_1.txt and python_2.txt)
    get word frequency of each file, output files to store them
    find the common words and ether and not both words, output files

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
import string

"""Write new functions below this line (starting with unit 4)."""
def load_file_data(filename):
    # get all data from the txt
    # remove punctuations
    # shape the output
    with open(filename,'r') as fo:
        data = fo.read();
        dataLow = data.lower()
        punc = string.punctuation
        #dataNoPunc = dataLow.translate(dataLow.maketrans('', '', punc))
        #dataNoPunc = dataLow.strip(punc)
        #dataNoTrans = dataNoPunc.split('\n')
        dataNoTrans = dataLow.split('\n')
        dataWord = [i.split(' ') for i in dataNoTrans if i != '']
        wordList = [item.strip(punc) for sublist in dataWord for item in sublist]
    return wordList;

def unique_word(wl):
    # get the word list
    # put them all in a dictionary
    wordKey = sorted(set(wl))
    wordCount = [wl.count(i) for i in wordKey]
    wordUnique = dict(zip(wordKey, wordCount))
    return wordUnique

def dic_write_out(wl, filename):
    # get word list and file names
    # write out dictionary
    with open(filename, 'w') as fo:
        for i, j in wl.items():
            fo.write(f'{i}: {j}\n')

def set_write_out(wl, filename):
    with open(filename, 'w') as fo:
        for i in wl:
            fo.write(f'{i}\n')

def main():
    # get the data and word dictionary from files
    # write the dictionary out
    wordList1 = load_file_data('python_1.txt');
    wordFreq1 = unique_word(wordList1);
    dic_write_out(wordFreq1, 'python_1_word_frequency.txt')
    wordList2 = load_file_data('python_2.txt');
    wordFreq2 = unique_word(wordList2);
    del wordFreq2['']
    dic_write_out(wordFreq2, 'python_2_word_frequency.txt')
    # find common words and output
    wordSet1 = set(wordFreq1)
    wordSet2 = set(wordFreq2)
    inter = sorted(wordSet1 & wordSet2)
    set_write_out(inter, 'common_words.txt')
    # find ether and not both words and output
    sysdif = sorted(wordSet1 ^ wordSet2)
    set_write_out(sysdif, 'eitherbutnotboth.txt')


    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
