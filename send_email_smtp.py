# this file is associated with cert-pdf.py . Make sure you generated pdf files first
from email.message import EmailMessage
import ssl
import smtplib
import csv 

email_pwd = "fill gmail 16 character password for app passwords"
sender = 'fill sender gmail address'

# function for ending the 
def send_mail(name,recevier):

    subject = "certification of participation"
    body = f'''
        Hey {name},
        fill the contents of email
        Thank you
    '''

    # initialize email message
    em = EmailMessage()

    em['From']=sender
    em['To']=recevier
    em['Subject']=subject
    em.set_content(body)

   
    # capitalize the name to find the pdf file
    full_name=name.upper()

    #attach the pdf file dynamically
    with open(f"./Generate_PDFs/{full_name}.pdf",'rb') as content_file:
        content = content_file.read()
        em.add_attachment(content,maintype='application',subtype='pdf',filename='certificate.pdf')

    # load the ssl default context
    context = ssl.create_default_context()

    # send mail by smtp gmail server with port 465
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        # login to gmail
        smtp.login(sender,email_pwd)
        # send the mail
        smtp.sendmail(sender,recevier,em.as_string())


# main function
if __name__ == "__main__":
    # open the csv list which contains name and email address
    with open('./list.csv', 'r') as readFile:
        # start reading the file
        reader = csv.reader(readFile)
        l = 1
        for i, row in enumerate(reader):
            print("###############Sending Mail ", i, "################")
            if l != 0:
                # select name from the csv
                name = row[1]
                # select email from the csv
                email_address=row[2]
                if name:
                   send_mail(name,email_address)
            l = l + 1