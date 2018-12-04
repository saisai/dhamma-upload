#!/usr/bin/env python
# coding=utf-8

files = [f.strip('\n') for f in open('_titles_links.txt', 'r') if len(f) > 2]

count = 1035
for f in files:
    
    print('{:03d}.mp4|{}|{}'.format(count, f.split('|')[1], f.split('|')[2]))
    
    count += 1 
