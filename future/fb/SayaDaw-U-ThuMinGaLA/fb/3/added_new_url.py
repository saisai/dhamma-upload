#!/usr/bin/env python
# coding=utf-8

from collections import Counter

urls = [f.strip('\n') for f in open('raw_urls.txt')]
#urls = [f.strip('\n') for f in open('raw_url.txt')]

#print(urls)

#print(Counter(urls).items())
for key, val in Counter(urls).items():
    if val > 1:
        print(key, val)
