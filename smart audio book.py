import pyttsx3
import PyPDF2
book = open ('AG.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print (pages)
friend = pyttsx3.init()
page = pdfReader.getPage(1)
text = page.extractText ()
friend.say (text)
friend.runAndWait()