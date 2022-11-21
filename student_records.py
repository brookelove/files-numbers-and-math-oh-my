# try block for opening the file and have an except if it can not open
# open the text file
class CannotOpenFile(Exception):
    pass


student_records = []
try:
    text_file = open("cs412_3_5_input.txt", 'r')

except CannotOpenFile:
    print("Unable to read file")

# need to have a for loop to run thrugh the data while the line is  == \n
for line in text_file:
    # print(line)  #prints our ever line on the textfile!
    # use use .strip() take off the \n , and .
    remove_extra_char = line.strip(".,\n")
    # print(remove_new_line)  # prints new line with no \n at the end of it
    split_line = remove_extra_char.split(' ')
    # join together the first two words to get one name
    split_line[0:2] = [' '.join(split_line[0:2])]

    # print(split_line) # returns name with firstand last together
    join_to_tuple = [str(i) for i in split_line]
    # print(join_to_tuple)
    # print(tuple(join_to_tuple))
    student_records.append(tuple(join_to_tuple))
    # tuple_line = map_line
    # print(tuple_line)
    # # doing this sepeates them into different tuples but all characters
    # line_tuple = tuple(remove_new_line)
    # print(line_tuple)
text_file.close()
print(student_records)

# take the informaation make it into a tuple then convert
# appen d that tuple into a list

# take the information and split it into different sections
# append to the tuple
# append the tuple into a list
# then tell the file to go tothe next line
# data = text_file.readline()
# print(data)
# text_file.close()
