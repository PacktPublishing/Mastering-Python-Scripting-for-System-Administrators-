import PyPDF2
 
pdf = open('test.pdf', 'rb')
rd_pdf = PyPDF2.PdfFileReader(pdf)
wr_pdf = PyPDF2.PdfFileWriter()
 
for pg_num in range(rd_pdf.numPages):
	pdf_page = rd_pdf.getPage(pg_num)
	pdf_page.rotateClockwise(90)
	wr_pdf.addPage(pdf_page)
 
pdf_out = open('rotated.pdf', 'wb')
wr_pdf.write(pdf_out)
pdf_out.close()
print("pdf successfully rotated")
pdf.close()

