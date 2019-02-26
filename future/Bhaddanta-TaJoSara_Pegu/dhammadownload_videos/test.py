#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup as bs4

text = open('get_url.txt', 'r').read()

soup = bs4(text, 'html.parser')

count = 1
with open('titles_linkss.txt', 'w') as f:
    
    for key in soup.find_all('a'):
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1

