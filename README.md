# starlet-certificate

use this repo to generate certificates for [Starlet](https://bit.ly/ME-starlet)

### The code has tested on Python 3.10.6

1. Begin by installing the dependencies using 

    ```bash
        pip install -r requirements.txt
    ```
2. Set up [cert-pdf.py](cert-pdf.py) if want certificate for group of data provide link to csv file contains name of the participants or otherwise give custom inputs on createpdf function call on the main method (which is commented)
3. Run cert-pdf.py file
4. Pdf result available Generate_PDFs folder

* Template folder - Stores the certificate templates
* Fonts folder - Stores the font in ttf format