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
import os
f_1 = "cs412_3_4_input.txt"
text_file = open("f_1", 'r')

with open('f_1') as text_file:
    data = text_file.readlines()
    print(data)
