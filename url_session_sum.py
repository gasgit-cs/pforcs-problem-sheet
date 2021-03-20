import pandas as pd

# col headers
col_names=('ip','dash1', 'dash2','time','url','statuscode','sizeofresponse','referer','useragent','dunno')
#  read in access log, seps, 
df = pd.read_csv(r'./data/access.log', sep=' ', header=None, names=col_names)
# check df type
print(type(df['time']))
# strip brackets 
df['time'] = df['time'].str.strip('[]')
# check time 
#print(df['time'])
# convert to date time, format
df['time'] = pd.to_datetime(df['time'], format="%d/%b/%Y:%H:%M:%S") 
# set time as index  
df.set_index('time')
# print first 10 rows
print(df.head(10))
# print index
print(df.index)
# print df info
df.info()