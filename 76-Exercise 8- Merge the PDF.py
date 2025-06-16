# wap to manipulate pdf files using pypdf, your program should be able to merge multiple pdf files to a single pdf. 
# pypdf is a free and open source pure python pdf librery capable of splitting, merging,cropping...

from PyPDF2 import PdfWriter
import os

merger= PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write ("merged-pdf.pdf")
merger.close()