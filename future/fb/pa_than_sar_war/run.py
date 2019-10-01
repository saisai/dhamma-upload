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
                    get_json_option,
                    get_json_files_in_same,
                    convert_myanmar_number_option,
                    get_json_title,
                    add_extra_description,
                    breaker_in_order,
                    
                    )
                    
                    
                    
  
                    
              

#get_html_mp3('raw_html.txt', 'raw_titles_links.txt', 1)


#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)
#convert_myanmar_number_option('raw_titles_links.txt', 'titles_links.txt', 1)


#breaker_in_order(get_results('titles_links_desc.txt'))

#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt

def get_json_new():    
    
    playlist = 'မႏၲေလးၿမိဳ့ မဟာဝိသုဒၶါ႐ုံတိုက္သစ္ စည္ရွင္ေက်ာင္း အရွင္ဝဏၰိတာလကၤာရာဘိဝံသ၏ ပ႒ာန္းစာဝါ အသံဖိုင္မ်ား'
    description_title = 'မႏၲေလးၿမိဳ့ မဟာဝိသုဒၶါ႐ုံတိုက္သစ္ စည္ရွင္ေက်ာင္း အရွင္ဝဏၰိတာလကၤာရာဘိဝံသ၏ ပ႒ာန္းစာဝါ အသံဖိုင္မ်ား။ credit= အရွင္ဓမၼိႆာရာလက္ာရ'
    source='\nsource from https://www.facebook.com/profile.php?id=100027409260250 \n ပရိယတၱိစာေမးပြဲဆိုင္ရာ ပုစၧာေရာင္ျခည္' 
    get_json_files_in_same('title_links.txt', 'title_links.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
    #get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt




#get_json_new()
thread_upload_test_title('raw_json_title.txt')







