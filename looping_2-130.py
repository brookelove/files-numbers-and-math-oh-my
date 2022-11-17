'''
1. for loop hat loops through integers from 2 and 130 
    a. global constant that are minimum and maximum value 
2. each integer in the loop: odd, even, squares, and cubed
    A. EVEN:
        a. indicate an empty list for both even (GLOBAL SCOPE)
        b. num % 2 = 0 
            i. take that num and append it to the even_list
    B. ODD: 
        a. indicate an empty list for odd (GLOBAL SCOPE)
        b. num % 2 = 1
            i. take that num and append it to the odd_list
    C. SQUARES:
        a. indicate an empty list for sqaure results (GLOBAL SCOPE)
        b. take the num and sqaure the number if it returns 0 
        c. append that to the sqaure list
    D. CUBED:
        a. indicate an empty list for cube results (GLOBAL SCOPE)
        b. take the num and cube the number if it returns 0 
        c. append that to the cubed list
'''
import math
MINVALUE = 2
MAXVALUE = 130
odd_list = []
even_list = []
squared_list = []
cubed_list = []


def loopingthroughnumbers():
    for num in range(MINVALUE, MAXVALUE+1):
        sqaure_rt = round(math.sqrt(num))
        cubed_rt = round(num**(1/3))
        if (num % 2 == 0):
            even_list.append(num)
        if (num % 2 == 1):
            odd_list.append(num)
        if (sqaure_rt * sqaure_rt == num):
            squared_list.append(num)
        if (cubed_rt * cubed_rt * cubed_rt == num):
            cubed_list.append(num)


loopingthroughnumbers()

print("Checking numbers from 2 to 130")
print(f"Odd ({len(odd_list)}) : {odd_list[0]}...{odd_list[-1]}")
print(f"Even ({len(even_list)}) : {even_list[0]}...{even_list[-1]}")
print(f"Square ({len(squared_list)}) : {squared_list}")
print(f"Cube ({len(cubed_list)}) : {cubed_list}")
