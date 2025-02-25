import pdfplumber
import pandas as pd

with pdfplumber.open("apreports.pdf") as pdf:
    page = pdf.pages[15]
    text = page.extract_text()
print(text)
