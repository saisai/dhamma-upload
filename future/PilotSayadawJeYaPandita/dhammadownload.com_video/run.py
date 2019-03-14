#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_html_mp4, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test)

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


thread_download('titles_links.txt', 1)
#thread_upload_test('raw_json_title.txt')
#thread_upload('raw_json_title.txt', 1)