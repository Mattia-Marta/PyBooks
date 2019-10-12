#! python3

import os, shutil, random, string

def randomString():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(4,12)))

beginning, ending, file = '', '', ''

abswd = os.path.abspath('.')

#americanFolder = os.path.join(abswd, 'AmericanFolder')
os.chdir('./Organizing Files/AmericanFolder')

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
