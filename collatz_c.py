# program to demonstarte collattz conjuncture
# take a int from the user, and follow steps
# check is valid int(sign)
# if its is even divide by 2
# if it is odd,multiply by 3 and add 1
# return, store and display values

# author glen gardiner

# list data structure to store values
# cl - colatz list to store data
cl = []

# get and return int fron user
def get_input():
    # i - input value
    i = int(input("Enter int: "))
    return i

# check sign, if not greater than 0, get input and check sign again
# s - passed value to check sign
def check_sign(s):
    if s > 0:
        return s
    else:
        print("Not Positive Input, Try Again:)")
        i = get_input()
        return check_sign(i)

# check parity, do calculation, append to list and return value
# if (p / 2 == 0 )  p is even
# p - passed value to check parity
# cv - current value
# cl - list to store data
def check_par(p):
    if (p % 2) == 0:
        cv = p // 2
        cl.append(cv)
        return cv
    else:
        cv = (p * 3) + 1
        cl.append(cv)
        return cv

# while loop to check condition( c is not equal to 1 ) is true proceed
#  until false break
# c -  passed value to check condition
def meet_condition(c):
    while True:
        if c != 1:
            c = check_par(c)
        else:
            print("{} exit!".format(c))
            break
 # iiterate list and display in sequence   
def display_col_list():
    print("Collatz Result")
    for x in cl:
        print(x, end=" ")

# main function to organise/control program flow
def main():
    x = get_input()
    y = check_sign(x)
    meet_condition(y)
    display_col_list()

if __name__ == "__main__":
    main()
