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
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/youtube/dr-soe-lwin/'
remote_port = 8022
#copy_to_remote('*.pdf',
copy_to_remote('*.mp4',
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote
                )

