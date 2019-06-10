#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_html_mp4, get_html_mp3, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test,
                    update_raw_reversed_titles_links)
                    
                    
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)
                    

#get_html_mp3('get_url.txt', 'raw_titles_links.txt', 1)
#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)


#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt



playlist = 'ေညာင္တုန္း ဆရာေတာ္ ဘဒၵႏ ၱေဇာတိကဘိဝံသ ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား(mp3s)'
description_title = 'ေညာင္တုန္း ဆရာေတာ္ ဘဒၵႏ ၱေဇာတိကဘိဝံသ ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား(mp3s)'
source='\nsource from https://www.thitsarparamisociety.com/ashin-zaw-ti-ka-nyaungdone/'
get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt



#thread_download('titles_links.txt', 1)
#thread_upload_test('raw_json_title.txt')
#thread_upload('raw_json_title.txt', 1)