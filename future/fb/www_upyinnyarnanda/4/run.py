#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb_2,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,
                    get_json_fb,get_json_files_in_same)

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
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
download_fb('links.txt', 2)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)

'''
remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.36'
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/PahtamagyiGrade/'
remote_port = 8022
#copy_to_remote('*.pdf',
copy_to_remote('AshinTayzaniya-YamakaAhLinYaung-for-Pahtamagyigrade.pdf',
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote
                )
'''  
def get_json():
	playlist = 'မဟာမင္းထင္ေက်ာင္းတိုက္ ဓမၼဒီပေက်ာင္းဆရာေတာ္ page မွာ videos မ်ား'
	description_title = 'မဟာမင္းထင္ေက်ာင္းတိုက္ ဓမၼဒီပေက်ာင္းဆရာေတာ္ page မွာ videos မ်ား'
	source='\nsource from https://www.facebook.com/pg/www.upyinnyarnanda/videos/'
	#get_json_fb_2('edit_titles.txt', 'edit_titles.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
	#get_json_fb('edit_titles.txt', 'edit_titles.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
	get_json_files_in_same('edit_titless.txt', 'edit_titles.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt

    
#get_json()    
#thread_upload_test_title('raw_json_title.txt')

