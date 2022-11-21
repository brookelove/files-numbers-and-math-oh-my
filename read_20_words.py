'''
1. read a file named cs412_3_4_input.txt
    a. print a error message and end the file if the file is missing
    b. it cant crash if the file doesnt exist
    c. dont include your test input file in your assignment 
2. validate that the file contains a single sentence of 20 words
    a. print a clear eror message to set the number f words allowed in teh file 
    b. use a constant variable to set the number in the file 
3. Break up hte sentence into four lines of 5 single spaced words
4. write the lines  to a new file names cs412_3_4_output.txt
5. on completeion print statemtn
    a. do not hardcode the file name in the print
    b. this or an error message 
    c. do not include the output 
'''
import sys


class CannotOpenFile(Exception):
    pass


READFILE = "cs412_3_4_input.txt"
MAX_WORDDS = 20
MAX_WORDS_PER_LINE = 5
WRITE_FILE = "cs412_3_4_output.txt"
# 1. open file using a try-catch block
try:
    text_file = open(READFILE, "r")
except CannotOpenFile:
    print(f"--> Error: Cannot open file {READFILE}")
# 2. Make it readable
all_data = text_file.readlines()
print(all_data)
# 3. convert data to a list of all of the words, remove
