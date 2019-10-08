#!/usr/bin/env python
# coding=utf-8
import re
import glob
from shutil import copy 
# copyfile(src, dst)




def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

#files = glob.glob('*.MP3')
#files = [f.strip('\n') for f in open('fb_down_finished.txt')]
files = [f.strip('\n') for f in open('title.txt')]

count = 1
#for f in sorted(files, key=natural_keys, reverse=True):
for f in sorted(files, key=natural_keys):
    #tt = '{:03d}.mp3'.format(count)
    #dest = 'edit/{}'.format(tt)
    #print(tt)
    #print(dest)
    print(f.split('|')[2])
    #print(f.split('|')[1:])
    #print('|'.join(f.split('|')[1:]))
    #copy(f, dest)
    count += 1

