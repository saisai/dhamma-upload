#!/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_fb_title, rearrange_urls, download_fb, 
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,
                    thread_download_remote_local)


remote_username = 'walen'
remote_pass = 'walen'
remote_hostname = '192.168.1.123'
#escaped_remote = '/storage/34A5-151A/youtube/ashin_pon_nya_nanda/'
escaped_remote = '/home/walen/mahasi/crawler/'
local_path = '/cygdrive/e/dhamma-upload/future/fb/bokyaung/2/tt/'
remote_port = 22             
copied_file = "*.py"       
thread_download_remote_local(copied_file, local_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, 2)                    
