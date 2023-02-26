# starlet-certificate

use this repo to generate certificates  and send the certificate to 
corresponding email address using smtp server for [Starlet Hackathon](https://bit.ly/ME-starlet)
condected by Mind Empowered on 24th-25 th February 2023 at Kerala Startup Mission

### The code has tested on Python 3.10.6

1. Begin by installing the dependencies using 

    ```bash
        pip install -r requirements.txt
    ```
2. Create folder named Generate_PDFs Set up [cert-pdf.py](cert-pdf.py) if want certificate for group of data provide link to csv file contains name of the participants or otherwise give custom inputs on createpdf function call on the main method (which is commented)
3. Run cert-pdf.py file
4. Pdf result available Generate_PDFs folder

* Template folder - Stores the certificate templates
* Fonts folder - Stores the font in ttf format


## SEND EMAIL 
1. make sure the pdf are generated successfully
2. fill the email_pwd and sender value in the [send_email_smtp.py](send_email_smtp.py)
3. run the file 