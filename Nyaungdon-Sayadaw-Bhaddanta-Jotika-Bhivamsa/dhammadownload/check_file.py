#!/usr/bin/env python
# coding=utf-8


import requests


urls = [url.split('|')[1] for url in open('titles_links.txt')]

for url in urls:
    rr = requests.get(url)
     
    if rr.status_code == 404:
        print(url)
    
    