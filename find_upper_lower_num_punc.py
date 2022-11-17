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
upper = []
lower = []
digits = []
punc = []

sentences = re.split(' . ', docstring)

for i in sentences:
    u = 0
    l = 0
    d = 0
    p = 0
    # print(i)  # returns each sentenece with.
    # print(type(i))
    current_sentence = list(i)
    for j in current_sentence:
        if j in string.ascii_lowercase:
            l += 1
        elif j in string.ascii_uppercase:
            u += 1
        elif j in string.digits:
            d += 1
        elif j in string.punctuation:
            p += 1
    upper.append(u)
    lower.append(l)
    digits.append(d)
    punc.append(p)
print(upper)
print(lower)
print(digits)
print(punc)
