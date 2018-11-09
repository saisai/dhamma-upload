#!/usr/bin/env python
# coding=utf-8
import glob
from pydub.utils import mediainfo
import subprocess
import datetime
import os
import shutil

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

moved_mp3 = 'moved_mp3'

if not os.path.isdir(moved_mp3):
    os.mkdir(moved_mp3)

#counter = 46
for i in sorted(glob.glob("*.mp3")):
    print(i)
    format = i.split('.')[0]
    print('counter' , format)
    info = mediainfo(i)
    seconds = float(info['duration']) 
    #print(seconds)
    #print(str(datetime.timedelta(seconds=seconds)))
    #print(minutes)
    result = seconds / 28
    #print(result)
    #print(round(result))
    #print(result * 8)
    #format = '{:03}'.format(counter)
    #print(format)
    # plus one second 
    #plus_one = round(result) + 1 
    #plus_one = round(result) 
    plus_one = result
    
    
    #command = "ffmpeg|-y|-framerate|1/{}|-start_number|1|-i|photo-%03d.jpg|-i|{}|-c:v|libx264|-r|30|-pix_fmt|yuv420p|-c:a|aac|-strict|experimental|-s|320x240|-shortest|{}.mp4".format(plus_one, i , format)
    
    
    command = "ffmpeg|-y|-r|1/{}|-start_number|1|-i|photo-%03d.jpg|-i|{}|-r|18|-pix_fmt|yuv420p|-c:a|aac|-s|320x240|{}.mp4".format(plus_one, i , format)
    print(command)
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    
    print('Moving file {} .....'.format(i))
    shutil.move(i, moved_mp3)
    
    #counter += 1
