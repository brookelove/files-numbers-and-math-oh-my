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


def duplication(num):
    pass


while True:
    user_input = input("Please enter a 3-digit: ")
    placeholder = list(user_input)
    # print(placeholder)  # prints ['4', '5', '6']
    if float(user_input) == True:
        print("---> Error: This is not an integer. Please re-enter.")
        continue
    elif len(placeholder) > 3:
        print("---> Error: You did not enter a 3-digit number")
        continue
    else:
        print("Number Accepted!")
        break
