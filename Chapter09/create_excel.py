from openpyxl import Workbook

book_obj = Workbook()

excel_sheet = book_obj.active
excel_sheet['A1'] = 'Name'
excel_sheet['A2'] = 'student'
excel_sheet['B1'] = 'age'
excel_sheet['B2'] = '24'

book_obj.save("test.xlsx")
print("Excel created successfully")

