# progarm to demonstarte collattz conjuncture
# take an int number from the user, and follow the following steps
# check value
# if its is even divide it by 2
# if it is odd,multiply it by 3 and add 1
# author glen gardiner

# v1

# get inital input from user
inital_value = int(input("Enter integer please: "))
# test inital input

# check number is even with modulo
if (inital_value % 2) == 0:
    print("Value entered {} is even ".format(inital_value))
    even_val = inital_value // 2
    print("Value divided by 2 is: {}  ".format(even_val))
else:
    print("Value entered {} is odd ".format(inital_value))
    odd_val = (inital_value * 3) + 1
    print("Value entered multiplied by 3 + 1 is : {} ".format(odd_val))




