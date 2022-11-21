'''
1. prompt user to enter a three digit number
    a. have to get it validated as a number verses a letter!
        I. while loop
2.there has to be a loop that constatnly asks for the ascending value
    a. either it is the correct answer or one of the for digits must be answered
        I. using custom class
            i. No duplictions
            ii. no integers greater than 3
            iii. entereing a float
            iv. not in asxcending order
'''


class Duplication(Exception):
    pass


class OutofBounds(Exception):
    pass


class NonInteger(Exception):
    pass


class NotAscending(Exception):
    pass


def checking_for_duplication(num):
    i = 0
    my_lst = list(num)
    for i in len(my_lst):
        j = i + 1
        if my_lst[i] == my_lst[j]:
            i += 1
            j += 1
            return False
        else:
            return True


def check_if_ascending():
    user_input = input('Enter a Number: ')
    if list(user_input[0]) < list(user_input[1]) < list(user_input[2]):
        return user_input
    elif check_if_ascending(user_input) == False:
        raise Duplication
    elif list(user_input[0]) > list(user_input[1]) or list(user_input[1]) > list(user_input[2]):
        raise NotAscending
    elif user_input != type(int):
        raise NonInteger
    elif len(list(user_input)) > 3:
        raise OutofBounds


def main():
    complete = False
    while not complete:
        try:
            check_if_ascending()
            print("Number Accepted!")
            complete = True
        except Duplication:
            print("--> Error: Your number contains a duplication.")
        except OutofBounds:
            print("--> Error: You did not enter a 3-digit number.")
        except NonInteger:
            print("--> Error: This is not an integer. Please re-enter")
        except NotAscending:
            print("The digits are not in ascending order")


main()
