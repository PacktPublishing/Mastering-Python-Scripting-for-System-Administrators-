from openpyxl import Workbook

book_obj = Workbook()
excel_sheet = book_obj.active

rows = (
    (11, 12, 13),
    (21, 22, 23),
    (31, 32, 33),
    (41, 42, 43)
)

for values in rows:
	excel_sheet.append(values)
	print()

print("values are successfully appended")
book_obj.save('test.xlsx')
