#!/usr/bin/env python
# coding=utf-8
import os
import sys
import time


dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)

from crawler import (get_fb_title, rearrange_urls, download_fb, get_splited_lines)

#rearrange_urls('raw_urls.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')

#full_path = os.path.realpath(__file__)
#path, filename = os.path.split(full_path)
#os.chdir(path)

#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

#download_fb('44.txt', 1)


#result = os.path.isfile(dir_path+'44.txt')
#print(result)

count = 0
for txt in range(1, 90):
    #count = 0
    #print(count)
    #if count < 5:
    txt_file = '%s%s.txt' % (dir_path, txt)
    file_txt = '%s.txt' % (txt)
    if os.path.isfile(txt_file):
        if count < 5:
            print(txt_file)
            download_fb(file_txt, 1)
            #print(txt_file)
            count += 1
        else:
            break
    #count += 1
    #time.sleep(5)

