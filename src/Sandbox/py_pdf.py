"""
Created on Dec 6, 2015

Taken from this answer:
https://stackoverflow.com/a/34116472/1469465

@author: physicalattraction
"""

import PyPDF2
import os.path

from PIL import Image

from utils import pdf_dir

if __name__ == '__main__':
    file = os.path.join(pdf_dir(), 'wind_energy.pdf')
    with open(file, 'rb') as f:
        input1 = PyPDF2.PdfFileReader(f)
        page0 = input1.getPage(0)
        xObject = page0['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = 'RGB'
                else:
                    mode = 'P'

                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    img.save(obj[1:] + '.png')
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    img = open(obj[1:] + '.jpg', 'wb')
                    img.write(data)
                    img.close()
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img = open(obj[1:] + '.jp2', 'wb')
                    img.write(data)
                    img.close()
