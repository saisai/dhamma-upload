#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb_2,
                    get_splited_lines, download_fb, thread_upload, thread_upload_test_title)

#fb
'''
var myVar = setInterval(function(){window.scrollTo(0, document.body.scrollHeight);}, 10000);
clearInterval(myVar);

function myTimer() {
  window.scrollTo(0, document.body.scrollHeight);
}

function myStopFunction() {
  clearInterval(myVar);
}
'''
#rearrange_urls('raw_urls.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
#download_fb('du.txt', 1)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)

'''
remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.39'
escaped_remote = '/storage/1527-15E5/youtube/SayaDaw-U-ThuMinGaLA/'
remote_port = 8022
#copy_to_remote('*.pdf',
copy_to_remote('*.mp4',
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote
                )
'''

def get_json():
    playlist = 'သုမဂၤလာ ဗုဒၶတရားေတာ္ႏွင့္ လုပ္ငန္းစဥ္ျပန္႕ပြားေရး တရားဌာန မဂၤလာတိုက္ page မွာ videos မ်ား'
    description_title = 'သုမဂၤလာ ဗုဒၶတရားေတာ္ႏွင့္ လုပ္ငန္းစဥ္ျပန္႕ပြားေရး တရားဌာန မဂၤလာတိုက္ page မွာ videos မ်ား'
    source='\nsource from https://www.facebook.com/pg/thumingalarfoundation/videos/'
    #get_json_fb('edit_titles.txt', 'edit_desc.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
    get_json_fb_2('edit_titles.txt', 'edit_desc.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt

    
#get_json()
#get_splited_lines('links.txt', 30)

#download_fb('0.txt', 1)
#thread_upload('raw_json_title.txt', 1)
thread_upload_test_title('raw_json_title.txt')

