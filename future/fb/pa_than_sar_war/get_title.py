#!/usr/bin/env python
# coding=utf-8
def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))

    for i in mmlist:
        strmm += mm[i]

    return strmm

for i in range(1, 56):
    
    t = ' ပ႒ာန္းစာဝါ'
    print('{:03d}.mp3|test|({}) {}'.format(i, change(i), t))