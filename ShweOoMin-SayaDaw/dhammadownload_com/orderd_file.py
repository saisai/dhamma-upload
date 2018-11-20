import glob
import re
import os

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text) ]

count = 438
for mp3 in sorted(glob.glob('*.mp3'), key=natural_keys):
    dest = 'edit/'+ '{:03d}.mp3'.format(count)
    print(dest)
    os.rename(mp3, dest)
    count += 1
