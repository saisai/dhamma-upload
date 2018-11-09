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
n = '\n' * 10
titles = [title.strip(n) for title in open('titles.txt')]

with open('title.txt', 'w') as f:
    counter = 1
    for title in titles:    
        print(title)
        """
        try:
            f.write('{}။{}\n'.format(change(counter), title.split('။')[1]))
        except IndexError as err:
            print(err)
            f.write('this line {}'.format(title.split('။')))     
        """
        #print('{}။{}'.format(change(counter), title))        
        
        counter += 1

"""
with open('description.txt', 'w') as f:
    counter = 1
    for title in titles:
    
        try:
            if counter <= 46:
                location = "အလုပ္ေပးတရာေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))
            elif counter <= 66:
                location = "(၂၀၁၂)ခုနွစ္၊ ဇြန္လ (၂၄)ရက္မွ ဇူလိုင္လ (၃)ရက္ေန႔အထိ ဆရာေတာ္ ဦးဣႏၵာဝုဓာ ဘိဝံသ (ထူးႀကီး ဆရာေတာ္) ေဟာၾကားဆံုးမေတာ္မူခဲ့ေသာ ခႏၶာဥာဏ္ေရာက္ ဒိဌိျဖဳတ္ ပဋိစၥသမုပါဒ္ သစၥာေလးပါး တရားေတာ္မ်ား (၂၀)ပုဒ္"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))        
            elif counter <= 86:
                location = "ေအာင္ပန္းၿမိဳ႕ မိုးကုတ္ဝိပႆနာတရားစဥ္ႏွင့္ လုပ္ငန္းစဥ္ျပန္႕ပြားေရး အဖြဲ႕ခြဲ အမွတ္္ (၃၂၉)မွ က်င္းပျပဳလုပ္အပ္ေသာ (၂၂)ႀကိမ္ေျမာက္ မိုးကုတ္ဝိပႆနာ (၁၀)ရက္တရားစခန္းပြဲ ၌ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            elif counter <= 106:
                location = "မိုးကုတ္၀ိပႆနာ တရားစဥ္ႏွင့္လုပ္ငန္းစဥ္ ျပန္႕ပြားေရး အဖြဲ႕ခ်ဳပ္ႀကီး၌ (၁၀)ရက္တရားစခန္းပြဲတြင္ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            elif counter <= 126:
                location = "မိုးကုတ္၀ိပႆနာ တရားစဥ္ႏွင့္လုပ္ငန္းစဥ္ ျပန္႕ပြားေရး အဖြဲ႕ခ်ဳပ္ႀကီး၌ (၅)ရက္တရားစခန္းပြဲတြင္ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))
            elif counter <= 154:
                location = "မိုးကုတ္၀ိပႆနာ တရားစဥ္ႏွင့္လုပ္ငန္းစဥ္ ျပန္႕ပြားေရး အဖြဲ႕ခ်ဳပ္ႀကီး၌ (၁၀)ရက္တရားစခန္းပြဲတြင္ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            elif counter <= 174:
                location = "(၅၀)ႀကိမ္ေျမာက္ မိုးကုတ္ဝိပႆနာ (၁၀)ရက္တရားစခန္းပြဲ ၌ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား ( ၂၀၀၇ )။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))
            elif counter <= 203:
                location = "မိုးကုတ္ဝိပႆနာ(၁၀)ရက္ တရားစခန္းတြင္ ေဟာၾကားေတာ္မူခဲ့ေသာ အလုပ္ေပး တရားေတာ္မ်ား (၁-၁၁-၂၀၀၇) (၁၀-၁၁-၂၀၀၇)။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            elif counter <= 222:
                location = "အေမရိကန္၊ နယူးေယာက္ၿမိဳ႕၊ မိုးကုတ္၀ိပႆနာရိပ္သာ (၅) ရက္တရားစခန္းပြဲတြင္ (July 31 to Aug 4, 2008) ၌ ေဟာၾကားေတာ္မူအပ္ေသာ တရားေတာ္မ်ား။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            elif counter <= 252:
                location = "အေမရိကန္၊ နယူးေယာက္ၿမိဳ႕၊ မိုးကုတ္၀ိပႆနာရိပ္သာ၊ (၁၀) ရက္တရားစခန္း (Aug 8 to 17, 2008) ၌ ေဟာၾကားေတာ္မူအပ္ေသာ တရားေတာ္မ်ား။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))
            else:
                location = "ဟသၤာတၿမိဳ႔ ၊ မိုးကုတ္၀ိပႆနာရိပ္သာ၊ (၇) ရက္တရားစခန္း (၂၀၀၉) ၌ ေဟာၾကားေတာ္မူအပ္ေသာ တရားေတာ္မ်ား။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))                        
        except IndexError as err:
            print('this line {}'.format(title.split('။')))     
        
        
        counter += 1
    
"""


