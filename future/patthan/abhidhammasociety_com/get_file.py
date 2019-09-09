#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm

data = open('raw_html.txt').read()

soup = BeautifulSoup(data, 'html.parser')

count = 1 
for f in soup.find_all('a', attrs={'class':'a-mjp'}):
    #http://www.abhidhammasociety.com/DhammaLibrary/Audio/MaharPatthanaRecitation_Azusa/096_Book5_Pg142(20)-164(11).mp3
    #print("http://www.abhidhammasociety.com/DhammaLibrary/Audio/MaharPatthanaRecitation_Azusa/"+f.get_text()+".mp3")
    link = "http://www.abhidhammasociety.com/DhammaLibrary/Audio/MaharPatthanaRecitation_Azusa/"+f.get_text()+".mp3"
    
    cc = '{:03d}.mp3'.format(count)
    #print('{}|{}|{}'.format(cc, link, f.get_text() ))
    print('{}|{}|{}'.format(cc, link, ' '.join(f.get_text().split('_')[1:]) ))
    #print(' '.join(f.get_text().split('_')[1:]))
    count += 1 
