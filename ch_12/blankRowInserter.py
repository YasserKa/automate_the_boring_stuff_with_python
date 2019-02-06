import sys
import openpyxl

N = int(sys.argv[1])
M = int(sys.argv[2])
fileName = sys.argv[3]

wb = openpyxl.load_workbook(fileName)
sheet = wb.get_active_sheet()
sheet.insert_rows(idx=N, amount=M)
wb.save(fileName)
