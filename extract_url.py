# progarms to extract details from log file
# author glen gardiner

# using logfile from splunk example data 
import re
import json
import pprint
import os
import pickle

my_file = './mydir/access.log'
 
# list to store urls
url_list = []
# list to store json objects
json_list = []

# return no match message as n
def no_match():
    n = None
    return n

# function to extract the url beginnib=ng with a (space forward slash -  ending HTTP )
def extract_url(log):
    #d = re.search(r'(GET|POST)<?\s/.*HTTP|http$', arg)
    url_pattern = re.compile(r'\s\/.*HTTP|http$')
    url_match = re.search(url_pattern, log)
    #d = re.search(r'\s\/.*HTTP|http$', arg)
    if url_match:
        return url_match.group()
    else:
        no_match()
        
# function to extarct resource only, look forward look back
def extract_resource(arg):
    res_pattern = re.compile(r'(?<=\s\/).*?(?=\?)')
    res_match = re.search(res_pattern , arg)
    if res_match:
        return res_match.group()
    else:
        no_match()

# function to extract the varied paramaters from url
def extract_parameters(arg):
    par_pattern = re.compile(r'\?|&')
    # cast arg to string 
    split_list = re.split(par_pattern, str(arg))
    return split_list

# read file in
with open( my_file, encoding="UTF-8") as f:
    logfiles = f.readlines()
    # iterate each line
    for log in logfiles:        
        # staore paramatersdict objects
        parameters = {}
        # extarct urls
        my_url = extract_url(log)
        #print(log)
        # append to url list
        url_list.append(my_url)
        # extarct paramaters
        pars = extract_parameters(my_url)
        #print(pars)
        #print(p)
        # iterate over parameter list exclding the first
        # example [' /cart.do', 'action=changequantity', 'itemId=EST-15', 'productId=SC-MG-G10', 'JSESSIONID=SD0SL9FF8ADFF6607 HTTP']
        for parameter in pars[1:]:
            # split on the =
            k,v = re.split("=", parameter)
            # create a dict object with the k,v
            par_dict = dict({k:v})
            # update paramaters dict
            parameters.update(par_dict)
        # extarct resource
        res = extract_resource(log)
        # create new dict using resource and paramaters dicts
        res_and_pars = dict({'resource':res, 'paramaters': parameters})
        # append to json list
        json_list.append(res_and_pars)

# 
with open('./mydir/jsonlist.json', 'w') as filehandle:
    json.dump(json_list, filehandle)

with open('./mydir/urllist', "wb") as fp:
    pickle.dump(url_list, fp)
   



    

 




    
    




