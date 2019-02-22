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

one="ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား အမွတ္စဥ္ (၁)"
two=" ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား အမွတ္စဥ္ (၂)"
three=" ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား အမွတ္စဥ္ (၃)"
four=" ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား အမွတ္စဥ္ (၄)"
five=" ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား အမွတ္စဥ္ (၅)"
six=" အႏုေမာဒနာတရားေတာ္မ်ား"
seven=" တရားေတာ္မ်ား"


desc = {
	'one': (one, 1, 96),
	'two': (two, 97, 117),
	'three': (three, 118, 135),
	'four': (four, 136, 156),
	'five': (five, 157, 179),
	'six': (six, 180, 352),
	'seven': (seven, 353, 381),
	 }
     
'''
for dd in desc.items():
    
    for i in range(0, 467):
        #print(dd[1][0], 'test')
        if dd[1][1] <= i <= dd[1][2]:
            print(dd[1][0])
'''

with open('title.txt', 'w') as f:
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