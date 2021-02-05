# program to make a request to the coindesk api and return the bitcoin values
# author glen gardiner

# v1


import requests
import pprint

url_to_get = "https://api.coindesk.com/v1/bpi/currentprice.json"

my_data = requests.get(url_to_get)

bc_dict = my_data.json()

pprint.pprint(bc_dict)

# create tuples by iterating over the dict
for bc_rate in bc_dict['bpi'].items():
    
    # set variable for unpacking
    a, b = bc_rate
    # unpack currency
    print(a)
    # unpack rate
    print(b['rate'])
