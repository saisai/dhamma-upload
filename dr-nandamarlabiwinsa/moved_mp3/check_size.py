
import glob
import subprocess
import os 
import sys

empty_files = []
for i in sorted(glob.glob('*.mp3')):
    if os.stat(i).st_size ==0:
        print(i, os.stat(i).st_size ==0 )
        empty_files.append(i)
        

lines = [line.strip('\n') for line in open('titles_links.txt', 'r')]
#print(lines)
#count = 1

for line in lines:
    filename = line.split('|')[0]
    url = line.split('|')[1]
    if filename in empty_files:
        print(filename)
        print(url)
        command = 'wget -c -O {} "{}"'.format(filename, url)
        os.system(command)
        
        
        #command = 'wget|-c|-O|{}|"{}"'.format(filename, url)
        #print(command)
        #completed = subprocess.run(command.split('|'))
        #print('returncode:', completed)        
        
