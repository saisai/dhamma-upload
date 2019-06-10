#!/usr/bin/env python
# coding=utf-8
import os
import sys
import time
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)

from crawler import (get_fb_title, rearrange_urls, download_fb, get_splited_lines)

threads = 0
try:
    threads = sys.argv[1]
    
except IndexError as e:
    threads = 1


def get_percent():
    cmd = "df -h | grep media_rw | awk '{print $5}'"
    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode()
    print(output.split('%')[0])
    return int(output.split('%')[0])
    
txt_file = '%s%s.txt' % (dir_path, 'links')
print(txt_file)
if os.path.isfile(txt_file):
    if get_percent() <= 95:
        print(txt_file)
        download_fb('links.txt', int(threads))
        #print(txt_file)
    

'''    
count = 0
for txt in range(0, 90):
    #count = 0
    #print(count)
    #if count < 5:
    txt_file = '%s%s.txt' % (dir_path, txt)
    file_txt = '%s.txt' % (txt)
    if os.path.isfile(txt_file):
        if get_percent() <= 95 and count < 5:
            print(txt_file)
            download_fb(file_txt, int(threads))
            #print(txt_file)
            count += 1
        else:
            break
'''
