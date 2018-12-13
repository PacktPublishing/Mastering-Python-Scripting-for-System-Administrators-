import PyPDF2

pdf = open('test.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf)

print("Number of pages in pdf : ", read_pdf.numPages)
pdf.close()

