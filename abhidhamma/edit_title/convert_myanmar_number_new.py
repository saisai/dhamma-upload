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
    
def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm    


titles = [title.strip('\n') for title in open('new_file_test_today_edit.txt') if len(title) > 2]

count = 1
with open('final_result.txt', 'w') as f:
    for title in titles:    
        
        #print(title.split('|||')[2].split('။')[0], title.split('|||')[2].split('။')[1])
        print('{}|||{}|||{}။{}'.format(title.split('|||')[0], title.split('|||')[1], change(count), title.split('|||')[2].split('။')[1]))
        f.write('{}|||{}|||{}။{}\n'.format(title.split('|||')[0], title.split('|||')[1], change(count), title.split('|||')[2].split('။')[1]))
        #print(mm_to_eng(title.split('။')[0]), id, title)
        #print(mm_to_eng(title.split('|||')[2].split('။')[0]))
        #f.write('{}|||{}|||{}|||{}\n'.format(mm_to_eng(title.split('|||')[2].split('။')[0]), title.split('|||')[1], title.split('|||')[0], title.split('|||')[2]))
        
        count += 1

    



