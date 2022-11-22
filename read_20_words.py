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


class OutOfBounds(Exception):
    pass


READFILE = "cs412_3_4_input.txt"
MAX_WORDDS = 20
WORDS_PER_LST = 5
WRITEFILE = "cs412_3_4_output.txt"
sectioned_words = []
sectioned_lines = []
# 1. open file using a try-catch block


def writing_files(lst):
    try:
        with open(WRITEFILE, 'w') as text_file:
            text_file.write(lst)
        print(f"Success! Output written to: {WRITEFILE}")
        text_file.close()
    except CannotOpenFile:
        print("error")


# def create_five_lst(lst):
#     i = 0
#     for i in len(lst):
#         line = ' '.join(lst[i])
#         sectioned_lines.append(line)


def create_twenty_lst(text_file):
    all_data = text_file.readline()
    # text_file.close()
    # print(all_data) # list of all data in one line
    # print(type(all_data)) # returngs a string
    # print(len(all_data))  # gives you the lenght of the amount in the data, returns 1
    # 3. convert data to a list of all of the words, remove
    lst_of_words = all_data.split(' ')
    # print(lst_of_words) # returns all of the list
    # print(type(lst_of_words)) # returns a list
    # print(len(lst_of_words)) # should return 20
    # 4. confirm that the sentence is 20 words
    if len(lst_of_words) > MAX_WORDDS:
        print('--> Error: This sentence does not contain 20 words')
        sys.exit()

# for loop to seperate the 5 words
    for i in range(0, MAX_WORDDS, WORDS_PER_LST):
        n = i
        placeholder = lst_of_words[n:n + WORDS_PER_LST]
        sectioned_words.append(placeholder)
    i = 0
    for i in range(len(sectioned_words)):
        line = ' '.join(sectioned_words[i])
        line = line + '\n'
        sectioned_lines.append(line)
        i += 1
        # print(len(sectioned_lines))
        # writing_files(sectioned_lines)
    # for index in range(len(sectioned_lines)):
    #     writing_files(sectioned_lines[index])
    #     index += 1
    conjoined_line = ''.join(sectioned_lines)
    print(type(conjoined_line))
    writing_files(conjoined_line)


def reading_files():
    try:
        text_file = open(READFILE, "r")
        create_twenty_lst(text_file)
        text_file.close()
    except CannotOpenFile:
        print(f"--> Error: Cannot open file {READFILE}")
# 2. Make it readable


reading_files()

# print(lst_of_words[n:n + WORDS_PER_LST]) # gives a seperated list of words
# # print(grouped)
# print(sectioned_words)
# remove_new_line = data[:-1]
# lst_of_words.append(remove_new_line)
# print(lst_of_words)
