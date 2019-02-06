import os
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

dirPath = 'text_files'
filesList = os.listdir(dirPath)
for i in range(len(filesList)):
    fileName = filesList[i]
    fileStream = open(os.path.join(dirPath, fileName), 'r')
    lines = fileStream.readlines()
    for j in range(len(lines)):
        line = lines[j]
        print(line, i, j)
        sheet.cell(row=j+1, column=i+1, value=line.strip())

wb.save('text_files.xlsx')
