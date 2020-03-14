import os
import sys

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'

from crawler import (get_fb_title, rearrange_urls, download_fb,
                    get_json_fb, thread_upload_test, copy_to_remote, thread_upload_remote)

#fb
#rearrange_urls('raw_urls.txt', 'links.txt')
#get_fb_title('links.txt', 'results.txt', 'finished.txt', 'geckodriver.exe')
#download_fb('du.txt', 3)
#copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote)



remote_username = 'u0_a97'
remote_pass = 'snp'
remote_hostname = '192.168.1.45'
escaped_remote = '/storage/34A5-151A/youtube/4/'
remote_port = 8022
#copy_to_remote('*.pdf',
# thread_upload_remote(copied_file, running_from_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, threads):

#for i in range(0, 10):
#test = '[0-9][0-5][0-9][0-9].mp4'
test = '*.mp4'
thread_upload_remote('%s' % (test, ), running_from_path,
                remote_username, remote_pass, remote_hostname, remote_port, escaped_remote,
                3
                )


