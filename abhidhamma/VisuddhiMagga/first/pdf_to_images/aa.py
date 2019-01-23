#!/usr/bin/env python
# coding=utf-8
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pages = 'pages'

if not os.path.isdir(pages):
    os.mkdir(pages)


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = 'pages/{}_page_{}.pdf'.format(
            fname, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    path = 'a.pdf'
    pdf_splitter(path)
