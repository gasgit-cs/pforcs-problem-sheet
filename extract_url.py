# progarms to extract details from log file
# author glen gardiner

# using logfile from splunk example data
import re
import json
import pprint
import os

# file 
my_file = './mydir/access.log'

# function to check file exists
def check_file_path(file_to_check):
    try:
        os.path.exists(file_to_check)
    except FileNotFoundError as e:
        print(e)

# function to check file exists
check_file_path(my_file)

# list to store urls
url_list = []
# list to store json objects
json_list = []

# function to extract the url from the point (space forward slash) ending with (space  HTTP  space)
def extract_url(log):
    url_pattern = re.compile(r'\s\/.*\sHTTP\s')
    url_match = re.search(url_pattern, log)
    if url_match:
        return url_match.group()


# function to extarct resource only, look forward look back
def extract_resource(log):
    res_pattern = re.compile(r'(?<=\s\/).*?(?=\?)')
    res_match = re.search(res_pattern, log)
    if res_match:
        return res_match.group()


# function to extract the varied paramaters from url
def extract_parameters(url):
    par_pattern = re.compile(r'\?|&')
    # cast url to string, split on pattern
    split_list = re.split(par_pattern, str(url))
    # return items as list
    return split_list


# read file in
with open(my_file, encoding="utf-8") as f:
    logfiles = f.readlines()
    # iterate each line
    for log in logfiles: 

        # store paramater dict objects
        parameters = {}
       
        # extarct urls
        my_url = extract_url(log)
        # append to url list
        url_list.append(my_url)

        # extarct paramaters
        pars = extract_parameters(my_url)
        # iterate over parameter list excluding the first
        # example [' /cart.do', 'action=changequantity', 'itemId=EST-15', 'productId=SC-MG-G10', 'JSESSIONID=SD0SL9FF8ADFF6607 HTTP']
        for parameter in pars[1:]:
            # split on the =
            k, v = re.split("=", parameter)
            # create a dict object with the k,v
            par_dict = dict({k: v})
            # update paramaters dict
            parameters.update(par_dict)

        # extarct resource from log
        res = extract_resource(log)
        # create new dict using resource and paramaters dicts
        res_and_pars = dict({'resource': res, 'paramaters': parameters})
        
        # append to json list
        json_list.append(res_and_pars)

# write out the json objects list to a a json file
with open('./mydir/jsonlist.json', 'w') as f:
    json.dump(json_list, f)

# write out list of urls to utf-8 text file
with open('./mydir/urllist', 'w', encoding='utf-8') as f:
    f.write(str(url_list))

with open('./mydir/jsonlist.txt', 'w', encoding='utf-8') as f:
    f.write(str(json_list))

def message():
    print("Sorted, check mydir for results to file!")


message()