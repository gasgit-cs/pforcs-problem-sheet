
# pforcs-problem-sheet G00305555 

## W01
### ***Setup***

Install all enviroments and tools required for this module/course

#

## W02
### ***Program to create a bmi calculator***

Get user input for height(cms) and weight(kg), calculate bmi.

BMI = kg/m2

[HSE BMI Chart](https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf)

Program output

```bash
We need some details to calculate:)


Emter your height cms: 180
Height: 1.8
Enter your weight kg: 60
Weight: 60.0


Your BMI is : 18.51851851851852
```
#

## W03
### ***Program to get current bitcoin values***
Utilse the coindesk api, parse the response,  unpack and print bitcoin values

#

#### ***Requirements***

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
Take a int number from the users and calculate steps\

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
Program to estimate the square root of an positive float using newtons equation N = .5(N / G + G)
N - positive number to find square root of
G - educated guess\

*Steps*\
        pass number and inital guess to the equation\
        check inital estimate return if close\
        otherwise loop using the estimate as G\
        n times until estimate is < or equal to N

### Requirements
Import module menurq ( simple module to display a menu ) 

Program output
```bash
Choose option from list
1 : Run
2 : Quit
Enter choice: 1

Running Program...

Enter Positive Float: 121
Enter educated guess: 5
Inital Estimate:  14.6
Subsequent Estimate: 11.443835616438356
Subsequent Estimate: 11.008606819471272
Subsequent Estimate: 11.000003364519355
Subsequent Estimate: 11.000000000000515
Subsequent Estimate: 11.0
SQRT is 11.0
```



## W06

### ***Program read in a file, count occurence of a letter ***

Program to take a file name as an argument from console, ask user to enter a letter as input, open and count occurences of the letter \


*Steps*\
        pass file to program through console\
        ask user which letter to count
        convert to upper and lower and store in vars lc uc
        open the file with file reader\
        initalise count variables lower, upper\
        iterate over f to extract each line\
        iterate over each line to extract each char\
        check the char is lowercase  or uppercase of user input\
        increment counts, add total and print results\



### Requirements


Program output
```bash
Enter the letter you require counted:a
Total Chars count: 798668        Total Lower input: 60785        Total Upper input: 1536         Total input: 62321
```