#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup


#data = open('data.txt').read()
data = [f.strip('\n') for f in open('data.txt')]

def test():
    
    def text(line):
        breaker = 'https' not in line
        ext_desc = ""
        if breaker == True:
            ext_desc = line
        return (breaker, ext_desc)
        
       
    def get_line(line):
        breaker = 'https' in line
        ext_desc = ""
        if breaker != False:
            ext_desc = line
        return ext_desc

    count = 1        
    for f in data:
        tmp = ""
        #asdf =""
        fmt = '{:03d}.mp3'.format(count)
        if text(f)[0] == True:
            tmp = text(f)[1]
            asdf = tmp
        else:
            print('{}|{}|{}'.format(fmt, f, asdf))
            count += 1
            
        
            
        
        

test()    
#soup = BeautifulSoup(data, 'html.parser')

#for f in soup.find_all('a'):
    #print(f.get('href'))
