# program to estimate the square root of an positive float using newtons equation N = .5(N / G + G)
# N - positive number to find square root of
# G - educated guess
# pass number and inital guess to the equation and check inital estimate, 
# loop using last estimate n times to euqation until estimate is < or equal to N

# author glen gardiner

from menurq import menu_options as mo
#import math

# 
def num():
    n = float(input("Enter positive num(float): ")) 
    return n

def guess():
    g = float(input("Enter educated guess: " ))
    return g

# function takes 2 args
# n - number to get square root of
# g - educated guess
# i - inital estimate 
# s - susbequent estimated value
def my_square_root(n, g):
  
        # i is the inital estimate 
        i = (( n / g ) + g) * 0.5
        print("Inital Estimate: ", i) 
      
        # whie the square of i is greater than n
        while  i * i > n:
            # substitute g with inital value for subsequent iterations
            s = (( n / i ) + i) * 0.5
            print("Subsequent Estimate:", s)
            # if estimate and sub estimate are equal, round required
            if s == i:
                return round(i,1)
            else:
                i = s
        else:
            # return 
            return i
     
# function, N raised to the power of 0.5
def actual_sqrt(s):
    y = s ** 0.5
    print("Actual Sqrt: ", round(y, 1))


def main():
    
    while True:
        # using menu_option from my menrq module
        mo()
        #7call num function and assign return to x
        x = num()
        # assign x to s for test function
        s = x
        # print actual sqrt to test
        #actual_sqrt(s)
        # call guess function and assige return to y
        y = guess()
        # pass x & y to my_square_root function
        z = my_square_root(x, y)
        # f-string format, value unchanged 
        z1 = f'{z:.1f}'
        # print final estimate
        print("SQRT is {}".format(z1))
        
# conditional function check for main 
if __name__ == "__main__":
    # call main to control the program
    main()

    
