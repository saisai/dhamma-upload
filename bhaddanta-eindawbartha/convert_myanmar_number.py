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
    counter = 1
    for title in titles:    
        try:
            f.write('{}။{}\n'.format(change(counter), title.split('။')[1]))
        except IndexError as err:
            f.write('this line {}'.format(title.split('။')))     
        
        #print('{}။{}'.format(change(counter), title))        
        
        counter += 1


with open('description.txt', 'w') as f:
    counter = 1
    for title in titles:
    
        try:
            location = " "
            f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))                                      
            """
            if counter <= 41:
                location = "တရားေတာ္မ်ား"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))                              
            else:
                location = "ဓမၼဂုဏ္ရည္ဆရာေတာ္ MP3 တရားမ်ား စုစည္းမွဳ"
                f.write('{}။{}|{}\n'.format(change(counter), title.split('။')[1], location))  
            """
        except IndexError as err:
            print('this line {}'.format(title.split('။')))     
        
        
        counter += 1
    



