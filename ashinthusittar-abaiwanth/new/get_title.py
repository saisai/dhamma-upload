#!/usr/bin/env python
# coding=utf-8

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm

num = 1
for i in range(2, 50):
    fmt = '{:2d}.mp3'.format(i)
    print('{}|အလုပ္ေပးတရားေတာ္ ({})|အလုပ္ေပးတရားေတာ္ ({})'.format(fmt,change(num), change(num)))
    
    num += 1
