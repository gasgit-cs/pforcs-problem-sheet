# program to read in a file and count a char
# author glen gardiner


# v1 crude

import sys

filename = sys.argv[1]
uppere = "E"
lowere = "e"


def read_file(filename,lowere, uppere):
    f = open(filename, "r")

    t = f.readlines()

    count = 0

    for x in t:
        print(x)
        for y in x:
            if y == lowere or y == uppere:
                count += 1
        #print(x)
    print(count)
    f.close()



read_file(filename, lowere, uppere)