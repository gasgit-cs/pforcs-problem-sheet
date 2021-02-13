# progarm to demonstarte collattz conjuncture
# take a int from the user, and follow steps
# check is valid int(sign)
# if its is even divide by 2
# if it is odd,multiply by 3 and add 1
# return, store and display values

# author glen gardiner

# list data structure to store values
col_list = []

# get and return int fron user
def get_input():
    i = int(input("Enter int: "))
    return i

# check sign, if not greater than 0, get input and check sign again
def check_sign(s):
    if s > 0:
        return s
    else:
        print("Not Positive Input, Try Again:)")
        i = get_input()
        return check_sign(i)

#  check parity, do calculation, append to list and return value
def check_par(cp):
    if (cp % 2) == 0:
        curr_val = cp // 2
        col_list.append(curr_val)
        return curr_val
    else:
        curr_val = (cp * 3) + 1
        col_list.append(curr_val)
        return curr_val

# while condition is true, check and return or break
def meet_condition(mc):
    while True:
        if mc != 1:
            mc = check_par(mc)
        else:
            break
 # iiterate list and display       
def display_col_list():
    for x in col_list:
        print(x, end=" ")

# main function to organise/control program flow
def main():
    cs = get_input()
    mc = check_sign(cs)
    meet_condition(mc)
    display_col_list()

if __name__ == "__main__":
    main()
