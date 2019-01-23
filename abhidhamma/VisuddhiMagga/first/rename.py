#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json
import re 

import glob
from pydub.utils import mediainfo
import subprocess
import datetime
import os
import shutil
import functools

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

new_images = 'new_images'

if not os.path.isdir(new_images):
    os.mkdir(new_images)
    
    


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


images = [i for i in glob.glob("*.jpg")]    

count = 1
for i in sorted(images, key=natural_keys):
    counter = '{}/photo-{:03d}.jpg'.format(new_images, count)
    print(i)
    shutil.copy(i, counter)
    count += 1
