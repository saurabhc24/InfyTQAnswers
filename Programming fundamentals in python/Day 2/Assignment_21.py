"""
Write a python program to generate and display the next date of a given date.

Assume that
Date is provided as day, month and year as shown in below table.
The input provided is always valid. Output should be day-month-year.
Hint: print(day,"-",month,"-",year) will display day-month-year

+-------+-------------+-----------------+
|       |Sample Input | Expected Output |
+-------+-------------+-----------------+
|  Day  |      1      |                 |
+-------+-------------+                 |
| Month |      9      |     2-9-2015    |
+-------+-------------+                 |
|  Year |     2015    |                 |
+-------+-------------+-----------------+

Also identify the test data and use it to test the program.
"""

def next_date(day,month,year):
    flag = False
    day = day + 1
    if year%4 == 0:
        if year % 100:
            if year%400 == 0:
                flag =  True
            else:
                flag = False
        else :
            flag = True
    else : 
        flag = False
    if month in [1,3,5,7,9,11]:        
        if day >31:
            day = 1
            month = month + 1
    elif month in [4,6,8,10,12]:
        if day >30:
            day = 1
            month = month + 1
    elif month == 2 :
        if flag == True :
            if day > 29:
                day = 1
                month = month + 1
        else :
            if day >28 :
                day = 1
                month = month + 1
    if month > 12:
        month = 1
        year = year + 1
    print(day,"-",month,"-",year)
next_date(1,9,2015)
