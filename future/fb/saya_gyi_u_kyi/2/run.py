#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,get_json_files_in_same)

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
rearrange_urls('fb_links.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
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
	playlist = 'Komyo Aung page (fb) မွ ဆရာႀကီးဦးၾကည္ သင္ႀကားပို႔ခ်ေသာ တရားေတာ္မ်ား'
	description_title = 'သစၥာဒီပက၀ိပႆနာအဖြဲ႕ခ်ဳပ္ တရားျပဌာန ဦးစီးပဓာနနာယက၊ အာဒိကမၼိက ကမၼဌာနစရိယ မူလဓမၼာစရိယ၊ ပရိယတၱိမာမက၊ ပဋိပတၱိ၀ိသာရဒ ပဋိပတၱိသာသာနာ့ဟိတရဓရ ဘြဲ႕ရ က်မ္းျပဳပုဂၢိဳလ္ ဆရာႀကီးဦးၾကည္ သင္ႀကားပို႔ခ်ေသာ တရားေတာ္မ်ား'
	source='\nsource from https://www.facebook.com/profile.php?id=100037549250042&lst=100007043114370%3A100037549250042%3A1569295868&sk=videos/'
	get_json_files_in_same('title_results.txt', 'title_results.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt

    
#get_json()    
#thread_upload_test_title('raw_json_title.txt')

