import PyPDF2
dictionaryFile = open('dictionary.txt', 'r')

pdfFileObj = open('pdfs/encrypted_meetingminutes2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for line in dictionaryFile.readlines():
    passUpper = line.upper().strip()
    passLower = line.lower().strip()
    if (pdfReader.decrypt(passUpper) == 1 or
            pdfReader.decrypt(passLower) == 1):
        print('The password was:'+line)
        break

dictionaryFile.close()
pdfFileObj.close()
