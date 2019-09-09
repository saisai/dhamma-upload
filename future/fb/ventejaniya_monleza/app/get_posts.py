#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup

data = open('html.txt').read()

soup = BeautifulSoup(data, 'html.parser')

for f in soup.find_all('a'):
    try:
        if 'posts' in f.get('href'):
            if f.get('href').count('/') == 3:
                print('https://www.facebook.com' + f.get('href'))
    except TypeError as e:
        pass

