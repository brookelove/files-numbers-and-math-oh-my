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


def checking_for_duplication(my_lst):
    i = 0
    for i in len(my_lst):
        j = i + 1
        if my_lst[i] == my_lst[j]:
            i += 1
            j += 1
            return False
        else:
            return True


def ascendingNumber():
    user_input = input('Enter a Number: ')
    # int_user_input = int(user_input)
    lst_user_input = list(user_input)
    if lst_user_input[0] < lst_user_input[1] and lst_user_input[1] < lst_user_input[2] and len(lst_user_input) == 3:
        return user_input
    elif float(user_input) or str(user_input):
        raise NonInteger
    elif len(lst_user_input) > 3:
        raise OutofBounds
    elif lst_user_input[0] > lst_user_input[1] or lst_user_input[1] > lst_user_input[2]:
        raise NotAscending
    elif checking_for_duplication(lst_user_input):
        raise Duplication


def main():
    complete = False
    while not complete:
        try:
            ascendingNumber()
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
