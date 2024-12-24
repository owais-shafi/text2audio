import pyttsx3
import pdfplumber

# Initialize pyttsx3 engine
speaker = pyttsx3.init()
# Default rate is 200, lower makes it more human-like
speaker.setProperty('rate', 170)
# Open PDF with pdfplumber
with pdfplumber.open('oop.pdf') as book:
    pages = len(book.pages)
    # Reading from page 4
    for num in range(4, pages):
        page = book.pages[num]
        text = page.extract_text()

        if text:
            speaker.say(text)
            speaker.runAndWait()
        else:
            print("No text found on page")

