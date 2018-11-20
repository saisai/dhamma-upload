# coding=utf-8

import subprocess
import os 
#with open('dl.txt', 'r') as f:
#    print(f.readlines())

#lines = [line.rstrip('\n') for line in open('dl_links.txt')]
lines = [line.rstrip('\n') for line in open('new_links.txt')]

for line in lines:
    format_count = line.split(',')[0].split('/')[-2]
    
    if not os.path.isfile(format_count + '.mp4'):    
        print(format_count)
        
        format_count = line.split(',')[0].split('/')[-2]
        line= line.split(',')[0].replace('"', '')
        command = 'youtube-dl|-c|-o|{}.%(ext)s|{}'.format(format_count, line)
        print(command.split('|'))
        completed = subprocess.run(command.split('|'))
        print('returncode:', completed)      
        
    '''
    print(line.split(',')[0].replace('"', ''))
    print(line.split(',')[0].split('/')[-2])
    format_count = line.split(',')[0].split('/')[-2]
    #line= line.split(',')[0]
    line= line.split(',')[0].replace('"', '')
    command = 'youtube-dl|-c|-o|{}.%(ext)s|{}'.format(format_count, line)
    print(command.split('|'))
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    '''

'''
format_count = '218588348615440'
line= 'https://www.facebook.com/WinNaingKyawfromYangon/videos/218588348615440'
command = 'youtube-dl|-o|{}.%(ext)s|{}'.format(format_count, line)
print(command)
completed = subprocess.run(command.split('|'))
print('returncode:', completed)
'''
