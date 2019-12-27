#!/usr/bin/env python
# coding=utf-8
import os
import sys

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'
#print('a', running_from_path)

from crawler import (get_html_mp4, check_duplicate,
                    convert_myanmar_number, get_json,
                    thread_download, update_raw_titles_links,
                    thread_upload, thread_upload_test, get_html_mp3,
                    change_order, get_results, thread_convert_mp3_to_mp4,
                    thread_upload_test_title, thread_upload_remote,  
                    get_json_option,
                    get_json_files_in_same,
                    convert_myanmar_number_option,
                    get_json_title,
                    add_extra_description,
                    breaker_in_order,
                    thread_download,
                    )
                    
                    
                    
  
                    
              

#get_html_mp3('raw_html.txt', 'raw_titles_links.txt', 1)
#get_html_mp4('raw_html.txt', 'raw_titles_links.txt', 1)


#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)
#convert_myanmar_number_option('raw_titles_links.txt', 'titles_links.txt', 1)


#breaker_in_order(get_results('desc.txt'))

#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt

def get_json_new():    
    
    playlist = 'အဘိဓမ္မာဂုဏ်ထူးဆောင် (ဋီကာကျော်) ပထမဆင့်သင်တန်း စိတ်ပိုင်း(၂၀၁၉)'
    description_title = 'ဓမ္မဗျူဟာ ဒေါ်ခင်လှတင် မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ ဓမ္မဗျူဟာ သာသနမာမကအဖွဲ့  လူပုဂ္ဂိုလ်များဆိုင်ရာ ဓမ္မစာပေသင်တန်းကျောင်း အမှတ်(၆)၊ ကြားတောရလမ်း၊ ဗဟန်းမြို့နယ်၊ ရန်ကုန် ဖုန်း။ (၉၅) ၀၁-၃၈၀၈၈၀ \n  ဓမ္မဗျူဟာ ဒေါ်ခင်လှတင် မဟာ သဒ္ဓမ္ဓဇောတိကဓဇ သင်ကြားပို့ချသော တရားတော်များ'
    source='\nsource from http://www.dhammadownload.com/' 
    get_json_files_in_same('titles_links.txt', 'titles_links.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
    #get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt



#thread_download('titles_links.txt', 2)
#get_json_new()
#thread_download("titles_links.txt", 3)
thread_upload_test_title('raw_json_title.txt')
#thread_convert_mp3_to_mp4(3)







