import PyPDF2

pdf = open('test.pdf', 'rb') 
read_pdf = PyPDF2.PdfFileReader(pdf) 
pdf_page = read_pdf.getPage(1)
pdf_content = pdf_page.extractText()
print(pdf_content)
pdf.close()

