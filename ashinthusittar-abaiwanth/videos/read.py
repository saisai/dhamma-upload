#!/usr/bin/env python
# coding=utf-8

results = [f.strip('\n') for f in open('raw_titles_links_edited.txt')]
cc = 1
for ff in results:
    #print(ff.split('|'))
    fmt = '{:03d}.mp3'.format(cc)
    print('{}|{}|{}'.format(fmt, ff.split('|')[1], ff.split('|')[2]))
    cc += 1
