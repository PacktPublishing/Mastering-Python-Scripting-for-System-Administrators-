import xlrd 

excel_file = ("/home/student/sample.xlsx") 

book_obj = xlrd.open_workbook(excel_file) 
excel_sheet = book_obj.sheet_by_index(0) 

result = excel_sheet.cell_value(0, 1) 
print(result)
