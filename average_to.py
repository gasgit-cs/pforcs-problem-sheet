# create a function to take a list and index, return the average of the numbers
# up to and including the given index

# author glen gardiner


import random
import logging
import sys

# function to take user input, test input is not a negative number, raise exception and log


def get_input_index():
    try:
        my_input = int(input("Enter Int index: "))
        if (my_input < 0):
            logging.error("Non positive number entered %d",
                          my_input, exc_info=True)
            raise ValueError("Non positive number entered")
    except ValueError as e:
        logging.error(e, 'Value Error', exc_info=True)
        print(e)
    else:
        logging.info('Input OK')
        return my_input


def create_random_list(max=50, rge=12):

    try:
        assert max > 0, "max cannot be zero"
        rdm_list = [random.randrange(1, max, 1) for i in range(rge)]
        assert len(rdm_list) !=0,' list is empty'
        print(rdm_list)
        return rdm_list
    except AssertionError as err:
        logging.exception(err)
        raise err
       
    


def average_to(aList, toIndex):
    new_list = [x for x in aList[0:(toIndex + 1)]]
    print(new_list)
    if new_list == []:
        raise Exception("New list is empty")
    else:

        try:
            x = int(sum(new_list))
            print("Summ of new list: ", x)
            avg = x//toIndex

        except ZeroDivisionError as e:
            logging.warning("/0 :()")
            logging.error(e)
            #raise Exception("Division by zero error")
            raise Exception(e)
        else:
            logging.info('Division OK')
            print("Avg of new list:", avg)
            return avg


def main():
    logging.basicConfig(filename='./debug_average.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s -%(name)s -Line: %(lineno)s')

    x = get_input_index()
    y = create_random_list()
    average_to(y, x)


if __name__ == "__main__":
    main()
