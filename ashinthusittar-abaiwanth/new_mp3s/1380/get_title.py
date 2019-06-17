#!/usr/bin/env python
# coding=utf-8

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))

    for i in mmlist:
        strmm += mm[i]

    return strmm


title = '၁၃၈၀-ခု ႏွစ္ တြင္ ပုိ႕ ခ် ေတာ္ မူ အပ္ ေသာ က်မ္းရင္းသုံးက်မ္းလုံးဆုိင္ရာ ဓမၼာစရိယ အေျခခံ'

for f in range(1, 200):
    fmt = '{:03d}.mp3'.format(f)
    print('{}|test|{}။{}'.format(fmt,change(f), title))