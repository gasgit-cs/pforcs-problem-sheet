# create a function to take a list and index, return the average of the numbers
# up to and including the given index

# author glen gardiner


# incomplete ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
import logging
import sys


def get_input_index():
    try:
        my_input = int(input("Enter Int index: "))
        if (my_input < 0):
            logging.error("Non positive number entered %d", my_input, exc_info=True)     
            raise ValueError("Non positive number entered")
    except ValueError as e:
        logging.error(e, '\/()\/', exc_info=True)
        print(e)
    else:
        logging.info('Input OK')
        return my_input

        
def create_random_list():
    rdm_list = [random.randrange(1, 50, 1) for i in range(12)]
    # print(str(rdm_list))
    try:
        assert len(rdm_list) != 0, "List is empty." 
        return rdm_list
    except AssertionError as err:
        logging.error('List is empty:(')
        raise err

def average_to(aList, toIndex):
    new_list = [x for x in aList[0:toIndex]]
    print(new_list)
    try:
        x = int(sum(new_list))
        avg = x//toIndex
   
    except ZeroDivisionError as e:
        logging.warning("/0 :()")
        logging.error(e)
    else:
        logging.info('Division OK')
        return avg

def main():
    logging.basicConfig(filename='./debug_average.log', filemode='a',level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s -%(name)s -Line: %(lineno)s')

    x = get_input_index()
    y = create_random_list()
    average_to(y, x)


if __name__ == "__main__":
    main()
