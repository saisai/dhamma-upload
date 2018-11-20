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
titles = [title.strip('\n\n\n') for title in open('titles.txt')]

with open('title.txt', 'w') as f:
    counter = 257
    for title in titles:    
        try:
            f.write('{}။{}\n'.format(change(counter), title.split('။')[1]))
        except IndexError as err:
            f.write('this line {}'.format(title.split('။')))     
        
        #print('{}။{}'.format(change(counter), title))        
        
        counter += 1


with open('description.txt', 'w') as f:
    counter = 257
    for title in titles:
    
        try:
            #if counter <= 20:
            location = "အလုပ္ေပးတရာေတာ္မ်ား"
            f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))
            """
            elif counter <= 66:
                location = "(၂၀၁၂)ခုနွစ္၊ ဇြန္လ (၂၄)ရက္မွ ဇူလိုင္လ (၃)ရက္ေန႔အထိ ဆရာေတာ္ ဦးဣႏၵာဝုဓာ ဘိဝံသ (ထူးႀကီး ဆရာေတာ္) ေဟာၾကားဆံုးမေတာ္မူခဲ့ေသာ ခႏၶာဥာဏ္ေရာက္ ဒိဌိျဖဳတ္ ပဋိစၥသမုပါဒ္ သစၥာေလးပါး တရားေတာ္မ်ား (၂၀)ပုဒ္"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))        
            elif counter <= 86:
                location = "ေအာင္ပန္းၿမိဳ႕ မိုးကုတ္ဝိပႆနာတရားစဥ္ႏွင့္ လုပ္ငန္းစဥ္ျပန္႕ပြားေရး အဖြဲ႕ခြဲ အမွတ္္ (၃၂၉)မွ က်င္းပျပဳလုပ္အပ္ေသာ (၂၂)ႀကိမ္ေျမာက္ မိုးကုတ္ဝိပႆနာ (၁၀)ရက္တရားစခန္းပြဲ ၌ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))                        
            else:
                location = "ဟသၤာတၿမိဳ႔ ၊ မိုးကုတ္၀ိပႆနာရိပ္သာ၊ (၇) ရက္တရားစခန္း (၂၀၀၉) ၌ ေဟာၾကားေတာ္မူအပ္ေသာ တရားေတာ္မ်ား။"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))            
            """
        except IndexError as err:
            print('this line {}'.format(title.split('။')))     
        
        
        counter += 1
    



