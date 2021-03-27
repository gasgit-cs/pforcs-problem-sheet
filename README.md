
# pforcs-problem-sheet G00305555 

## W01

### ***Setup***

Install all enviroments and tools required for this module/course.

#

## W02

### ***Program to create a bmi calculator***

Get user input for height(cms) and weight(kg), calculate bmi.

BMI = kg/m2

[HSE BMI Chart] (https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf)

Program output

```bash
We need some details to calculate:)


Enter your height cms: 180
Height: 1.8
Enter your weight kg: 60
Weight: 60.0


Your BMI is : 18.51851851851852
```

#

## W03

### ***Program to get current bitcoin values***

Utilse the coindesk api, parse the response, unpack and print bitcoin values


### Requirements

Imported modules requests & pprint.

Requests for making http get/post requests to the api.

Pprint to format json output( easy read )

```bash
{'bpi': {'EUR': {'code': 'EUR',
                 'description': 'Euro',
                 'rate': '31,491.0611',
                 'rate_float': 31491.0611,
                 'symbol': '&euro;'},
         'GBP': {'code': 'GBP',
                 'description': 'British Pound Sterling',
                 'rate': '27,627.9448',
                 'rate_float': 27627.9448,
                 'symbol': '&pound;'},
         'USD': {'code': 'USD',
                 'description': 'United States Dollar',
                 'rate': '37,937.2894',
                 'rate_float': 37937.2894,
                 'symbol': '&#36;'}},
 'chartName': 'Bitcoin',
 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
               '(USD). Non-USD currency data converted using hourly conversion '
               'rate from openexchangerates.org',
 'time': {'updated': 'Feb 5, 2021 22:27:00 UTC',
          'updatedISO': '2021-02-05T22:27:00+00:00',
          'updateduk': 'Feb 5, 2021 at 22:27 GMT'}}
```

Program output

```bash
Rates Now :) || :(
USD current rate of bitcoin is 37,849.0204
GBP current rate of bitcoin is 27,563.6627
EUR current rate of bitcoin is 31,417.7906
```

#

## W04

### ***Program to demo Collatz conjecture***

Take an int from the user and calculate steps

*Steps*\
        take an integer from user\
        determine parity\
        if it is even divide it by 2 and return as current value, add to list\
        if it is odd, multiply it by 3 and add 1 and return as current value add to list\
        conditional checking until current value is 1, exit

        

### Requirements

None

Program output

```bash
Enter int: 10
1 Exit!
Collatz Result
5 16 8 4 2 1
```

#

## W05

### ***Program to apply Newtons Equation for square root***

Program to estimate the square root of a positive float using newtons equation N = .5(N / G + G)
N - positive number to find square root of
G - educated guess\

*Steps*\
        pass number and initial  guess to the equation\
        check initial estimate return if close\
        otherwise, loop using the estimate as G\
        n times until estimate is < or equal to N

### Requirements
Import module menurq (simple module to display a menu) 

Program output

```bash
Choose option from list
1 : Run
2 : Quit
Enter choice: 1

Running Program...

Enter Positive Float: 121
Enter educated guess: 5
initial Estimate:  14.6
Subsequent Estimate: 11.443835616438356
Subsequent Estimate: 11.008606819471272
Subsequent Estimate: 11.000003364519355
Subsequent Estimate: 11.000000000000515
Subsequent Estimate: 11.0
SQRT is 11.0
```

#

## W06

### ***Program to read in a file, count occurence of a letter***

Program to take a file name as an argument from console, ask user to enter a letter as input, open and count occurences of the letter


*Steps*\
        pass file to program through console\
        ask user which letter to count
        convert to upper and lower and store in vars lc uc
        open the file with file reader\
        initialise count variables lower, upper\
        iterate over f to extract each line\
        iterate over each line to extract each char\
        check the char is lowercase or uppercase of user input\
        increment counts, add total and print results



### Requirements
I extracted the text from https://www.gutenberg.org/files/2701/old/moby10b.txt\
Created a file called md.txt



Program output
```bash
Enter the letter you require counted: e
Total Chars count: 1009467       Total Lower input: 116960       Total Upper input: 1363         Total input: 118323
```

#

## W07

### ***Program to extract logs from a file using regex***

Program will parse the log file, store urls and paramater dictobjects in lists
Extract paramaters from urls and create a list of json objects

*Steps*\
read in file\
extract url, append to list\
extract paramaters from url\
split out, convert to json objects and store in a dict\ 
extract resource\
build a new nested dict object and append to my list of dict objects\
write results out to files


### Requirements

import re, io, json, pprint

Program output


Sample from urllist.txt

<pre>[' /product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /oldlink?itemId=EST-6&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ',' /product.screen?productId=BS-AG-G09&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /category.screen?categoryId=STRATEGY&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /product.screen?productId=FS-SG-G03&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /cart.do?action=addtocart&itemId=EST-21&productId=FS-SG-G03&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /cart.do?action=purchase&itemId=EST-21&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /cart/success.do?JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /cart.do?action=remove&itemId=EST-11&productId=WC-SH-A01&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /oldlink?itemId=EST-14&JSESSIONID=SD0SL6FF7ADFF4953 HTTP ', ' /product.screen?productId=WC-SH-G04&JSESSIONID=SD7SL8FF5ADFF4964 HTTP ', ' /cart.do?action=addtocart&itemId=EST-18&productId=WC-SH-G04&JSESSIONID=SD7SL8FF5ADFF4964 HTTP ', ' /cart.do?action=purchase&itemId=EST-18&JSESSIONID=SD7SL8FF5ADFF4964 HTTP ', ' /cart/error.do?msg=CreditDoesNotMatch&JSESSIONID=SD7SL8FF5ADFF4964 HTTP ', ' /category.screen?categoryId=NULL&JSESSIONID=SD7SL8FF5ADFF4964 HTTP ', '</pre>


Sample from jsonlist.json


<pre>[{'resource': 'product.screen', 'paramaters': {'productId': 'WC-SH-A02', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': \'oldlink', 'paramaters': {'itemId': 'EST-6', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'product.screen', 'paramaters': {'productId': 'BS-AG-G09', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'category.screen', 'paramaters': {'categoryId': 'STRATEGY', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'product.screen', 'paramaters': {'productId': 'FS-SG-G03', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'cart.do', 'paramaters': {'action': 'addtocart', 'itemId': 'EST-21', 'productId': 'FS-SG-G03', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'cart.do', 'paramaters': {'action': 'purchase', 'itemId': 'EST-21', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'cart/success.do', 'paramaters': {'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'cart.do', 'paramaters': {'action': 'remove', 'itemId': 'EST-11', 'productId': 'WC-SH-A01', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'oldlink', 'paramaters': {'itemId': 'EST-14', 'JSESSIONID': 'SD0SL6FF7ADFF4953 HTTP '}}, {'resource': 'product.</pre>

Sample from jsonlist.json after right click and format documemt to display in human readable format :)

```
[
    {
        "resource": "product.screen",
        "paramaters": {
            "productId": "FS-SG-G03",
            "JSESSIONID": "SD0SL6FF7ADFF4953 HTTP "
        }
    },
    {
        "resource": "cart.do",
        "paramaters": {
            "action": "addtocart",
            "itemId": "EST-21",
            "productId": "FS-SG-G03",
            "JSESSIONID": "SD0SL6FF7ADFF4953 HTTP "
        }
    },
    {
        "resource": "cart.do",
        "paramaters": {
            "action": "purchase",
            "itemId": "EST-21",
            "JSESSIONID": "SD0SL6FF7ADFF4953 HTTP "
        }
    },
    {
        "resource": "cart/success.do",
        "paramaters": {
            "JSESSIONID": "SD0SL6FF7ADFF4953 HTTP "
        }
    },
    {
        "resource": "cart.do",
        "paramaters": {
            "action": "remove",
            "itemId": "EST-11",
            "productId": "WC-SH-A01",
            "JSESSIONID": "SD0SL6FF7ADFF4953 HTTP "
        }
    }
]

```


## W08

### ***Program to Plot with NumPy and Matplotlib***
Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

Program Output

View here: (https://github.com/gasgit-cs/pforcs-problem-sheet/blob/main/plot_task.png)



## W09

### ***Program to read in log file, use pandas and regex to work with data***

Read the access.log into a dataframe\
Set the date time to be the index\ 
Use regular expressions to extract the session id from the URLs and store them in a different column\
Use groupBy to get the sum of all the data downloaded by each sessionId\
Create a plot of this\

Program Output

'''

SID: SD0SL10FF6ADFF5239  Downloads [3986, 432, 3642, 1185, 880, 214, 470, 3818, 3451] Total Downloaded 18078\
SID: SD0SL3FF2ADFF5170  Downloads [769, 306, 2602, 3446] Total Downloaded 7123\
SID: SD0SL5FF6ADFF5249  Downloads [3598, 2154, 2942, 1304, 532, 1702, 1661, 1180] Total Downloaded 15073\
SID: SD0SL6FF7ADFF4953  Downloads [3878, 1748, 2550, 407, 2047, 1201, 486, 3280, 3619, 1352] Total Downloaded 20568\
SID: SD10SL10FF5ADFF5106  Downloads [1711, 2133, 3821, 899] Total Downloaded 8564\
SID: SD10SL7FF8ADFF5413  Downloads [222, 2538, 521, 2919, 3265, 2058, 266, 986, 3531, 1317] Total Downloaded 17623\
SID: SD1SL8FF3ADFF5403  Downloads [3713, 2188] Total Downloaded 5901\ 

or 

my_extract_sid\
SD0SL10FF6ADFF5239     18078\
SD0SL3FF2ADFF5170       7123\
SD0SL5FF6ADFF5249      15073\
SD0SL6FF7ADFF4953      20568\
SD10SL10FF5ADFF5106     8564\
SD10SL7FF8ADFF5413     17623\
SD1SL8FF3ADFF5403       5901

'''


##Steps