# test file for functions in average_to.py 
# author glen gardiner

# not completed yet :(

# import functions to test
from average_to import get_input_index , create_random_list, average_to

# test negative number
def test_get_input_index():
    assert get_input_index(), "Fail! - negative value entered"
# test random list / not completed
def test_range_random_list():
    pass
# text for empty list
def test_average_to_list():
    assert average_to([], 3), "Fail! - new list is empty"
# division by zero
def test_average_to_divide():
    assert average_to([10,20,30,40], 0), "Cannot divide by zero"


if __name__ == "__main__":

    #test_get_input_index()
    test_range_random_list()
    #test_average_to_list()
    #test_average_to_divide()
    

    

 



