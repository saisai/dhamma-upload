#!/usr/bin/env python
# coding=utf-8
# https://www.geeksforgeeks.org/python-difference-two-lists/
# https://www.techbeamers.com/python-difference-between-two-lists/
def Diff(li1, li2):
    return (list(set(li1) - set(li2))) 
    
working = [f.strip('\n') for f in open('working.txt', encoding='utf8')]
not_working = [f.strip('\n') for f in open('not_working_5.3.8.txt', encoding='utf8')]

#print(Diff(working, not_working))
for i in Diff(working, not_working):
    print(i)

#for w, nw in zip(working, not_working):
#    if w == nw:
#        print('same', w)
#    else:
#        print(w)
'''
seen = set()
for w in working:
    for nw in not_working:
        if w == nw:
            pass 
            #test = 1
            #print('same', w)
        else:
            if w not in seen or w != nw:
                #print(type(w))
                #print(w)
                seen.add(w)
                #print(w)
                
print(seen)                
'''                
