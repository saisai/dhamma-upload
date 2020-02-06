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
files = [f.strip('\n') for f in open('results.txt', encoding='utf-8')]

#count = 1
#for f in sorted(files, key=natural_keys, reverse=True):
for f in sorted(files, key=natural_keys):
    #tt = '{:03d}.mp3'.format(count)
    #dest = 'edit/{}'.format(tt)
    #print(tt)
    #print(dest)
    print('{}|{}|{}'.format(f.split('|')[1],f.split('|')[2],f.split('|')[3]))
    #print(f.split('|')[1:])
    #print('|'.join(f.split('|')[1:]))
    #copy(f, dest)
    #count += 1

