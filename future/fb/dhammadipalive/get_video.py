#!/usr/bin/env python
# coding=utf-8
data = [f.strip('\n') for f in open('raw_links.txt')]

#print(data)

for f in data:
    if 'videos' in f:
        try:
            #print(f)
            #print(f.split('/')[6])
            if f.split('/')[6] == "":
                print(f)
        except IndexError as e:
            pass
        #print(len(f.split('/')))
        #if f.split('/')[6] != "":
            #print(f.split('/'))
