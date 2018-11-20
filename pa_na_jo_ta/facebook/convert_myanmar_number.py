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
titles = [title.strip('\n\n\n') for title in open('new_edited_titles.txt')]

with open('title.txt', 'w') as f:
    counter = 1
    for title in reversed(titles):
        """
        try:
            #print(title.split('|')[0], title.split('|')[2].split('။')[1])
            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
            #f.write('{}။{}\n'.format(change(counter), title.split('|').split('။')[1]))
        except IndexError as err:
            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2]))
            #f.write('this line {}'.format(title.split('။')))     
        """
        cc = '{:03d}'.format(counter)
        print(cc)
        print('{}။{}'.format(change(cc), title))        
        f.write('{}။{}\n'.format(change(cc), title))        
        
        counter += 1
