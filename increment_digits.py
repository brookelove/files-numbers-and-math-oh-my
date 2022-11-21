'''
1. prompt use for a three digit whole number 
2. spilt the information in number_placelholeder list 
3. then take the index of the first number and put it into a compare_list 
4. number index and add 1 and then add 2
5. then .join() the list together (compare_str) 
6. use if else statement
    i. if compare_str == user_input; then print Number accepted!
    ii. else; call the user input and then run the function again 
'''


class Duplication(Exception):
    pass


class OutOfBounds(Exception):
    pass


class NonInteger(Exception):
    pass


class NotAscending(Exception):
    pass


incrementing_number = []


def the_same(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if i == j:
                return True


def check_if_increment(num, lst):
    num = int(lst[0])
    for i in range(num, num + 3):
        incrementing_number.append(str(i))
    increment_str = ''.join(incrementing_number)
    if int(increment_str) == num:
        return True


def get_user_input():
    user_input = int(input("Please enter a 3-digit: "))
    split_input = list(user_input)

    # conditions for all for custom exceptions all of them might seperate into functions
    if str('.') in user_input:
        raise NonInteger
    elif the_same(user_input) == True:
        raise Duplication
    elif check_if_increment(int(user_input), split_input) == True:
        raise NotAscending
    elif len(split_input) > 3:
        raise OutOfBounds
    return user_input


def mainfunc():
    complete = False
    while not complete:
        try:
            num = get_user_input()
            print("Number Accepted!")
        except Duplication:
            print('--> Error: Your number contains a Duplication')
        except OutOfBounds:
            print('--> Error: You did not enter a 3-digit number.')
        except NonInteger:
            print('--> Error: This is not an integer. Please re-enter.')
        except NotAscending:
            print('--> Error: The digits are not in ascending order.')


mainfunc()
# while True:

# placeholder = list(user_input)
# # print(placeholder)  # prints ['4', '5', '6']
# if float(user_input) == True:
#     print("---> Error: This is not an integer. Please re-enter.")
#     continue
# elif len(placeholder) > 3:
#     print("---> Error: You did not enter a 3-digit number")
#     continue
# # elif duplication(num)
# else:
#     print("Number Accepted!")
#     break
