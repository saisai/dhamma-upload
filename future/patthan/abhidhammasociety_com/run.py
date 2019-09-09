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


#check_duplicate('links_title.txt') #titles_links.txt

#update_raw_titles_links('raw_titles_links.txt', 'titles_links.txt', 1)
#convert_myanmar_number_option('raw_titles_links.txt', 'titles_links.txt', 1)

#add_extra_description(get_results('raw_titles_links_desc.txt'))
#breaker_in_order(get_results('titles_links_breaker.txt'))

#convert_myanmar_number('titles_links.txt', 'description.txt') # titles_links.txt description.txt

def get_json_new():    
    
    playlist = 'သံဃာေတာ္မ်ား ရြတ္ဖတ္ပူေဇာ္ထားေသာ မဟာပ႒ာနပါဠိေတာ္ ၅-က်မ္း စာမ်က္ႏွာအလိုက္ အသံဖိုင္မ်ား'
    description_title = 'အသံမစဲ မဟာပ႒ာန္းပြဲတြင္ ပါ၀င္ ရြတ္ဖတ္ပူေဇာ္မည့္သူမ်ား လြယ္ကူစြာ ေလ႔က်င့္ႏိုင္ရန္ရည္ရြယ္၍ အေမရိကန္ႏိုင္ငံ ျဗဟၼ၀ိဟာရ(အဇူဇာေက်ာင္း) ဘုန္းေတာ္ၾကီးေက်ာင္းတြင္ ျပဳလုပ္က်င္းပခဲ႔သည့္ ၁၀ၾကိမ္ေျမာက္ အသံမစဲ မဟာပ႒ာန္းပြဲတြင္ သံဃာေတာ္မ်ား ရြတ္ဆိုပူေဇာ္ထားေသာ mp3 အသံဖိုင္မ်ားကို ဓမၼဗြီဒီယို မွ ရယူထားပါသည္။ ဗုဒၶအလင္းေရာင္မွ ကိုျမင့္ထြန္းမွ စာမ်က္ႏွာ နံပါတ္မ်ားကို နာယူေလ့က်င့္သူမ်ား လြယ္ကူအဆင္ေျပေစရန္အတြက္ ရွာေဖြျပဳစုေပးထားပါသည္။'
    source='\nsource from http://www.abhidhammasociety.com/mahar-patthan-audio/mahar-patthan-azuza/' 
    get_json_files_in_same('titles.txt', 'titles.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt
    #get_json('titles_links.txt', 'description.txt', 'raw_json_title.txt',playlist, description_title, source) #titles_links.txt description.txt raw_json_title.txt




#get_json_new()
thread_upload_test_title('raw_json_title.txt')







