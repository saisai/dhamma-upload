#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as bs4
import requests


data = requests.get('http://dhammalann.org/books/myanmarbooks.html?start=0')

soup = bs4(data.text, 'html.parser')

for result in soup.find_all('a'):
    try:
        if '.pdf' in result.get('href'):
            print(result.get('href'))
    except TypeError as e:
        print(e)
