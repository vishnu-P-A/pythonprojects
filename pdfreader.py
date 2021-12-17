# importing required modules
import PyPDF2
import sys


def readPDF(file_name):
    # creating a pdf file object
    pdfFileObj = open(file_name, "rb")

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()


if __name__ == "__main__":
    readPDF(sys.argv[1])
