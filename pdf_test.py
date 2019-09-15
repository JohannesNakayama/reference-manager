import PyPDF2
import os

path = os.path.join('files', 'batagelj.pdf')

with open(path, 'rb') as pdf_file:
    pdfReader = PyPDF2.PdfFileReader((pdf_file))
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())
    print(pageObj.getContents())
    print(pdfReader.documentInfo)
    print(pdfReader.getFields())
    print(pdfReader.outlines)

    xmpmd = pdfReader.getXmpMetadata()
    print(xmpmd.custom_properties)

print('test is finished')
