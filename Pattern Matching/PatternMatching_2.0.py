'''
Version 2.0: here we use regex (regular expressions)
to describe a pattern of text. 

CHARACTER CLASSES for REGEX

\d          stands for digit
\D          stands for anything but digits
\w          stands for letters, numbers and _
\W          stands for anything but w type
\s          stands for spaces, tabs and newlines
\S          stands for anything but s

How to use REGEX:
1.Import the regex module with import re.
2.Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3.Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4.Call the Match object’s group() method to return a string of the actual matched text.

Using pipe '|' you can try to match one of multiple elements.
In case of multiple match, the first found is the one returned.
Can also be used to search multiple words with the same prefix.

The (x)? can be used to mark on "optional text"
The (x)* means "match 0 or more"
The (x)+ means "match 1 or more"

regex is greedy by default so it will look for the longest match possible;
to use the non-greedy version u need to put a ? next to the last curly bracket.

findall() is like search but will return a list of strings of all the match, not just the 1st one.

The '.' is a wildcard character, it works as every char, like the '?' in web searches
(.* goes straight into greedy mode)

The re.compile() function can hold multiple arguments
re.compile(r'x', re.IGNORECASE) or re.I to match case-insensitive chars

The Regex.sub() method for objects is passed two arguments. 
The first argument is a string to replace any matches. 
The second is the string for the regular expression.

'''

import re 
#object creator (the r is used to pass the string as raw (no escape chars))
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#MO stands for Match Objects
mo = phoneNumRegex.search('My number is 354-289-3492.')
print('Phone number found: ' + mo.group())

#Pattern can even be filtered with parentheses. dividing the match in groups
numRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = numRegex.search('My number is 354-289-3492.')
print('Prefix is '+mo.group(1))
print('Suffix is '+mo.group(2))

#Pass 0 or nothing to print the whole match
print('Whole number is '+mo.group(0))

#Otherwise, using GROUPS you get the array of group results.
pref, suff = mo.groups()
print (pref)
print (suff)

#This will return Batman
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()

#This will return Tina Fey
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()

#Example on how to use the "same prefix" type of code:
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

#Example of Optional Matching: here will go for Batman
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

#Example of Optional Matching: here will go for Batwoman
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

#Example of non-greedy regex function
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

#Example of findall() function: will return ['415-555-9999', '212-555-0000']
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#Will return [('415', '555', '1122'), ('212', '555', '0000')]
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#Will return ['cat', 'hat', 'sat', 'lat', 'mat']
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

#Case-insensitive example: will return 'RoboCop'
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

#sub() method: Will return 'CENSORED gave the secret documents to CENSORED.
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')




