# progarms to extract details from log file
# author glen gardiner

# using logfile from splunk example data 
import re
import json
import pprint
import os
import pickle

my_file = './access.log'
 
# list to store urls
url_list = []
# list to store json objects
json_list = []

# return no match message as n
def no_match():
    n = "No Match"
    return n

# function to extract the url beginnib=ng with a (space forward slash -  ending HTTP )
def extract_url(arg):
    #d = re.search(r'(GET|POST)<?\s/.*HTTP|http$', arg)
    d = re.search(r'\s\/.*HTTP|http$', arg)
    if d:
        return d.group()
    else:
        no_match()
        
# function to extarct resource only, look forward look back
def extract_resource(arg):
    r = re.search(r'(?<=\s\/).*?(?=\?)', x)
    if r:
        return r.group()
    else:
        no_match()

# function to extract the varied paramaters from url
def extract_parameters(arg):
    sus = re.split(r'\?|&', str(arg))
    return sus

# read file in
with open( my_file, encoding="UTF-8") as f:
    t = f.readlines()
    # iterate each line
    for x in t:        
        # staore paramatersdict objects
        parameters = {}
        # extarct urls
        url = extract_url(x)
        # append to url list
        url_list.append(url)
        # extarct paramaters
        p = extract_parameters(url)
        # iterate over parameter list
        for j in p[1:]:
            # split on the =
            k,v = re.split("=", j)
            # create a dict object with the k,v
            my = dict({k:v})
            # update paramaters dict
            parameters.update(my)
        # extarct resource
        res = extract_resource(x)
        # create new dict using resource and paramaters dicts
        randp= dict({'resource':res, 'paramaters': parameters})
        # append to json list
        json_list.append(randp)


with open('./listfile.json', 'w') as filehandle:
    json.dump(json_list, filehandle)

with open('./urllist', "wb") as fp:
    pickle.dump(url_list, fp)
   



    

 




    
    




