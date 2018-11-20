# -*- coding: utf-8 -*-
import os
import sys
import shutil 
import collections 
import argparse

#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")

#print("This file path, relative to os.getcwd()")
#print(__file__ + "\n")

#print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
#print(full_path + "\n")


#print("This file directory and name")
path, filename = os.path.split(full_path)
#print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

# change the working directory with
os.chdir(path)


titles = [title.strip('\n') for  title in open('title.txt', 'r') if title != '\n']

print("total title => ",len(titles))
count = len(titles)
name = []
description = "ၾကာနီကန္ဆရာေတာ္ ဦးဇဠိလ ေဟာၾကားေတာ္မူေသာတရားေတာ္မ်ား \nsources from http://www.dhammaransi.com \n\t\t\t http://www.dhammadownload.com \n\t\t\t http://www.thitsarparamisociety.com"
for title in reversed(titles):
    counter = '{:03}'.format(count)
    #print(title)
    dict_title = {
                 "title": "{}".format(title),
                  "description": description,  
                   "id": "{}".format(counter)
                }
    name.append(dict_title)
    count -= 1
playlist = "ၾကာနီကန္ဆရာေတာ္ ဦးဇဠိလ ေဟာၾကားေတာ္မူေသာတရားေတာ္မ်ား"

parser = argparse.ArgumentParser(add_help=True, description="youtube upload script") 
parser.add_argument('--test', '-t', action='store_true', help='testing')
parser.add_argument('--upload', '-u', action='store_true', help='upload ')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')

args = parser.parse_args() 

if args.test:

    for key in reversed(name):

        file = '{}.mp4'.format(key['id'])
        test = []

        
        if os.path.isfile(file):
        
            title =  key['title']             
            print('{} --title="{}" --description="{}" --playlist="{}" {}.mp4'.format('youtube-upload', \
                title, key['description'], playlist, key['id']))            
            
        else:
            print('No file found to be uploaded', file)
            
elif args.upload:

    folder_name = 'finished'
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)    

    for key in reversed(name):

        file = '{}.mp4'.format(key['id'])
        
        if file in ['015.mp4', '021.mp4', '081.mp4', '085.mp4']:
            if os.path.isfile(file):
            
                title =  key['title']            
                
                if 0 == os.system('{} --title="{}" --description="{}" --playlist="{}" {}.mp4'.format('youtube-upload', \
                    title, key['description'], playlist, key['id'])):
                    print("Yes")
                    print("Moving file...")
                    shutil.move(file, 'finished/')
                    #os.remove(file)
                else:
                    print("No")
                    sys.exit(1)            
            else:
                print('No file found to be uploaded', file)
else:
    parser.print_help()
