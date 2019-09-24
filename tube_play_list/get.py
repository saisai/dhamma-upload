#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup

from common import read_file

data = read_file("raw_html.txt")

soup = BeautifulSoup(data, 'html.parser')

with open('playlists.txt', 'a') as wf:
    for f in soup.find_all('a', attrs={'id': 'video-title'}):
        wf.write(f.get_text())
        wf.write('\n')

