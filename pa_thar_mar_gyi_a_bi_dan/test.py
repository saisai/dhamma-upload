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

files = glob.glob('*.MP3')

count = 2
for f in sorted(files, key=natural_keys):
    tt = '{:03d}.mp3'.format(count)
    dest = 'edit/{}'.format(tt)
    print(tt)
    print(dest)
    print(f)
    copy(f, dest)
    count += 1

