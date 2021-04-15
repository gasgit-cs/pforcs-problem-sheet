from average_to import get_input_index , create_random_list, average_to

def test_get_input_index():
    assert get_input_index(), "Fail! - negative value entered"

def test_create_random_list():
    assert create_random_list(), "Fail! - somethig went wrong:() "

def test_average_to():
    assert average_to([], 3), "Fail! - new list is empty"

if __name__ == "__main__":

    test_get_input_index()
    test_create_random_list()
    test_average_to()
    

    

 



