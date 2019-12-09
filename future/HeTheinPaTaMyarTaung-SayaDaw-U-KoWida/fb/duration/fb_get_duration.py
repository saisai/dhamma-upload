#!/usr/bin/env python
# coding=utf-8
import os

import os.path
import time
import re

import inspect
from pathlib import Path

cur_dir = os.getcwd() # get current working directory
print(cur_dir)

from crawler import (get_fb_title, rearrange_urls, download_fb,
                    get_json_fb, thread_upload_test, copy_to_remote, convert_myanmar_number,
                    update_raw_titles_links, get_json_fb,
                    get_splited_lines, download_fb, thread_upload,
                    thread_upload_test_title,
   get_fb_duration, get_fb_duration_result, check_duplicate)



if __name__ == '__main__':
    #check_duplicate('links.txt') #titles_links.txt
    #main()
    get_fb_duration_result(2, cur_dir, "../../geckodriver")                   