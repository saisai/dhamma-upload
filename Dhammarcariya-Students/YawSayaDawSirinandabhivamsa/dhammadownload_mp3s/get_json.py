# -*- coding: utf-8 -*-
import json
def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    
    strmm = ''
    mmlist = list(map(int, str(num)))
    eng = ''
    for i in mmlist:
        eng += str(i)
        #print(i)
        strmm += mm[i]

    return eng

get_new = []
for m in range(0, 257):
    aa = change(m)
    #new_dict = {m: str(aa)}
    get_new.append('{}။'.format(aa))

#print(get_new)
titles = [title.strip('\n') for title in open('titles_links.txt')]
get_count = len(titles)
print(get_count)


descriptions = [title.strip('\n') for title in open('description.txt')]
get_count_descriptions = len(descriptions)
print(get_count_descriptions)


description_title ="တိပိဋကဓရ-အဂၢမဟာပ႑ိတ ေယာဆရာေတာ္ ဘဒၵႏၲသီရိႏၵာဘိဝံသ ဓမၼာစရိယ စာသင္သားမ်ားအတြက္ စာခ်တန္း(၃)က်မ္းအတြက္စာဝါမ်ား အသံဖိုင္မ်ား"
source = "\nsource from http://www.dhammadownload.com"


results = []    
playlist = "တိပိဋကဓရ-အဂၢမဟာပ႑ိတ ေယာဆရာေတာ္ ဘဒၵႏၲသီရိႏၵာဘိဝံသ ဓမၼာစရိယ စာသင္သားမ်ားအတြက္ စာခ်တန္း(၃)က်မ္းအတြက္စာဝါမ်ား အသံဖိုင္မ်ား"

for title, description in zip(titles, descriptions):
  
    
    if len(title.split('|')[2]) > 100:
        dict_title = {
                     "playlist" : playlist,
                     "title": "{}".format(title.split('|')[2]),
                      "description": "{}\n{}{}".format(description_title, description, source), 
                       "id": "{}".format( title.split('|')[0].split('.')[0] )
                    }       

        print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
        results.append(dict_title)
    else:
        dict_title = {
                      "playlist" : playlist,
                     "title": "{}".format(title.split('|')[2]),
                      "description": "{}\n{} ({}){}".format(description_title, description.split('|')[0], description.split('|')[1], source), 
                       "id": "{}".format(title.split('|')[0].split('.')[0])
                    }       

        results.append(dict_title)
    
    
data = json.dumps(results, indent=4)        
with open('raw_json_title.txt', encoding='utf-8', mode='w') as f:
    json.dump(data, f)
