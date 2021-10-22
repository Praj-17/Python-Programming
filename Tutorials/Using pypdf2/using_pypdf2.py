import PyPDF2
a = PyPDF2.PdfFileReader('CNotesForProfessionals.pdf')
# print(a.documentInfo)
print(a.getNumPages())