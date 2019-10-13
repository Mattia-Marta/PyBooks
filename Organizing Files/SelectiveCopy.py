#!python3
#selectiveCopy.py-
#Copy all the file with a defined extension into a folder named as the extension.

import os, sys, shutil

def selectiveCopy(folder, extension):
    folder = os.path.abspath(sys.argv[1])
    dest = os.path.join(folder, extension)
    if not os.path.exists(dest):
        os.mkdir(dest, mode=0o777)
    for foldername, subfolder, filename in os.walk(folder):
        print('Looking into %s' % (foldername))
        for file in filename:
            if file.endswith('.' + extension):
                print('Moving %s to destination folder...' % (file))
                print(os.path.join(folder, foldername))
                print(dest)
                shutil.copy(os.path.join(folder, foldername, file), dest)
    print('DONE!')
    
    
if os.path.exists(os.path.abspath(sys.argv[1])):
    selectiveCopy(sys.argv[1], sys.argv[2])