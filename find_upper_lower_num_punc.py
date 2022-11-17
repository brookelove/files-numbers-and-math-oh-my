'''
1. create a docstring with three sentences
2. use split() methond
    a. append it to a new list
3. use a for loop to go through the seperated_sentence_list
    a. have 4 different lists all global (uppercase, lowercase, digits, punctuation)
        - using import string (string.ascii_lowercase,string.ascii_uppercase, string.ascii_punctuation, string.ascii_lowercase, string.digits)
4. print results in a table that are formated well using docstring and f-types
'''
import re
import string
docstring = '''I love to code with python. I love having three dogs with me. I want to learn how to make bread.'''
upper = 0
lower = 0
digits = 0
punc = 0
i = 0
sentences = re.split(' . ', docstring)

for i in sentences:
    # print(i)  # returns each sentenece with.
    # print(type(i))
    placeholder_sentence = list(i)
    # for j in i:
    #     if j in string.ascii_lowercase:
    #         lower += 1
    #     if j in string.ascii_uppercase:
    #         upper += 1
    #     if j in string.digits:
    #         digits += 1
    #     if j in string.punctuation:
    #         punc += 1
