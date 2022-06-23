from PyPDF2 import PdfReader

def fae_extract(filename):
    reader = PdfReader(filename)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)

if __name__ == "__main__":
    filename = "ReportSupervisionProteccion-2022635527.pdf"
    fae_extract(filename)
