# program to make a request to the coindesk api and return the bitcoin values
# author glen gardiner

import requests
import pprint

# function to nmake requests from the api


def make_request(url_to_get):
    try:
        my_data = requests.get(url_to_get)  # pass url to requests get
        print("Type:", type(my_data))
        print("Response + code: ", my_data)  # print response and code
    except requests.exceptions.HTTPError as e:  # catch error
        print(e.response.text)  # print error

    return my_data  # retuen data

# function to parse and print


def convert_my_data(my_data):
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
