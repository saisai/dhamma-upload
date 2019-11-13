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


def get_new_result(cur_dir):
    # To remove the NoneType from the file
    duration = [f.strip('\n') for f in open(cur_dir+'/duration.txt')]

    finished = [f.strip('\n') for f in open(cur_dir+'/finished.txt')]


    new_duration = [f for f in duration if f.split('|')[2] == 'NoneType']
    edited_duration = [f for f in duration if f.split('|')[2] != 'NoneType']



    for get_duration in edited_duration:
        with open(cur_dir+'/duration_edited.txt', 'a') as f:
            f.write(get_duration)
            f.write('\n')
            
            


    seen_duration = set()
    seen_finished = {}
    print('New Duration', len(new_duration))
    #if len(new_duration) > 0:
    
    for link in new_duration:
        for cmp_link in finished:
            #print(link.split('|')[1] in cmp_link.split('|')[1])
            if link.split('|')[1] in cmp_link.split('|')[1]:
                print(link)
                print(cmp_link)
                with open(cur_dir+'/redo.txt', 'a') as f:
                    seen_duration.add(cmp_link)
                    f.write(cmp_link)
                    f.write('\n')
                    
    for cmp_link in finished:
        
        if cmp_link not in seen_duration:        
            with open(cur_dir+'/finished_edited.txt', 'a') as f:
                seen_duration.add(cmp_link)
                f.write(cmp_link)
                f.write('\n')                        
                    
    duration_edited = cur_dir+'/duration_edited.txt'
    finished_edited = cur_dir+'/finished_edited.txt'
    duration = cur_dir+'/duration.txt'
    finished = cur_dir+'/finished.txt'    
    os.rename(duration_edited, duration)
    os.rename(finished_edited, finished)

        
                        
        #return True
        
    #else:
        #return False        
    
        
        
print(os.getcwd())

stop_loop = True
while True:

    if not os.path.isfile(cur_dir +'/duration.txt') and not os.path.isfile(cur_dir +'/finished.txt'):
        print('first time')
        get_fb_duration('links.txt', 'duration.txt', 'finished.txt', '../../geckodriver', 4)
    elif os.path.isfile(cur_dir +'/duration.txt') and os.path.isfile(cur_dir +'/finished.txt') and os.path.isfile(cur_dir +'/redo.txt'):
        print('redo')
        time.sleep(1)
        get_fb_duration('redo.txt', 'duration.txt', 'finished.txt', '../../geckodriver', 4)
        
        get_nonetype = cur_dir + '/duration.txt'
        
        
        
        with open(get_nonetype) as f:
            
            count_NoneType = 0
            
            for line in f:
                if 'NoneType' in line.strip('\n'):
                    print(line.strip('\n'))
                    
                    count_NoneType += 1
                    
            
            if count_NoneType != 0:
                
                redo = cur_dir +'/redo.txt'
                if os.path.isfile(redo):
                    os.remove(redo)
                    
                get_new_result(cur_dir)
                time.sleep(1) # sleep for 1 second
            else:
                redo = cur_dir +'/redo.txt'
                if os.path.isfile(redo):
                    os.remove(redo)            
                break # break the main loop
                

    else:
        print('else')
        get_nonetype = cur_dir + '/duration.txt'        
        
        with open(get_nonetype) as f:
            
            count_NoneType = 0
            
            for line in f:
                if 'NoneType' in line.strip('\n'):
                    print(line.strip('\n'))
                    
                    count_NoneType += 1
                    
            
            if count_NoneType != 0:
                
                redo = cur_dir +'/redo.txt'
                if os.path.isfile(redo):
                    os.remove(redo)
                    
                get_new_result(cur_dir)
                time.sleep(1) # sleep for 1 second
            else:
                redo = cur_dir +'/redo.txt'
                if os.path.isfile(redo):
                    os.remove(redo)            
                break # break the main loop        
        '''
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
                        
                        redo = cur_dir +'/redo.txt'
                        if os.path.isfile(redo):
                            os.remove(redo)
                            
                        get_new_result(cur_dir)
                        time.sleep(1) # sleep for 1 second
                        
                        break   # inner loop break
        
                    
        '''            

        
        
    
        
    
    
        
        
#get_fb_duration('links.txt', 'duration.txt', 'finished.txt', '../../geckodriver', 3)        
        
        




