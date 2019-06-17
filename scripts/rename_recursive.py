#!/usr/bin/env python
# coding=utf-8

import glob
import os
import re 
import fnmatch
import subprocess

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]



matches = []

for root, dirnames, filenames in os.walk("."):    
    for filename in fnmatch.filter(filenames, "*.MP3"):
        if 'edit' not in os.path.join(root, filename):
            print(os.path.join(root, filename))
            matches.append(os.path.join(root, filename))    
        
        
matches2 = []
for root, dirnames, filenames in os.walk("."):
    for filename in fnmatch.filter(filenames, "*.mp3"):
        if 'edit' not in os.path.join(root, filename):
            print(os.path.join(root, filename))
            matches2.append(os.path.join(root, filename))

matches2.extend(matches)            
print(len(matches2))
count = 1
for ff in sorted(matches2, key=natural_keys):
    fmt = '{:03d}.mp3'.format(count)
    
    
    
    command = "rsync|-avzz|-P|{}|edit/{}".format(ff, fmt)
    
    print(command)
    print(ff, fmt)
    
    completed = subprocess.run(command.split('|'))
    #print('returncode:', completed)
    print(completed.returncode)    
    if completed.returncode == 0:        
        print('Complete file {} .....'.format(fmt))  
        print(ff, fmt)
    
    count += 1
    
        


