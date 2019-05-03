#!/usr/bin/env python
# coding=utf-8
import os
import sys

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'
#print('a', running_from_path)

from crawler import (get_html_mp4, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test, get_html_mp3,
                    change_order, get_results, thread_convert_mp3_to_mp4,
                    thread_upload_test_title, thread_upload_remote,
                    thread_convert_mp3_to_mp4_with_text
                    )
                    
                    
                    
  
                    
#full_path = os.path.realpath(__file__)
#path, filename = os.path.split(full_path)
#os.chdir(path)
                    

#get_html_mp3('raw_html.txt', 'raw_titles_links.txt', 1)

#for txt in change_order(list(reversed(get_results('raw_titles_links.txt')))):
#    print(txt)

#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('links.txt', 'titles_links.txt', 1)


#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt


'''
playlist = 'ေဒါက္တာစိုးလြင္ (မႏၲေလး) ၀ိသုဒၶိမဂ္ဓမၼလမ္း၀ိပႆနာသင္တန္း တရားေတာ္မ်ား'
description_title = 'ေဒါက္တာစိုးလြင္ (မႏၲေလး) ၀ိသုဒၶိမဂ္ဓမၼလမ္း၀ိပႆနာသင္တန္း တရားေတာ္မ်ား'
source='\nsource from https://www.thitsarparamisociety.com/'
get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
'''


#thread_download('raw_titles_links.txt', 5)
#thread_upload_test('raw_json_title.txt')
#thread_upload_test_title('raw_json_title.txt')
#thread_upload('raw_json_title.txt', 1)



thread_convert_mp3_to_mp4(4)
#thread_convert_mp3_to_mp4_with_text('convert_good.txt', running_from_path,  2)
'''
remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.38'
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/youtube/dr-soe-lwin/'
remote_port = 8022
#copy_to_remote('*.pdf',
# thread_upload_remote(copied_file, running_from_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, threads):
thread_upload_remote('*.mp4', running_from_path,
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote,
                2
                )
'''                
#thread_upload_remote(, 2)





