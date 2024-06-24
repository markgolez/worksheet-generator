# import PyPDF2
# import os

# # Open the files that have to be merged one by one
# pdf1File = open('K:/python/myapp/merged/Quiz1.pdf', 'rb')
# pdf2File = open('K:/python/myapp/merged/quiz.pdf', 'rb')

# # Read the files that you have opened
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# # Create a new PdfFileWriter object which represents a blank PDF document
# pdfWriter = PyPDF2.PdfFileWriter()

# # Loop through all the pagenumbers for the first document
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# # Loop through all the pagenumbers for the second document
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# # Now that you have copied all the pages in both the documents, write them into the a new document
# pdfOutputFile = open(
#     'K:/python/myapp/merged/mergedFiles/MergedFiles.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)

# # Close all the files - Created as well as opened
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()
# print('ok')


import PyPDF2
import sys
import os

files = os.listdir('merged/Quiz/')
inputs = ['K:/python/myapp/merged/Quiz/' +
          x for x in files if 'anskey' not in x]
part2 = 'merged/quiz3p2.pdf'
# inputs = sys.argv[1:] # From input (without spaces!)
# inputs = ['K:/python/myapp/merged/Quiz2/Quiz1 - #1.pdf',
#           'K:/python/myapp/merged/quiz.pdf']  # Add those pdf's to your project
# print(inputs)


def pdf_combine(pdf_list):

    for idx, pdf in enumerate(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        merger.append(pdf)
        merger.append(part2)

        path = 'K:/python/myapp/merged/mergedFiles/' + str(idx) + '.pdf'
        merger.write(path)


pdf_combine(inputs)
 