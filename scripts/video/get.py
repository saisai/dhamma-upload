#!/usr/bin/env python
# coding=utf-8

import re
import json

data = [url.replace(" ", "").split('\n') for url in open('videosid.txt') ]
#print(data)

for id in data:
    if id[0] != "":
        url = 'https://www.facebook.com/WinNaingKyawfromYangon/videos/{}/'.format(id[0])
        print(url)
    #print(len(id))

"""
for link in data:
    if 'https://www.facebook.com/ajax/pagelet/generic.php' in link:
        a = json.dumps(link)
        #print(a)
        b = a.split('\\')
        print(b[1])
        #c =
"""
