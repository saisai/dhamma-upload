#!/usr/bin/env python
# coding=utf-8

import re
from bs4 import BeautifulSoup


html = open('raw_html.txt').read()


soup = BeautifulSoup(html, 'html.parser')

#536517523346879/videos

p = re.compile(r'536517523346879/videos/[0-9]+')

for f in soup.findAll('a'):
    try:
        if '536517523346879/videos/' in f.get('href'):
            if p.search(f.get('href')) != "":
                if 'https://www.facebook.com' not in f.get('href'):
                    #print(f.get('href').split('/')[:4])
                    print('https://www.facebook.com'+'/'.join(f.get('href').split('/')[:4]))
    except TypeError:
        pass
