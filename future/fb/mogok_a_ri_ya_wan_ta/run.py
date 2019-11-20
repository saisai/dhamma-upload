#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb_2,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,check_duplicate)

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
#rearrange_urls('raw_url.txt', 'links.txt')
#check_duplicate('links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
#download_fb('du.txt', 1)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)


def get_json():
	playlist = 'အရိယဝံသ မိုးကုတ္ဝိပႆနာ မဂၢင္ဓမၼရိပ္သာ page မွ တရားေတာ္မ်ား'
	description_title = 'အရိယဝံသ မိုးကုတ္ဝိပႆနာ မဂၢင္ဓမၼရိပ္သာ page မွ တရားေတာ္မ်ား'
	source='\nsource from https://www.facebook.com/pg/အရိယဝံသ-မိုးကုတ္ဝိပႆနာ-မဂၢင္ဓမၼရိပ္သာ-257435104635888/videos//'
	#get_json_fb_2('edit_titles.txt', 'edit_results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
	get_json_fb('edit_titles.txt', 'edit_results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
	#get_json_fb('edit_titles.txt', 'edit_results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt

    
#get_json()    
#thread_upload_test_title('raw_json_title.txt')

