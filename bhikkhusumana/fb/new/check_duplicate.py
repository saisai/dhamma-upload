#!/usr/bin/env python
# coding=utf-8


from collections import Counter

urls = [f.strip('\n') for f in open('bb.txt')]

#print(urls)

for key, val in Counter(urls).items():
    if val > 1:
        print(key, val)
