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
            logging.error("Non positive number entered %d", my_input, exc_info=True)     
            raise ValueError("Non positive number entered")
    except ValueError as e:
        logging.error(e, '\/()\/', exc_info=True)
        print(e)
    else:
        logging.info('Input OK')
        return my_input

        
def create_random_list(max=50):

    if max <= 0:
        print("Range cannot be 0")
    else: 

    
        rdm_list = [random.randrange(1, max , 1) for i in range(12)]
        print(str(rdm_list))
        
        
        # try:
        #     assert max > 0, "Range cannot be 0"
        
        
        
        # except AssertionError as e:
        #     print(e)

        try:
            assert len(rdm_list) != 0, "List is empty." 
            
            return rdm_list
        except AssertionError as err:
            logging.error('List is empty:(')
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
            print("Avg of new list:" ,avg)
            return avg

def main():
    logging.basicConfig(filename='./debug_average.log', filemode='a',level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s -%(name)s -Line: %(lineno)s')

    x = get_input_index()
    y = create_random_list()
    average_to(y, x)


if __name__ == "__main__":
    main()
