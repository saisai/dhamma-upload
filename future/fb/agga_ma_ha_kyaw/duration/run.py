#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,
                    get_fb_duration)

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

#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver')
#get_fb_duration('links.txt', 'duration.txt', 'finished.txt', '../geckodriver')
get_fb_duration('redo.txt', 'duration_edited.txt', 'finished_edited.txt', '../geckodriver')
#download_fb('du.txt', 1)
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
	playlist = 'Bokyaung page မွာ videos မ်ား'
	description_title = 'Bokyaung page မွာ videos မ်ား'
	source='\nsource from https://www.facebook.com/pg/bokyaung/videos/'
	get_json_fb('titles.txt', 'results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt

#get_splited_lines('links.txt', 30)

#download_fb('links.txt', 3)
#thread_upload('raw_json_title.txt', 1)
#thread_upload_test('raw_json_title.txt')
#thread_upload_test_title('raw_json_title.txt')

