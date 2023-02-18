# imports

from PyPDF2 import PdfReader, PdfWriter
import io
import os
import glob
import csv
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter, A4


# pdf creation function
def createpdf(name):
    pass


# import our fonts
pdfmetrics.registerFont(TTFont('Roboto', './Fonts/Roboto-Regular.ttf'))
pdfmetrics.registerFont(TTFont('RobotoMono', './Fonts/RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Ember-bold', './Fonts/Amazon-Ember-Medium.ttf'))
packet = io.BytesIO()

# pdf creation function
def createpdf(name):
    packet = io.BytesIO()

    # line start and end x position - change this according to certificate
    start = 130
    end = 680

    full_name = name.upper()

    # define certificate size - change this also
    cert_page_size = ((2000,1414))
    can = canvas.Canvas(packet,pagesize=cert_page_size)

    # set printing font
    can.setFont('Ember-bold',26)

    # define starting position of string
    x_pos = start+ abs((end-start)/2 - len(full_name))
    print("full name : ",full_name)

    # change x value from file also y according to file
    can.drawString(x_pos - ((len(full_name)/2)*12), 320, full_name)
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # get the template - change the file name here
    template_pdf = PdfReader(open("./Template/certificatesample.pdf","rb"))

    output = PdfWriter()

    # add the string to pdf
    page = template_pdf.pages[0]
    page2 = new_pdf.pages[0]
    page.merge_page(page2)
    output.add_page(page)

    # finally, write "output" to a real file
    outputStream = open(f"./Generate_PDFs/{full_name}.pdf","wb")
    output.write(outputStream)
    outputStream.close()


# main function
if __name__ == "__main__":
    # remove already generated files if any
    files = glob.glob('./Generate_PDFs/*')
    for f in files:
        os.remove(f)

    # for generating one file
    createpdf("NAME GOES HERE")

    # for generating file from csv - replace link to csv file
    # with open('link to csv', 'r') as readFile:
    #     reader = csv.reader(readFile)
    #     l = 0
    #     for i, row in enumerate(reader):
    #         print("###############Processing", i, "################")
    #         if l != 0:
    #             name = row[0]
    #
    #             if name:
    #                 createpdf(name)
    #         l = l + 1
