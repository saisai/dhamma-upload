#!/usr/bin/env python
# coding=utf-8

import re
from bs4 import BeautifulSoup


#html = open('raw_url.txt').read()


        
def get_result(line):
    

    soup = BeautifulSoup(line, 'html.parser')
    #print(soup)
    #536517523346879/videos

    p = re.compile(r'/AshintayzawbarthaMYK/videos/[0-9]+')

    for f in soup.find_all('a'):
        #print(f)
        
        try:
            if '/AshintayzawbarthaMYK/videos/' in f.get('href'):
                if p.search(f.get('href')) != "":
                    if 'https://www.facebook.com' not in f.get('href'):
                        #print(f)
                        #print(f.get('href').split('/')[:4])
                        print('https://www.facebook.com'+'/'.join(f.get('href').split('/')[:4]))
        except TypeError:
            pass

count = 1            
with open('raw_url.txt') as f:
    for ff in f:
        #print(ff)
        #if count == 500:            
        #    break
        #print(count)
        if not ff:
            
            break
        get_result(ff)
        count += 1