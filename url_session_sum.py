# program to read in log file, use pandas and reg ex to work with data
# author glen gardiner

import pandas as pd
import re

# col headers
col_names=('ip','dash1', 'dash2','time','url','statuscode','sizeofresponse','referer','useragent','dunno')
#  read in access log
df = pd.read_csv(r'./mydir/short_access.log', sep=' ', header=None, names=col_names)
# check df type
print(type(df['time']))
# strip brackets 
df['time'] = df['time'].str.strip('[]')
# check time 
#print(df['time'])
# convert to datetime, format
df['time'] = pd.to_datetime(df['time'], format="%d/%b/%Y:%H:%M:%S") 
# prin first 4 to test
print(df.head(4))
# drop unwanted columns
df.drop(columns=['ip','dash1','dash2'], inplace=True)
# set time as index  
df.set_index('time')
# print to test
print(df['url'])
# print first 10 rows
#print(df.head(10))
# print index
# print(df.index)
# print df info
# df.info()
# print(df.describe())
# regex function to extract the session id 
def extract_sessionid(x):
    x = re.search(r'((?<=JSESSIONID=).*?(?=\sHTTP\s))',x).group()
    return x
# create new column my_extract and apply extract function to url
df['my_extract_sid'] = df['url'].apply(extract_sessionid)
# function to group (my extracted sid) and (size of response), itreate and unpack k,v , print k, valuses in v and sum values in v 
def unpack_print_group_by():
    total_mbs_unpack = df.groupby(['my_extract_sid'])['sizeofresponse']
    for k, v in total_mbs_unpack:
        print("SID: {}  Downloads {} Total Downloaded {} ".format(k, [x for x in v], v.sum()))
unpack_print_group_by()    
# function to group (my extracted sid) and (size of response), summing of response
def sum_downloads():

    total_mbs = df.groupby(['my_extract_sid'])['sizeofresponse'].sum()

    print(total_mbs)

sum_downloads()

## to do 
## create plot of data




