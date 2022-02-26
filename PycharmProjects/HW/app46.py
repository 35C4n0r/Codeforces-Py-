import openpyxl as xl
xl.load_workbook('trnsaction.xlsx')
sheet = wb['Sheet1']
sheet['a1']
sheet.cell(1, 1)
print(cell.value)
