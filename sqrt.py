# program to estimate the square root of an positive float using newtons equation N = 1/2(N / G + G)
# N - positive number to find square root of
# G - educated guess
# pass number and inital guess to the equation and check inital estimate, 
# loop using last estimate n times to euqation until estimate is < or equal to N


# author glen gardiner


def num():
    n= float(input("Enter float: "))
    return n

def guess():
    g = float(input("Enter guess: " ))
    return g

# function takes 2 args
# n - number to get square root of
# g - educated guess
# x - inital estimate and estimate until condition is satisfied 

def my_square_root(n, g):
        # x is the inital estimate 
        x = (( n / g ) + g) * 0.5
        # loop until estimate squared is less than or equal to N
        while x * x > n:
            # calculate using current estimate
            x = (( n / g ) + g) * 0.5
            
            return x
# test function
def actual_sqrt(x):
    print("Actual SQRT: ", round(x ** .5, 1))


def main():
    # get number n 
    x = num()
    # print actual sqrt to test
    actual_sqrt(x)
    # get educated guess
    y = guess()
    
    z = my_square_root(x, y)
    print(z)

if __name__ == "__main__":
    main()
