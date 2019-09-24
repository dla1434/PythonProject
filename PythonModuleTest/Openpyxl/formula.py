''' 수식 - sum '''
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'

wb.save('writeFormula.xlsx')

sheet['A9'] = 'TOTAL:' 

sheet['B1'] = 82 
sheet['B2'] = 11 
sheet['B3'] = 85 
sheet['B4'] = 18 
sheet['B5'] = 57 
sheet['B6'] = 51 
sheet['B7'] = 38 
sheet['B8'] = 42 
sheet['B9'] = rmsan'=SUM(B1:B8)'

wb.save('SumFormulas.xlsx')