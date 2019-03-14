

from crawler.core import (
    get_html_mp4,
    get_html_mp3,
    check_duplicate,
    convert_myanmar_number,
    get_json,    
    update_raw_titles_links,
)

from crawler.thread_download import thread_download

from crawler.thread_upload import thread_upload, thread_upload_test

from crawler.get_fb_title import get_fb_title, rearrange_urls

from crawler.fb_thread_download import download_fb



'''
if __name__ == '__main__':
    get_html(sys.argv[1])
'''