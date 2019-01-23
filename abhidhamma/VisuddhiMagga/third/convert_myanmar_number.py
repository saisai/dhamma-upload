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

one="ပညာဘူမိ နိေဒၵသ"
two="ဒိ႒ိ ဝိသုဒၶိ နိေဒၵသ"
three="ကခၤါဝိတရဏ ဝိသုဒၶိ နိေဒၵသ"
four=" မဂၢါမဂၢဉာဏဒႆနဝိသုဒၶိ နိေဒၵသ"
five="ပဋိပဒါဉာဏဒႆနဝိသုဒၶိ နိေဒၵသ"
six="ဉာဏဒႆနဝိသုဒၶိ နိေဒၵသ"

desc = {
	'one': (one, 914, 1166),
	'two': (two, 1167, 1208),
	'three': (three, 1209, 1229),
	'four': (four, 1230, 1288),
	'five': (five, 1289, 1341),
	'six': (six, 1342, 1368),	
	 }
     
'''
for dd in desc.items():
    
    for i in range(0, 467):
        #print(dd[1][0], 'test')
        if dd[1][1] <= i <= dd[1][2]:
            print(dd[1][0])
'''

with open('title.txt', 'w') as f:
    counter = 914
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