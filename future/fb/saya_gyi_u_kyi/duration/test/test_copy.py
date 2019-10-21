#!/usr/bin/env python
# coding=utf-8
import os

import os.path
import time

import inspect
from pathlib import Path

cur_dir = os.getcwd() # get current working directory

from crawler import (get_fb_title, rearrange_urls, download_fb,
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,
   get_fb_duration)
'''                    
def _get_input(name):
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / name
'''	

def _get_input(name):
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / name

    
def read_line(name="input.txt"):
    with open(_get_input(name)) as f:
        return next(f).strip("\n")


def read_lines(name="input.txt"):
    with open(_get_input(name)) as f:
        return [l for l in (l.strip("\n") for l in f) if l]
        
def read_lines_yield(name="input.txt"):
    with open(_get_input(name)) as f:
        for l in f:
            yield l
        
        
def read_large_file(file_handler, block_size=10000):
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []

    # don't forget to yield the last block
    if block:
        yield block
        
#def read_in_chunks(file_object, chunk_size=1024):
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        #print('a')
        #print(len(data))
        #print(data)
        yield data     


        
        
        
print(os.getcwd())

if not os.path.isfile(cur_dir +'/duration.txt') and not os.path.isfile(cur_dir +'/finished.txt'):
    print('yes')
    #get_fb_duration('links.txt', 'duration.txt', 'finished.txt', '../../geckodriver', 3) 
else:
    tmp = cur_dir + '/tmp'
    if not os.path.isdir(tmp):
        os.mkdir(tmp)
    else:
        get_nonetype = cur_dir + '/duration.txt'
        #get_nonetype = cur_dir + '/links_2.txt'
        with open(get_nonetype) as f:
            for line in f:
                if 'NoneType' in line.strip('\n'):
                    print(line.strip('\n'))
                    break
                    
                    
        #f = open(get_nonetype)
        #get_chunks = ""
        #for piece in read_in_chunks(f):
            #get_chunks += piece
            #for f in piece.split('\n'):
                #if 'NoneType' in f:
                    #print(f)
                #else:
                    #print(f)
            
        #print(type(get_chunks))
        #print(len(get_chunks.split('\n')))
        #print(get_chunks.split('\n'))
        #for f in get_chunks.split('\n'):
            #if 'NoneType' in f:
                #print(f)
        
        
    
        
    
    
        
        
#get_fb_duration('links.txt', 'duration.txt', 'finished.txt', '../../geckodriver', 3)        
        
        




