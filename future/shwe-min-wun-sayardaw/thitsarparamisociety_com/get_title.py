#!/usr/bin/env python
# coding=utf-8


titles = [f.strip('\n') for f in open('description.txt', 'r') if len(f) > 1]


with open('title.txt', 'w') as f:
    for title in titles:
        # print(title.split('|')[0])
        f.write('%s\n' % (title.split('|')[0], ))
