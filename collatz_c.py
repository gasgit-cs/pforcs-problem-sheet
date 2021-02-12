# progarm to demonstarte collattz conjuncture
# take an int number from the user, and follow the following steps
# check value
# if its is even divide it by 2
# if it is odd,multiply it by 3 and add 1

# author glen gardiner


#################################################################################

# v2

# take an int number from the user, and follow the following steps
# create function to check
# if its is even divide it by 2 and return as current value
# if it is odd,multiply it by 3 and add 1 return as current value
# using a while loop to keep checking as long as the current value is not 1


# get value
# check sign
# check parity
# calculate value
# return current value even or odd
# if not 1 check again


def check_value(next_val):
    if (next_val % 2) == 0:
        curr_val = next_val // 2
        print(curr_val,  end=" ")
        return curr_val
    else:
        curr_val = (next_val * 3) + 1
        print(curr_val, end=" ")
        return curr_val

def get_input():
    val_1 = int(input("Enter int: "))
    return val_1

# check parity, if not negative and greater then 0 return, else return get input
def check_par(val_1):
    if val_1 != type(int()) and val_1 > 0:
        #print("Returned", str(val_1))
        return val_1
    else:
        print("Not Positive Input, Try Again:)")
        return get_input()
# while 
def meet_condition(next_val):
    while next_val != 1:
        next_val = check_value(next_val)
    else:
        # print exit message once 1 is returned
        print("Exited by 1 :()")

def main():

    input1 = get_input()
    next_val = check_par(input1)
    meet_condition(next_val)


if __name__ == "__main__":
    main()

# while next_val != 1:
#     next_val = check_value(next_val)
# else:
#     # print exit message once 1 is returned
#     print("Exited by 1 :()")


# conditional while loop, ture until returned value from check_value is not == 1



#################################################################################

# v3

# recursive
# 
# get value
# check sign
# check parity
# calculate value
# return current value even or odd
# if not 1 check again

# def check_recursive(val_1):
#     # check if value is even with modulo
#     if(val_1 % 2) == 0:
#         # assign val divided by  2
#         curr_v = val_1 // 2
#         # check if current value is not == 1
#         if curr_v != 1:
#             print(curr_v)
#             # if not pass to check function
#             check_recursive(curr_v)
#         else:
#             # current value is 1, exit
#             print("{} Exit ".format(curr_v))
#     else:
#         # current value is odd, do calculation
#         curr_v = (val_1 * 3) + 1
#         # check if current value is == 1
#         if curr_v != 1:
#             print(curr_v)
#             # if not pass to check_function
#             check_recursive(curr_v)
#         else:
#             # current value is 1, exit
#             print("{} Exit ".format(curr_v))
# # get input 
# def get_pos_input():
#     val_1 = " "
#     val_1 = int(input("Enter int please V3: "))
#     return val_1
# # check parity, if not negative and greater then 0 return, else return get input
# def check_par(val_1):
#     if val_1 != type(int()) and val_1 > 0:
#         #print("Returned", str(val_1))
#         return val_1
#     else:
#         print("Not Positive Input, Try Again:)")
#         return get_pos_input()
   
# def main():
#     x = get_pos_input()
#     y = check_par(x)
#     # pass y as val_1 to check_recurrsive
#     check_recursive(y)

# if __name__ == "__main__":
#     main()




