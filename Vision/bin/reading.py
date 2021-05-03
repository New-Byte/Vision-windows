import pyttsx3
import PyPDF2
from search_any import search_any_file
import sys

def read(filename, pageno):
    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print (pages)
    page = pdfReader.getPage(pageno)
    text = page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

filename = sys.argv[1]
pageno = sys.argv[2]

filename = search_any_file(filename)
read(filename[0], int(pageno)-1)