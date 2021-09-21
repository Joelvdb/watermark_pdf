import PyPDF2

pdf_file = "sample.pdf"
watermark = "watermark.pdf"
merged_file = "merged.pdf"

input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

output = PyPDF2.PdfFileWriter()

for page in range(input_pdf.getNumPages()):
    pdf_page = input_pdf.getPage(page)
    watermark_page = watermark_pdf.getPage(0)
    pdf_page.mergePage(watermark_page)
    output.addPage(pdf_page)

merged_file = open(merged_file,'wb')
output.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()
