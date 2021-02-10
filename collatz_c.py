# progarm to demonstarte collattz conjuncture
# take an int number from the user, and follow the following steps
# check value
# if its is even divide it by 2
# if it is odd,multiply it by 3 and add 1

# author glen gardiner

# v1

# check if else logic

# get inital input from user
inital_value = int(input("Enter integer please V1: "))
# check number is even with modulo
if (inital_value % 2) == 0:
    print("Value entered {} is even ".format(inital_value))
    even_val = inital_value // 2
    print("Value divided by 2 is: {}  ".format(even_val))
else:
    print("Value entered {} is odd ".format(inital_value))
    odd_val = (inital_value * 3) + 1
    print("Value entered multiplied by 3 + 1 is : {} ".format(odd_val))


#################################################################################

# v2

# take an int number from the user, and follow the following steps
# create function to check
# if its is even divide it by 2 and return as current value
# if it is odd,multiply it by 3 and add 1 return as current value
# using a while loop to keep checking as long as the current value is not 1


def check_value(next_val):
    if (next_val % 2) == 0:
        print("Value entered {} is even ".format(next_val))
        curr_val = next_val // 2
        print("Value divided by 2 is: {}  ".format(curr_val))
        return curr_val

    else:
        print("Value entered {} is odd ".format(next_val))
        curr_val = (next_val * 3) + 1
        print("Value entered multiplied by 3 + 1 is : {} ".format(curr_val))
        return curr_val


# get int from user
next_val = int(input("Enter int please V2: "))
# conditional while loop, ture until returned value from check_value is not == 1
while next_val != 1:
    next_val = check_value(next_val)
else:
    # print exit message once 1 is returned
    print("Exited by 1 :()")

#################################################################################

# v3

# recursive

# get value
# check value
# calculate value
# return current value even or odd
# if not 1 check again


def check_recursive(val_1):
    # check if value is even with modulo
    if(val_1 % 2) == 0:
        # assign val divided by  2
        curr_v = val_1 // 2
        # check if current value is not == 1
        if curr_v != 1:
            print(curr_v)
            # if not pass to check function
            check_recursive(curr_v)
        else:
            # current value is 1, exit
            print("{} Exit ".format(curr_v))
    else:
        # current value is odd, do calculation
        curr_v = (val_1 * 3) + 1
        # check if current value is == 1
        if curr_v != 1:
            print(curr_v)
            # if not pass to check_function
            check_recursive(curr_v)
        else:
            # current value is 1, exit
            print("{} Exit ".format(curr_v))


# get user input
val_1 = int(input("Enter int V3: "))
# pass val_1 to check_recurrsive
check_recursive(val_1)
