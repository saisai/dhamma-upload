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
files = [f.strip('\n') for f in open('fb_down_finished.txt')]

count = 1
for f in sorted(files, key=natural_keys, reverse=True):
    #tt = '{:03d}.mp3'.format(count)
    #dest = 'edit/{}'.format(tt)
    #print(tt)
    #print(dest)
    print(f.split('|')[1])
    #copy(f, dest)
    count += 1

