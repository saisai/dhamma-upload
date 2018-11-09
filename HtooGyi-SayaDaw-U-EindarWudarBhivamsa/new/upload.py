# -*- coding: utf-8 -*-
import os
import sys
import shutil 
import collections 
import argparse
import json
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


name = []
with open("raw_json_title.txt") as json_file:
    data = json.load(json_file)
    name = json.loads(data)
    #print(type(results))
"""    
for key in name:
    print(key['title'])
    print(key['id'])
    print(key['description'])
    print(key['playlist'])
"""
parser = argparse.ArgumentParser(add_help=True, description="youtube upload script") 
parser.add_argument('--test', '-t', action='store_true', help='testing')
parser.add_argument('--upload', '-u', action='store_true', help='upload ')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')

args = parser.parse_args() 

upload_file_ext = 'mp4'
#upload_file_ext = 'wmv'

if args.test:

    #for key in reversed(name):
    for key in name:

        file = '{}.{}'.format(key['id'], upload_file_ext)
        test = []

        
        if os.path.isfile(file):
        
            title =  key['title']             
            print('{} --title="{}" --description="{}" --playlist="{}" {}.{}'.format('youtube-upload', \
                title, key['description'], key['playlist'], key['id'], upload_file_ext))            
            
        else:
            print('No file found to be uploaded', file)
            
elif args.upload:

    folder_name = 'finished'
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)    

    #for key in reversed(name):
    for key in name:

        file = '{}.{}'.format(key['id'], upload_file_ext)
                
        if os.path.isfile(file):
        
            title =  key['title']            
            
            if 0 == os.system('{} --title="{}" --description="{}" --playlist="{}" {}.{}'.format('youtube-upload', \
                title, key['description'], key['playlist'], key['id'], upload_file_ext)):
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
