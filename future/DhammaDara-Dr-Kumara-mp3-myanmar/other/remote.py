import os
import sys

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'
#print('a', running_from_path)

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, thread_upload_remote)

#fb
#rearrange_urls('raw_urls.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
#download_fb('du.txt', 3)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)


remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.39'
escaped_remote = '/storage/1527-15E5/youtube/DhammaDara-Dr-Kumara-mp3-myanmar/'
remote_port = 8022
#copy_to_remote('*.pdf',
#copy_to_remote('*.mp4',
                #remote_username, remote_pass, remote_hostname, remote_port, escaped_remote
                #)
thread_upload_remote('*.mp4', running_from_path,
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote,
                3
                )
