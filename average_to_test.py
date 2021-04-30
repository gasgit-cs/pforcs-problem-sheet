# test file for functions in average_to.py
# author glen gardiner

# not completed yet :(

# import functions to test
from average_to import get_input_index, create_random_list, average_to

# test negative number
def test_get_input_index_fail():

    assert get_input_index(), "Fail! - negative value entered"

# test range 0 random list failing
def test_range_random_list_fail():
    try:
        assert create_random_list(0,30), "Fail - max cannot be 0"
    except AssertionError as msg:
        print(msg)
# test emptylist random list failing
def test_empty_random_list_fail():
    try:
        assert create_random_list(30,0), "Fail - list is empty"
    except AssertionError as msg:
        print(msg)

# test range random list passing
def test_range_random_list_pass():
    try:
        assert create_random_list(30,6), "Oops"
    except AssertionError as msg:
        print(msg)
    else:
        print("pass")

# test random list pass
def test_random_list_pass():
    try:
        assert create_random_list(30,6), "Oops"
    except AssertionError as msg:
        print(msg)
    else:
        print("pass")
    
# text for empty list
def test_average_to_list_fail():
    try:
        assert average_to([], 3), "Fail! - new list is empty"
    except AssertionError as msg:
        print(msg)
    
def test_average_to_list_pass():
    try:
        assert average_to([1,2,3,4,5,6,7],3), "Oops"
    except AssertionError as msg:
        print(msg)
    else:
        print("pass")
# division by zero
def test_average_to_divide():
    try:
        assert average_to([10, 20, 30, 40], 0), "Cannot divide by zero"
    except AssertionError as msg:
        print(msg)

if __name__ == "__main__":

    #test_get_input_index_fail()

    #test_range_random_list_fail()
    #test_range_random_list_pass()
    #test_empty_random_list_fail()
    #test_random_list_pass()

    #test_average_to_list_fail()
    #test_average_to_list_pass()
    #test_average_to_divide()
