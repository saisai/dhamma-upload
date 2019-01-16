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
