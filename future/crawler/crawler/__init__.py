

from crawler.core import (
    get_html_mp4,
    get_html_mp3,
    check_duplicate,
    convert_myanmar_number,
    get_json,    
    get_json_fb,
    update_raw_titles_links,
    update_raw_reversed_titles_links,
    get_splited_lines,
    check_link,
    get_line_from_file,
    copy_to_remote
)

from crawler.thread_download import thread_download

from crawler.thread_upload import thread_upload, thread_upload_test

from crawler.get_fb_title import get_fb_title, rearrange_urls

from crawler.fb_thread_download import download_fb

from crawler.thread_convert_mp3_to_mp4 import thread_convert_mp3_to_mp4





'''
if __name__ == '__main__':
    get_html(sys.argv[1])
'''