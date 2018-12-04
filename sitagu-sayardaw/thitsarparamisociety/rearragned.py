#!/usr/bin/env python
# coding=utf-8


files = [f.strip('\n') for f in open('_titles_links.txt', 'r') if len(f) > 2]

with open('titles_links.txt', 'w') as f:
    count = 1
    for key in files:
        counter = '{:03d}'.format(count)
        f.write('{}.mp3|{}|{}\n'.format(counter, key.split('|')[1], key.split('|')[2]))
        #f.write('{}\n'.format(key.get_text()))
        count += 1
