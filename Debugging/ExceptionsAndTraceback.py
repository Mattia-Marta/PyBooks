'''
"Writing code accounts for 90 percent of programming. 
Debugging code accounts for theother 90 percent."
Exception is like "stop doing this and go to the exception statement"

------------------------TRACEBACK------------------------

Exceptions are raised with "raise" statement, done like follow:
• The raise keyword
• A call to the Exception() function
• A string with a helpful error message passed to the Exception() function

Getting the output of an error while still handling it, is possible using traceback module.
Using traceback.format_exc() you get the traceback error as a string.
This could be useful to output everything to a txt file

------------------------ASSERTION------------------------

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong
Assert statement consists of the following:
• The assert keyword
• A condition (that is, an expression that evaluates to True or False)
• A comma
• A string to display when the condition is False

Running code with -0 param, will deactivate all the asserts.

------------------------LOGGING------------------------
STOP USING PRINT() TO DEBUG. 


'''

#Raise exception example
raise Exception('This is the error message that will appear.')

#handling traceback writing the result to errorInfo.txt
import traceback
try:
    raise Exception('OMG! An error occurred!')
except:
    errorfile = open('errorInfo.txt', 'w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('traceback was written into errorInfo.txt')
    
#Assert example
crilin = 'dead'
assert crilin == 'dead', 'Sorry, he cannot be alive, kill him' #This will pass
crilin = 'alive'
assert crilin == 'dead', 'Sorry, he cannot be alive, kill him' #This will ret AssertionErr

#Assert as a check with Traffic Light Simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] == 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] == 'red'
        elif stoplight[key] == 'red':
            stoplight[key] == 'green'

switchLights(market_2nd)

assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight) #use to see no red is in the zone

