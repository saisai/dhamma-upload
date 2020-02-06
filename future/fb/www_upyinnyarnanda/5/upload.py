#!/data/data/com.termux/files/usr/bin/env python
# coding=utf-8
import os

from crawler import (get_html_mp4, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test,
                    thread_upload_test_title)


full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)


#thread_upload_test_title('raw_json_title.txt')

thread_upload('raw_json_title.txt', 1)

