#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote)

#fb
#rearrange_urls('raw_urls.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
#download_fb('du.txt', 3)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)


remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.38'
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/youtube/PilotSayadawJeYaPandita/fb/'
remote_port = 8022
#copy_to_remote('*.pdf',
copy_to_remote('*.mp4',
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote
                )


'''
playlist = 'ပိုင္းေလာ့ဆရာေတာ္-Pilot Sayartaw'
description_title = 'ပိုင္းေလာ့ဆရာေတာ္-Pilot Sayartaw ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား'
source='\nsource from https://www.facebook.com/pg/pilotsayartaw/videos/'
get_json_fb('title.txt', 'edited_results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
'''


#get_html_mp4('get_url.txt', 'raw_titles_links.txt', 1)
#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)


#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt


'''
playlist = 'ပိုင္းေလာ့ ဆရာေတာ္္ အရွင္ေဇယ်ပ႑ိတ  ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား'
description_title = 'ပိုင္းေလာ့ ဆရာေတာ္္ အရွင္ေဇယ်ပ႑ိတ  ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား'
source='\nsource from http://dhammadownload.com/'
get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
'''


#thread_download('titles_links.txt', 1)
#thread_upload_test('raw_json_title.txt')
#thread_upload('raw_json_title.txt', 1)