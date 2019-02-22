# -*- coding: utf-8 -*-

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
titles = [title.strip('\n\n\n') for title in open('titles_links.txt')]

one="စုစည္းထားေသာ အကၡရာစဥ္ တရားေတာ္မ်ား"
two="မ်က္ေမွာက္ခ်မ္းသာေရး တရားေတာ္မ်ား"
three="သတိပ႒ာန္အက်ိဳး တရားေတာ္မ်ား"
four="သတိပ႒ာန္ ေၾကြးေၾကာ္သံ တရားေတာ္မ်ား"
five="အရိယာတို႔၏ စံအိမ္ တရားေတာ္မ်ား"
six="အေျခခံဘာသာေရး"
seven ="အရိယာဝါသတရားေတာ္မ်ား"
eight="ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး တရားေတာ္မ်ား"
nine="ဣရိယာပထပိုင္း တရားတေတာ္မ်ား"
ten="(၇.၇.၂၀၁၃)အေမရိကန္၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၇) တရားစခန္း"
eleven="(၁၄.၇.၂၀၁၃) အေမရိကန္၊ ေမရီလန္းျပည္နယ္ (၁၀)ရက္ တရားစခန္း"
twelve ="(၁၃.၆.၂၀၁၄) အေမရိကန္ႏိုင္ငံ၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း"
title_13 ="(၂၁.၅.၂၀၁၄) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား၊ LA ဓမၼစကၡဳဓမၼာရံု မဟာသတိပ႒ာန္ (၆)ရက္ တရားစခန္း"
title_14="(၁၄.၇.၂၀၁၅) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား LA ေကာင္တီ၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း"
title_15 = "(၁၂.၆.၂၀၁၅) အေမရိကန္ႏိုင္ငံ၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း"
title_16="(၂၃.၅.၂၀၁၆) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း"
title_17="(၃.၆.၂၀၁၆) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား LA ေကာင္တီ၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း"
title_18="(၁၁.၆.၂၀၁၆) အေမရိကန္၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း"
title_19="(၁၀.၆.၂၀၁၇) အေမရိကန္ႏိုင္၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း"
title_20="(၁၁.၅.၂၀၁၇) အေမရိကန္၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို၊ ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း"
title_21="(၂၂.၅.၂၀၁၇) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယားျပည္နယ္၊ ဆန္ဖရန္စစၥကို၊ မတ္မြန္ေဘးၿမိဳ႕၊ အခ်ိန္ျပည္႔ ( ၇ ) ရက္ တရားစခန္း "


desc = {
	'one': (one, 1, 169),
	'two': (two, 170, 175),
	'three': (three, 176, 185),
	'four': (four, 186, 211),
	'five': (five, 212, 216),
	'six': (six, 217, 223),	
	'seven': (seven, 224, 230),	
	'eight': (eight, 231, 239),	
	'nine': (nine, 240, 244),	
	'ten': (ten, 245, 257),	
	'eleven': (eleven, 258, 266),
	'twelve': (twelve, 267, 276),
	'title_13': (title_13, 277, 287),
	'title_14': (title_14, 288, 298),
	'title_15': (title_15, 299, 320),
	'title_16': (title_16, 321, 332),
	'title_17': (title_17, 333, 343),
	'title_18': (title_18, 344, 354),
	'title_19': (title_19, 355, 375),
	'title_20': (title_20, 376, 391),
	'title_21': (title_21, 392, 403),

	 }
     
'''
for dd in desc.items():
    
    for i in range(0, 467):
        #print(dd[1][0], 'test')
        if dd[1][1] <= i <= dd[1][2]:
            print(dd[1][0])
'''

with open('description.txt', 'w') as f:
    counter = 1
    for dd in desc.items():
        
        for title in titles:
                    
            number = int(title.split('|')[0].split('.')[0])
            #print(type(number))
            if dd[1][1] <= number  <= dd[1][2]:
                print(dd[1][0])
                print(title.split('|')[2])            
                    
                try:
                    
                    f.write('{}။{}|{}\n'.format(change(counter), title.split('|')[2].split('။')[1], dd[1][0]))
                    #print('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
                    #print(title.split('|')[2])
                    
                except IndexError as err:
                    f.write('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                    #print('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                    
                
                #print('{}။{}'.format(change(counter), title))
                
                counter += 1            
            
            
        
        
'''
for title in titles:
    
    #print(type(int(title.split('|')[0].split('.')[0])))
    
    for dd in desc.items():
        if dd[1][0]
        print(dd[1][0])
        print(type(dd[1][1]))
'''    
"""
with open('title.txt', 'w') as f:
    counter = 1
    for title in titles:
        
        try:
            
            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
            #print('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
            #print(title.split('|')[2])
            
        except IndexError as err:
            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2]))
            #print('{}။{}|\n'.format(change(counter), title.split('|')[2]))
            
        
        #print('{}။{}'.format(change(counter), title))
        '''
        try:
        
            if title.split('|')[2].split('။')[1]:
                print('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
        except IndexError as err:
            print('{}။{}|\n'.format(change(counter), title.split('|')[2]))
        '''
        counter += 1
"""