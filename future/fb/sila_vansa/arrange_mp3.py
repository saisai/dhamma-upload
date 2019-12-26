#!/usr/bin/env python
# coding=utf-8
import re
import glob
from shutil import copy
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

mp3s = glob.glob("*.mp3")


count = 1
for f in sorted(mp3s, key=natural_keys):
    fmt = '{:03d}.mp3'.format(count)
    print(f)
    print(fmt)
    dest = 'edit/{}'.format(fmt)
    print(dest)
    copy(f, dest)
    count += 1
