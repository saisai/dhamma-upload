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

one="ျဗဟၼဝိဟာရနိေဒၵသ"
two="ျဗဟၼဝိဟာရနိေဒၵသ"
three="အာရုပၸနိေဒၵသ"
four="သမာဓိနိေဒၵသ"
five="ဣဒိၶဝိဓနိေဒၵသ"
six="အဘိညာနိေဒၵသ"
seven="ခႏၶနိေဒၵသ"
eight ="ဣျႏၵိယသစၥနိေဒၵသ"

desc = {
	'one': (one, 467, 545),
	'two': (two, 546, 557),
	'three': (three, 558, 620),
	'four': (four, 621, 689),
	'five': (five, 690, 730),
	'six': (six, 731, 768),
	'seven': (seven, 769, 832),
	'eight': (eight, 833, 913),
	 }
     
'''
for dd in desc.items():
    
    for i in range(0, 467):
        #print(dd[1][0], 'test')
        if dd[1][1] <= i <= dd[1][2]:
            print(dd[1][0])
'''

with open('title.txt', 'w') as f:
    counter = 467
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