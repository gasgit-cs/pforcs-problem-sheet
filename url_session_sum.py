import pandas as pd
import re



# I want to find which sessionId downloaded the most data

# Read the access.log into a dataframe (see lab)
# Set the date time to be the index (you will need to manipulate this data, see lab)
# Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
# Use groupBy to get the sum of all the data downloaded by each sessionId.
# Create a plot of this (type of your choice)
# Extra:
# I have not written this code myself so I don't know how hard it is......
# Work out the amount of data each sessionId downloaded in any given day




#pd.set_option('max_colwidth', 800)
# col headers
col_names=('ip','dash1', 'dash2','time','url','statuscode','sizeofresponse','referer','useragent','dunno')
#  read in access log, seps, 
df = pd.read_csv(r'./mydir/access.log', sep=' ', header=None, names=col_names)
# check df type
print(type(df['time']))
# strip brackets 
df['time'] = df['time'].str.strip('[]')
# check time 
#print(df['time'])
# convert to date time, format
df['time'] = pd.to_datetime(df['time'], format="%d/%b/%Y:%H:%M:%S") 
# 
print(df.head(4))

df.drop(columns=['ip','dash1','dash2'], inplace=True)
# set time as index  
df.set_index('time')

print(df['url'])
# print first 10 rows
print(df.head(10))
# print index
print(df.index)
# print df info
df.info()
print(df.describe())


# regex function to extract the session id 
def extract(x):
    x = re.search(r'((?<=JSESSIONID=).*?(?=\sHTTP\s))',x).group()
    return x
# create new column my_extract and apply extract function to url
df['my_extract'] = df['url'].apply(extract)
# check df
print(df['my_extract'])



