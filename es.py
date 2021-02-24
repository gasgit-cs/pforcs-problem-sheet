# program to read in a file and count ocurrence of a char
# author glen gardiner
# run program calling es.py and passing the name of a file to read

# example: python es.py Lorem-ipsum.txt

import sys

# fn - filename
# i - input from user
# uc - uppercase i
# lc - lowercase i

fn = sys.argv[1]
# get letter from user
i  = input("Enter the letter you require counted: ")

# convert input to upper and lower
uc = i.upper()
lc =  i.lower()

# f - file
# t - text
# l - line
# c - charachter

def read_file(fn, lc, uc):
    # count all non space charachter
    count_all = 0
    # count lower
    count_lower = 0
    # count upper
    count_upper = 0

    try:
        # open file in read mode
        f = open(fn, "r")
        # read file to var t
        t = f.readlines()
        # iterate for each line in t
        for line in t:
            # print(line)
            # iterate for each char in each line
            for c in line:
                # check if c is a space
                if not c.isspace():
                    # if not increment count_all counter
                    count_all +=1
                    # check if c is lowercase
                    if c == lc:
                        # increment count_lower
                        count_lower += 1
                    # check if c is uppercase
                    elif c == uc:
                        # increment count_upper
                        count_upper +=1

        count_total = count_lower + count_upper       
        # display count result
        print("Total Chars count: {} \t Total Lower input: {} \t Total Upper input: {} \t Total input: {}".format(count_all,count_lower, count_upper, count_total))
        # close the file
        f.close()
        # catch teh exception and display my message and built in python message (e)
    except Exception as e:
        # my message
        print("File not found, check name and path:(")
        # python exception message
        print(e)
       


read_file(fn, lc, uc)

