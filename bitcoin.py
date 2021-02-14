# program to make a request to the coindesk api and return the bitcoin values
# author glen gardiner

# v1 intial script breakdown of components

# # import module requests for making http get request to api
# #import requests
# # import module pprint( prints json in easy formay for humans to read )
# # import pprint

# # create url to the api
# url_to_get = "https://api.coindesk.com/v1/bpi/currentprice.json"

# # create a var ( my_data ) to store the returned data from the get request
# # pass the url_to_get to requests get and assign results to my_data
# my_data = requests.get(url_to_get)
# #print(my_data) # test output
# # convert the response to json
# bc_dict = my_data.json()

# #print(type(bc_dict)) #test type
# # print the object to readable format using the pretty print module
# pprint.pprint(bc_dict)
# # add title
# print("Rates Now :) || :(")
# # unpack tuples by iterating over the dict items
# for bc_rate in bc_dict['bpi'].items():

#     #print(type(bc_rate)) #test type
#     # use a, b variables for unpacking
#     a, b = bc_rate
# #region
#     # unpack currency
#     # print(type(a)) #test type
#     # print(a) #test
#     # unpack rate
#     # print(type(b)) #test
#     # print(b['rate']) #test
# #endregion

#     print("{} current rate of bitcoin is {}".format(a, b['rate']))


##############################################################################

# v2 complete the program using functions and a main function to call from
# add try, except to catch any connection issues
#
import requests
import pprint


# things to do
# update try, except
# update comments to v2
# move v1 to commented out section at the bottom or delete


def make_request(url_to_get):
    # function to nmake requests from the api
    try:
        my_data = requests.get(url_to_get)
        my_data.raise_for_status()
        print(my_data)
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
    my_data = requests.get(url_to_get)
    return my_data


def convert_my_data(my_data):
    # function to parse and print
    # convert the response to json
    bc_dict = my_data.json()
    # print the object to readable format using the pretty print module
    pprint.pprint(bc_dict)
    # add title
    print("Rates Now :) || :(")
    # unpack tuples by iterating over the dict items
    for bc_rate in bc_dict['bpi'].items():
        a, b = bc_rate
        print("{} current rate of bitcoin is {}".format(a, b['rate']))

# main function as entry point to the program, calling other frinctions


def main():
    # assign full url to url_to_get var
    # pass the url_to_get to requests get and assign results to url_to_get
    url_to_get = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # pass url_to_get to make request function, assign the returned value to data
    data = make_request(url_to_get)
    # pass datto convert function
    convert_my_data(data)


# conditional block to check if the script contains a main function, running while True
if __name__ == "__main__":
    main()
