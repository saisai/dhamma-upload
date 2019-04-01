#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_html_mp4, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test, get_html_mp3,
                    change_order, get_results, thread_convert_mp3_to_mp4)
                    
                    
                    
  
                    
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)
                    

#get_html_mp3('get_url.txt', 'raw_titles_links.txt', 1)

#for txt in change_order(list(reversed(get_results('raw_titles_links.txt')))):
#    print(txt)

#check_duplicate('links.txt') #titles_links.txt
#update_raw_titles_links('links.txt', 'titles_links.txt', 1)


#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt


'''
playlist = 'ေဒါက္တာစိုးလြင္ (မႏၲေလး) ၀ိသုဒၶိမဂ္ဓမၼလမ္း၀ိပႆနာသင္တန္း တရားေတာ္မ်ား'
description_title = 'ေဒါက္တာစိုးလြင္ (မႏၲေလး) ၀ိသုဒၶိမဂ္ဓမၼလမ္း၀ိပႆနာသင္တန္း တရားေတာ္မ်ား'
source='\nsource from https://www.thitsarparamisociety.com/'
get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
'''


#thread_download('titles_links.txt', 1)
thread_upload_test('raw_json_title.txt')
#thread_upload('raw_json_title.txt', 1)


#thread_convert_mp3_to_mp4(1)



