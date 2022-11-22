class Duplication(Exception):
    pass


class OutOfBounds(Exception):
    pass


class NonInteger(Exception):
    pass


class NotAscending(Exception):
    pass


def get_value_from_user():
    user_input = input('Please enter a 3-digit integer: ')
    print(type(user_input))
    # print(type(1)) # returns int
    # print(len(user_input))  # returns the length of the string '565' is 3
    # print(user_input[0]) # prints the first digit in the array
    if not user_input.isdigit():
        raise NonInteger
    elif user_input[0] > user_input[1] or user_input[1] > user_input[2]:
        raise NotAscending
    elif user_input[0] == user_input[1] or user_input[1] == user_input[2] or user_input[0] == user_input[2]:
        raise Duplication
    elif len(user_input) != 3:
        raise OutOfBounds
    return user_input


def main():
    complete = False
    while not complete:
        try:
            get_value_from_user()
            print("Number Accepted!")
            complete = True
        except Duplication:
            print('--> Error: Your number contains a duplication')
        except OutOfBounds:
            print('--> Error: You did not enter a 3-digit number')
        except NonInteger:
            print('--> Error: This is not an integer. Please re-enter')
        except NotAscending:
            print('--> Error: The digits are not in ascending order')


main()
