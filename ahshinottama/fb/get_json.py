# -*- coding: utf-8 -*-
import json
def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm

get_new = []
for m in range(0, 257):
    aa = change(m)
    #new_dict = {m: str(aa)}
    get_new.append('{}။'.format(aa))

#print(get_new)
titles = [title.strip('\n') for title in open('title.txt')]
get_count = len(titles)
print(get_count)


descriptions = [title.strip('\n') for title in open('new_urltext_upload.txt')]
get_count_descriptions = len(descriptions)
print(get_count_descriptions)

description_title ="သစၥာေရႊစည္ဆရာေတာ္ အရွင္ဥတၱမ (စစ္ကိုင္ မင္းဝံေတာင္တန္း)  ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
source = "\nsource from https://www.facebook.com/thitsarshwesiahshinOttama/"


results = []    
count = 1
playlist = "သစၥာေရႊစည္ဆရာေတာ္ အရွင္ဥတၱမ (စစ္ကိုင္ မင္းဝံေတာင္တန္း)  ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
for title, description in zip(titles, descriptions):
    #print('{}'.format(title))
    #print('{}။{}'.format(change(counter), title.split('။')[1]))
    #counter = '{:03}'.format(count)
    counter = description.split('|')[0]
    
    #title = '{}။{}'.format(change(counter), title.split('။')[1])
    #description_zero = '{}။{}'.format(change(counter), description.split('|')[0].split('။')[1]) 
    description_zero = description.split('|')[1]
    #print(description_zero)
    #if len('{}။{}'.format(change(counter), title.split('။')[1])) > 100:
    if len(title) > 100:
        dict_title = {
                     "priority" : count,
                     "playlist" : playlist,
                     "title": "{}".format(title),
                      "description": "{}\n{}{}".format(description_title, description_zero, source), 
                       "id": "{}".format(counter)
                    }       

        print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
        results.append(dict_title)
    else:
        print(len("{}\n{}{}{}".format(description_title, description.split('|')[1], description_zero, source)))
        dict_title = {
                      "priority" : count,
                      "playlist" : playlist,
                     "title": "{}".format(title),
                      "description": "{}\n{}{}".format(description_title, description.split('|')[1], source),  
                       "id": "{}".format(counter)
                    }       
                    # "description": "{}\n{}\n{}".format(description_title, description.split('|')[1], source),
                    #"description": "{}\n{}{}{}".format(description_title, description.split('|')[1], description_zero, source), 

        results.append(dict_title)
    count += 1
    
data = json.dumps(results, indent=4)        
with open('raw_json_title.txt', encoding='utf-8', mode='w') as f:
    json.dump(data, f)
