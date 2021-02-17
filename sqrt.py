# program to estimate the square root of an positive float using newtons equation N = 1/2(N / G + G)
# N - positive number to find square root of
# G - educated guess
# pass number and inital guess to the equation and check inital estimate, 
# loop using last estimate n times to euqation until estimate is < or equal to N


# author glen gardiner


def num():
    n= float(input("Enter positive float: "))
    return n

def guess():
    g = float(input("Enter guess: " ))
    return g

# function takes 2 args
# n - number to get square root of
# g - educated guess
# e - inital estimate 
# ev - susbequent estimated value
def my_square_root(n, g):
        # e is the inital estimate 
        e = (( n / g ) + g) * 0.5

        print("Inital Estimate: ", e)
        # whie the square of e is greater than n

        while e * e > n:
            # substitute g with inital value for subsequent iterations
            ev = (( n / e ) + e) * 0.5
            print("Subsequent Estimate:",ev)

            e = round(ev, 1)
        else:
            #  return 
            return e
     


# test function, N raised to the power of 0.5
def actual_sqrt(s):
    y = s ** 0.5
    print("Actual Sqrt: ", round(y, 1))
    

def main():
    # get number n 
    x = num()
    s = x
    # print actual sqrt to test
    actual_sqrt(s)
    # get educated guess
    y = guess()
    
    z = my_square_root(x, y)
    print(z)

if __name__ == "__main__":
    main()
