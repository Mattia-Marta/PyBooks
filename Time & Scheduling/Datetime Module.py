'''
The datetime module is used to do math with dates and display them in a more
convenient format. 

Calling datetime.datetime.now() returns a datetime object formatted as computer's clock
Using datetime.datetime.fromtimestamp() you can convert from epoch to datetime.

There is even a data type named timedelta, representing a duration.
It gets created by datetime.timedelta()

The time.sleep() method lets you pause a program for a certain number of sec-onds. 
By using a while loop, you can pause your programs until a specific date

Using strftime() method you can make datetime obj human readable:

Directive → Meaning
-------------------
    %Y    →    Year with century, as in '2014'
    %y    →    Year without century, '00' to '99' (1970 to 2069)
    %m    →    Month as a decimal number, '01' to '12'
    %B    →    Full month name, as in 'November'
    %b    →    Abbreviated month name, as in 'Nov'
    %d    →    Day of the month, '01' to '31'
    %j    →    Day of the year, '001' to '366'
    %w    →    Day of the week, '0' (Sunday) to '6' (Saturday)
    %A    →    Full weekday name, as in 'Monday'
    %a    →    Abbreviated weekday name, as in 'Mon'
    %H    →    Hour (24-hour clock), '00' to '23'
    %I    →    Hour (12-hour clock), '01' to '12'
    %M    →    Minute, '00' to '59'
    %S    →    Second, '00' to '59'
    %p    →    'AM' or 'PM'
    %%    →    Literal '%' character

The strptime() does the opposite, from a string, it gets the datetime obj.

'''

#output: '2015/10/21 16:29:00'
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')

#value:datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')