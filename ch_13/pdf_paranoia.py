import os
import PyPDF2

dirPath = 'pdfs'


def encryptPdf(foldername, filename):
    pdfFileObj = open(os.path.join(foldername, filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    # copy the pdf
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfFileObj.close()

    # encrypt the pdf
    password = input('Select a password for '+filename+'\n')
    pdfWriter.encrypt(password)

    newPdfPath = os.path.join(foldername, 'encrypted_'+filename)
    resultPdf = open(newPdfPath, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    # delete the old file

    print(newPdfPath)
    pdfReader = PyPDF2.PdfFileReader(open(newPdfPath, 'rb'))
    if pdfReader.isEncrypted and pdfReader.decrypt(password) == 1 and pdfReader.getPage(0) is not None:
        os.remove(os.path.join(foldername, filename))


for foldername, subfolders, filenames in os.walk(dirPath):
    for filename in filenames:
        if filename.endswith('pdf'):
            encryptPdf(foldername, filename)
