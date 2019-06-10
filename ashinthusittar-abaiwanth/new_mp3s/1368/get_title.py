#!/usr/bin/env python
# coding=utf-8

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))

    for i in mmlist:
        strmm += mm[i]

    return strmm

title = '၁၃၆၈-ခု ႏွစ္ တြင္ ပုိ႕ ခ် ေတာ္ မူ အပ္ ေသာ နံ႕သာျမိဳင္ ပါရာဇိကဏ္ ပထမပါရာဇိက၀ါက်'

for f in range(1, 100):
    fmt = '{:03d}.mp3'.format(f)
    print('{}|test|{}။{}'.format(fmt,change(f), title))