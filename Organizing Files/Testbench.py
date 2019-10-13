'''
Using the testbench you'll create files into the "AmericanFolder" to test the script
'''

#! python3

import os, shutil, random, string

#Generate a random string using random lower chars. Number can be modified)
def randomString():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(4,12)))

beginning, ending, file = '', '', ''

abswd = os.path.abspath('.')

#changing cwd into 'AmericanFolder'
os.chdir('.\AmericanFolder')

#TODO generate file name with american date style
for i in range(0,10):
    dd = str(random.randint(1,28))
    mm = str(random.randint(1,12))
    yy = str(random.randint(1915, 2019))

    if (random.randint(1, 10)%2 == 0):
        beginning = randomString()
        americanFile = beginning + mm + '-' + dd + '-' + yy + '.txt'
    else:
        ending = randomString()
        americanFile = mm + '-' + dd + '-' + yy + ending + '.txt'

    #TODO Create the files
    file = open(americanFile, "w")
    file.close()

#End of for cycle
