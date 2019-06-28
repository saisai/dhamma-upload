#!/usr/bin/env python
# coding=utf-8

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))

    for i in mmlist:
        strmm += mm[i]

    return strmm

title = 'ရွဴကြက္အမွတ္ (၁)'

for f in range(1, 17):
    fmt = '{:03d}.mp3'.format(f)
    print('{}|test|{}။{}'.format(fmt,change(f), title))