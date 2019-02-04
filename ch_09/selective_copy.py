import shutil, os

oldDir = 'selective_copy_old'
newDir = 'selective_copy_new'

if (not os.path.exists(newDir)):
    os.mkdir(newDir)
for foldername, subfolders, filenames in os.walk(oldDir):
    for filename in filenames:
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            newParentFolder = foldername.replace(oldDir, newDir)

            if (not os.path.exists(newParentFolder)):
                os.makedirs(newParentFolder)
            oldFilePath = os.path.join(foldername, filename)
            newFilePath = os.path.join(newParentFolder, filename)

            print('copying ' + oldFilePath + ' to ' + newFilePath + '...')
            shutil.copy(oldFilePath, newFilePath)
