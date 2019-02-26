#!/usr/bin/env python
# coding=utf-8

import subprocess
import os

file_read = "2.txt"
files = [f.strip('\n') for f in open(file_read, 'r')]


for f in files:
    if not os.path.isdir(f.split('|')[0]):
        #os.system('%s %s -u -td 1' % ('python', result))
        dir = f.split('|')[0]
        os.system('%s %s' % ('mkdir', dir))
        #print(f.split('|')[0])
    
    
    dir = f.split('|')[0]
    link = f.split('|')[2]
    
    os.system('%s %s %s' % ('cp', 'browser.py', dir,))
    os.system('%s %s %s' % ('cp', 'aa.py', dir,))
    
    #os.system('%s %s %s %s %s "%s"' % ('cd', dir, '; wget', '-O', 'a.pdf', link))
    #os.system('%s %s %s %s %s "%s"' % ('cd', dir, '; curl', '-o', 'a.pdf', link))
    
    
    
    os.system('%s %s %s %s "%s"' % ('cd', dir, '; python3', 'browser.py', link, ))
    os.system('%s %s %s %s ' % ('cd', dir, '; python3', 'aa.py',))
    
    #os.system('%s %s' % ('mkdir', 'pages'))
    
    #data = """mkdir images; for i in `ls -v *.pdf`; do c=`basename $i .pdf`; echo $i; convert -geometry 1000x1000 -density 200x200 -quality 100 $i images/$c.jpg; done"""
    data = """
           rm -rfv images
           mkdir images
           for i in `ls -v *.pdf`; do c=`basename $i .pdf`; echo $i; convert -geometry 1000x1000 -density 200x200 -quality 100 $i images/$c.jpg; done
           """
    
    os.system('%s %s %s %s %s' % ('cd', dir, '; cd', 'pages;', data))
    #os.system('%s %s %s %s %s %s %s' % ('cd', dir, '; cd', 'pages;', 'printf', data, '> run.sh'))
    
    #os.system('%s %s %s %s' % ('wget', '-O', 'a.pdf', link))
    
    os.system('%s %s' % ('cd', '..'))
    
'''
wget -O a.pdf "http://dhammadownload.com/File-Library/Sadhammaransi-Sayadaw-Gyi/Saddhammaramsi-SayaDaw-KhitLuNgeMyarThiKaungSayar.pdf"
#wget -O a.pdf ""
python3 aa.py
cd pages;
rm -rfv images; mkdir images; for i in `ls -v *.pdf`; do c=`basename $i .pdf`; echo $i; convert -geometry 1000x1000 -density 200x200 -quality 100 $i images/$c.jpg; done
'''
        
        
