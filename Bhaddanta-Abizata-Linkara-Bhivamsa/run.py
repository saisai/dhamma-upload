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
                    
                    )
                    
                    
                    
  
                    
              

#get_html_mp3('raw_html.txt', 'raw_titles_links.txt', 1)


#check_duplicate('raw_titles_links.txt') #titles_links.txt
#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)
#convert_myanmar_number_option('raw_titles_links.txt', 'titles_links.txt', 1)


#breaker_in_order(get_results('titles_links_desc.txt'))

#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt

def get_json_new():    
    
    playlist = '​စစ္​ကိုင္​းတိပိဋကဆရာ​ေတာ္ အသွ်င္အဘိဇာတာဘိဝံသ ေဟာေတာ္မူေသာ တရားေတာ္မ်ား'
    description_title = 'ဓမၼာစရိယ (၁၀)ဘြဲ႕၊ ပါဠိပါရဂူ (၃)ဘြဲ႕၊ ဝိဒူ(၅)ဘြဲ႕၊ မဟာဝိဒူ(၅)ဘြဲ႕ႏွင့္ အျခားအစိုးရ တိပိဋကဆုိင္ရာ ဘြဲ႕မ်ား အပါအဝင္ ဘြဲ႕တံဆိပ္ေပါင္း (၄၇)ဘြဲ႕ရ မုံရြာၿမိဳ႕ သဒၶမၼေဇာတက သုေဗာဓါရုံေက်ာင္းတိုက္၊ ဒြါဒသမ တိပိဋက ဓရ ဓမၼဘ႑ာဂါရိက အသွ်င္အဘိဇာတာဘိဝံသ စစ္ကိုင္းဆရာေတာ္ ေဟာေတာ္မူေသာ တရားေတာ္မ်ား'
    source='\nsource from http://www.dhammadownload.com' 
    get_json_files_in_same('titles_links.txt', 'titles_links.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
    #get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt




#get_json_new()
thread_upload_test_title('raw_json_title.txt')







