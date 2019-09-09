#!/usr/bin/env python
# coding=utf-8
import os
import subprocess
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

        #output_filename = 'pages/{}_page_{}.pdf'.format(
        #    fname, page+1)
        
        output_filename = 'pages/photo-{:03d}.pdf'.format(
            page+1)        

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    path = 'a.pdf'    

    result = subprocess.check_output('pdfinfo a.pdf | grep Encrypted', shell=True)
    print(result)
    if b'yes' in result:
        os.system('gs -o repaired.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress a.pdf')
        #subprocess.check_output('gs -o repaired.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress a.pdf', shell=True)
        os.rename('a.pdf', 'corrupted.pdf')
        os.rename('repaired.pdf', 'a.pdf')
        
        
    pdf_splitter(path)
    
    '''
    https://superuser.com/questions/580887/check-if-pdf-files-are-corrupted-using-command-line-on-linux
    sudo apt install ghostscript
    sudo apt install poppler-utils
    
    pdfinfo a.pdf
    
    Creator:        Adobe Acrobat 8.0
    Producer:       Adobe Acrobat 8.0 Image Conversion Plug-in
    CreationDate:   Sat Aug 29 15:02:18 2009 +07
    ModDate:        Mon Aug 31 15:08:17 2009 +07
    Tagged:         no
    UserProperties: no
    Suspects:       no
    Form:           none
    JavaScript:     no
    Pages:          151
    Encrypted:      yes (print:yes copy:no change:no addNotes:no algorithm:RC4)
    Page size:      230.4 x 324 pts
    Page rot:       0
    File size:      168957004 bytes
    Optimized:      yes
    PDF version:    1.6
    
    if Encrypted: yes means
    PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]
    To fix this warning
    uisng 
    gs \
    -o repaired.pdf \
    -sDEVICE=pdfwrite \
    -dPDFSETTINGS=/prepress \
    corrupted.pdf
    https://superuser.com/questions/278562/how-can-i-fix-repair-a-corrupted-pdf-file
    
    Note: If this warning occurs
    PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]
    PdfFileReader can not read anymore.
    
    pdfinfo a.pdf
    
    Producer:       Epson Scan 2
    CreationDate:   Sat Aug 11 15:48:14 2018 +07
    ModDate:        Sun Aug 12 18:54:45 2018 +07
    Tagged:         no
    UserProperties: no
    Suspects:       no
    Form:           none
    JavaScript:     no
    Pages:          140
    Encrypted:      no
    Page size:      310.08 x 453.12 pts
    Page rot:       0
    File size:      48603847 bytes
    Optimized:      no
    PDF version:    1.4    
    
    if Encrypted: no means
    no user waning from PyPDF2
    
    '''
