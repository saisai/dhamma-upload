# -*- coding: utf-8 -*-

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm

def mm_to_eng(num):
    
    mm_eng = {'၀':0,'၁':1,'၂':2,'၃':3, '၄':4, '၅':5, '၆':6,'၇':7,'၈':8,'၉':9}
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += str(i)

    return strmm

#print(get_new)
'''
titles = [title.strip('\n') for title in open('title.txt')]
ids = [title.strip('\n') for title in open('id.txt')]

with open('titlesss.txt', 'w') as f:
    #counter = 1
    for title, id in zip(titles, ids):    
        f.write('{}|{}|{}\n'.format(mm_to_eng(title.split('။')[0]), id, title))
        print(mm_to_eng(title.split('။')[0]), id, title)
        #try:
            #f.write('{}။{}\n'.format(change(counter), title.split('။')[1]))
        #except IndexError as err:
            #f.write('this line {}'.format(title.split('။')))     
        
        #print('{}။{}'.format(change(counter), title))        
        
        #counter += 1
'''
titles = [title.strip('\n') for title in open('new_file_test_today.txt')]


with open('no_time_id_title_test_today.txt', 'w') as f:
    for title in titles:    
        
        #print(mm_to_eng(title.split('။')[0]), id, title)
        print(mm_to_eng(title.split('|||')[2].split('။')[0]))
        f.write('{}|||{}|||{}|||{}\n'.format(mm_to_eng(title.split('|||')[2].split('။')[0]), title.split('|||')[1], title.split('|||')[0], title.split('|||')[2]))

    



