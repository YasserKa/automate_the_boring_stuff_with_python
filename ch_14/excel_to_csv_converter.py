# read all excel files in a aworking directory
# convert them to csv
# for each sheet make a csv
# format is exccel_name_sheet_title.csv

import os
import csv
import openpyxl

excelSheetsDir = 'spreadSheets'

# go through the excel files
for excelFile in os.listdir(excelSheetsDir):
    wb = openpyxl.load_workbook(os.path.join(excelSheetsDir, excelFile))
    # go through the sheets
    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)
        csvDirectory = os.path.join('cvss',
                                    excelFile + '_' + sheetName + '.csv')
        csvFile = open(csvDirectory, 'w')
        csvWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        for row in sheet.rows:
            rowValue = list(map(lambda x: x.value, row))
            csvWriter.writerow(rowValue)
        print('done converting excelFile ' + excelFile + ' sheet ' + sheetName)
        csvFile.close()
