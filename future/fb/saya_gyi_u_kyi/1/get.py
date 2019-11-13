#!/usr/bin/env python
# coding=utf-8

not_included = [f.strip('\n') for f in open('not_included.txt')]
links = [f.strip('\n') for f in open('links.txt')]

for link in links:
    if link not in not_included:
        print(link)
