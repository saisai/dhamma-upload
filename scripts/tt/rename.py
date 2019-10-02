#!/usr/bin/env python
# coding=utf-8

import glob
import os
import re 

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


if not os.path.exists('edit'):
    os.mkdir('edit')
    
if not os.path.exists('original'):
    os.mkdir('original')    

mp3s = [f for f in glob.glob('*.mp3')]

count = 1
for mp3 in sorted(mp3s, key=natural_keys):
    fmt = '{:03d}.mp3'.format(count)
    print(mp3, fmt)
    os.system('cp {} original/{}'.format(mp3, mp3))
    ff = 'edit/{}'.format(fmt)
    os.rename(mp3, ff)
    count += 1
    


