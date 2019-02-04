# go through a tree
    # delete a file if it has a size of more than 100 MB
    # print them on the screen

import shutil, os, send2trash

dirPath = 'selective_copy_old'
for foldername, subfolders, filenames in os.walk(dirPath):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        if (os.path.getsize(filePath) > 10000000):
            send2trash.send2trash(filePath)
            print('deleting file ' + filePath)
