#let's calculate the factorial of a number using for loops

#import sys

#while True:
#    user_input = raw_input()
#    if user_input == 'exit':
#        sys.exit()
#    else:
#        num = int(user_input)
#        fact = 1
#        if num != 0 and num != 1:
#            for i in range(num):
#                fact = fact * num
#                num = num - 1
#        print fact


import sys

def factorial(n):
        fact = 1
        if n != 0 and n != 1:
            for i in range(n):
                fact = fact * n
                n = n - 1
        return fact

def type_error():
     print('You must type a positive integer number!')
     
while True:
    user_input = raw_input()
    if user_input == 'exit':
        sys.exit()
    else:
        try:
            input_to_int = int(user_input)
            if input_to_int < 0:
                type_error()
            else:
                print(factorial(input_to_int))
        except ValueError:
            type_error()
        
