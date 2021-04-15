# program to read in log file, use pandas and reg ex to work with data
# author glen gardiner

import pandas as pd
import re
import matplotlib.pyplot as plt

# col headers
col_names = ('ip', 'dash1', 'dash2', 'time', 'url', 'statuscode',
             'sizeofresponse', 'referer', 'useragent', 'dunno')
#  read in access log
df = pd.read_csv(r'./mydir/access.log', sep=' ', header=None, names=col_names)

# strip brackets
df['time'] = df['time'].str.strip('[]')

# convert to datetime, format
df['time'] = pd.to_datetime(df['time'], format="%d/%b/%Y:%H:%M:%S")

# prin first 4 to test df
#print(df.head(4))

# drop unwanted columns
df.drop(columns=['ip', 'dash1', 'dash2', 'dunno',
                 'statuscode', 'referer', 'useragent'], inplace=True)
# set time as index
df.set_index('time')

# print first 10 rows to test df
#print(df.head(10))

# regex function to extract the session id
def extract_sessionid(x):
    x = re.search(r'((?<=JSESSIONID=).*?(?=\sHTTP\s))', x).group()
    return x


# create new column my_extract and apply extract function to url
df['jsessionid'] = df['url'].apply(extract_sessionid)

# function to group (jsessionid) and (sizeofresponse), itreate and unpack k,v , print k, values in v and sum values in v
def unpack_print_group_by():
    print('Sample of groups and total by id')
    total_mbs_unpack = df.groupby(['jsessionid'])['sizeofresponse']
    break_point = 0
    for k, v in total_mbs_unpack:
        break_point+=1
        print("JSESSIONID: {}  Downloads: {} Total Downloaded: {} ".format(k, [x for x in v], v.sum()))
        if break_point ==10:
            break

# function to group (jsessionid) and (sizeofresponse), summing (sizeofresponse)
def sum_downloads():
    print('\nSum of group downloads by jsessionid')
    total_mbs = df.groupby(['jsessionid'])['sizeofresponse'].sum().head(10)
    print(total_mbs)

# function to group, sum and sort highest values
def get_highest():

    print("\nSorted sum of top download values")
    total_mbs = df.groupby(['jsessionid']).sum()
    x = total_mbs.sort_values('sizeofresponse', ascending=False)
    print(x.head(5))

# create plot
def my_plot():
    print('\nCreating plot now, check file ./plot_downloads.png or ./plot_downloads_all.py')
    # limit with head 30 to create readable plot
    #total_mbs = df.groupby(['jsessionid'])['sizeofresponse'].sum().head(30)
    # all
    total_mbs = df.groupby(['jsessionid'])['sizeofresponse'].sum()
    pt = pd.Series(total_mbs)

    pt.plot(kind="barh", figsize=(12, 8))
    plt.ylabel("jsessionid")
    plt.xlabel("Total MBS Downloaded")
    plt.title('Total Downloaded by SID')
   # plt.show()
    # plt.savefig('plot_downloads.png')
    plt.savefig('plot_downloads_all.png')


# to do
# get total download by JSID by day
def get_total_day():
    pass


def main():
    # display sample of groups
    unpack_print_group_by()
    # sum download by group
    sum_downloads()
    # sum and sort 
    get_highest()
    # create plot
    my_plot()

    

 
if __name__ == "__main__":
    main()
