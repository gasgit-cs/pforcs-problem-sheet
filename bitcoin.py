# program to make a request to the coindesk api and return the bitcoin values
# author glen gardiner

# v1

# import module requests for making http get request to api
import requests
# import module pprint( prints json in easy formay for humans to read )
import pprint

# create url to the api
url_to_get = "https://api.coindesk.com/v1/bpi/currentprice.json"

# create a  var ( my_data ) to store the returned dat from the get request
my_data = requests.get(url_to_get)
#print(my_data) # test
# convert the response to json
bc_dict = my_data.json() #test


#print(type(bc_dict)) #test


# print the object to readable format
pprint.pprint(bc_dict)
print("Rates Now :) | :(")
# unpack tuples by iterating over the dict items
for bc_rate in bc_dict['bpi'].items():

    #print(type(bc_rate)) #test
    # use a, b variables for unpacking
    a, b = bc_rate
    # unpack currency
    # print(type(a)) #test
    # print(a) #test
    # unpack rate
    # print(type(b)) #test
    # print(b['rate']) #test

    print("{} current rate of bitcoin is {}".format(a, b['rate']))



