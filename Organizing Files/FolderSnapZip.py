#! python3
#FolderSnapZip.py - 
# Copies an entire folder and its contents into a ZIP file whose filename increments

import zipfile, os, shutil, pathlib, sys

def backToZip(folder):
    folder = os.path.abspath(folder)
    parent = pathlib.Path(folder).parent
    os.chdir(parent)
    #Choose the actual number to use, will return the 1st free number
    num = 1
    while True:
        zipName = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipName):
            break
        num = num + 1    

    #TODO Create the zip file
    print('Creating %s...' % (zipName))
    backupZip = zipfile.ZipFile(zipName, 'w')

    #TODO Walk folder and compress every file
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        #Add all files in thw folder to the ZIP
        for file in filenames:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, file))
    backupZip.close()

    print('Uber Done!')

if len(sys.argv)<2:
    print('Invalid input')
    inputPath = input('Please, insert the quoted path: ')
    if not os.path.exists(inputPath):
        print('Invalid input\nExiting the program.')
        exit()
    else:
        backToZip(inputPath)

if sys.argv[1] == '-h':
    print('To make a zip of your file call FolderSnapZip.py with the quoted path of the folder you want to zip')
    exit()

if os.path.exists(sys.argv[1]):
    backToZip(sys.argv[1])
