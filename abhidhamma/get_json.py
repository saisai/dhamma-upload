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


descriptions = [title.strip('\n') for title in open('description.txt')]
get_count_descriptions = len(descriptions)
print(get_count_descriptions)

description_title ="သင္တန္းမွဴး၊ ဓမၼဗ်ဴဟာ  ေခၚခင္လွတင္ (မဟာသဒၶမၶေဇာတိကဓဇ)  ဓမၼဗ်ဴဟာ သာသနမာမကအဖြဲ႕ လူပုဂၢိဳလ္မ်ားဆိုင္ရာ ဓမၼစာေပသင္တန္းေက်ာင္း "
source = "\nအဘိဓမၼာ (ရိုးရိုး) ပထမဆင္႔သင္တန္း (၂၀၁၈)\nsource from http://www.dhammadownload.com"


results = []    
count = 114
playlist = "သင္တန္းမွဴး၊ ဓမၼဗ်ဴဟာ  ေခၚခင္လွတင္ (မဟာသဒၶမၶေဇာတိကဓဇ) ပို႔ခ်ေသာ ရုပ္/သံ မ်ား"
for title, description in zip(titles, descriptions):
    #print('{}'.format(title))
    #print('{}။{}'.format(change(counter), title.split('။')[1]))
    counter = '{:03}'.format(count)
    if len('{}။{}'.format(change(counter), title.split('။')[1])) > 100:
        dict_title = {
                     "playlist" : playlist,
                     "title": "{}".format(title),
                      "description": "{}\n{}{}".format(description_title, description, source), 
                       "id": "{}".format(counter)
                    }       

        print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
        results.append(dict_title)
    else:
        dict_title = {
                      "playlist" : playlist,
                     "title": "{}".format(title),
                      "description": "{}\n{}{}{}".format(description_title, description.split('|')[1], description.split('|')[0], source), 
                       "id": "{}".format(counter)
                    }       

        results.append(dict_title)
    count += 1
    
data = json.dumps(results, indent=4)        
with open('raw_json_title.txt', encoding='utf-8', mode='w') as f:
    json.dump(data, f)
