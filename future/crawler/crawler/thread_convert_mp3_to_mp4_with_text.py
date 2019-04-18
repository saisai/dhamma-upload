# coding=utf-8
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json
import re 

import glob
from pydub.utils import mediainfo
import subprocess
import datetime
import os
import shutil
import functools


from PIL import Image, ImageDraw, ImageFont


from .helper import natural_keys



file = sys.argv[0]

pathname = os.path.dirname(file)

running_from_path = os.path.abspath(pathname) + '/'

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

moved_mp3 = running_from_path + 'moved_mp3'

if not os.path.isdir(moved_mp3):
    os.mkdir(moved_mp3)
    
    
class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, queue, images_count, image_path, output_path):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.images_count = images_count
        self.image_path = image_path
        self.output_path = output_path
        

    def run(self):
        while True:
            # gets the url from the queue
            mp3file = self.queue.get()
            print(mp3file)
            # download the file
            #print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()

    def add_text_to_image(self, folder, text):
    
        # get the images from images folder 
        
        
        img = Image.open("photo-003.jpg")
        #width, height = img.size
        width, height = img.size
        x1, y1 = img.size
        height = y1

        y1 = y1//2 + (y1 + 350)
        yy = y1//2 + 50


        sentence = u"၁။ လူငယ်တို့အမေး ယနေ့ခေတ်ဘာသာရေး"
        #choose a font
        fnt = ImageFont.truetype('Thanlwin-Regular.ttf', 30)
        #img = Image.new('photo-001.jpg', (x1, y1), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        #find the average size of the letter
        sum = 0
        for letter in sentence:
          sum += d.textsize(letter, font=fnt)[0]
        average_length_of_letter = sum/len(sentence)
        print(average_length_of_letter)
        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''
        #add some line breaks
        for letter in sentence:
          if(letter == '-'):
            fresh_sentence += '\n\n' + letter
          elif(incrementer < number_of_letters_for_each_line):
            fresh_sentence += letter
          else:
            if(letter == ' '):
              #fresh_sentence += '\n'
              fresh_sentence += ' '
              incrementer = 0
            else:
              fresh_sentence += letter
          incrementer+=1
          #print(fresh_sentence)
        #render the text in the center of the box
        dim = d.textsize(fresh_sentence, font=fnt)
        #dim = d.textsize(sentence, font=fnt)
        x2 = dim[0]
        y2 = dim[1]
        qx = (x1/2 - x2/2)
        qy = (y1/2-y2/2)



        x, y = (width-200, height-100)
        xx, yy = (width-400, height-100)
        w, h = d.textsize(sentence, font=fnt)
        d.rectangle((0, y, x + w, y + h + 50), fill='black')
        d.text((qx,y+30), fresh_sentence, align="center",fill='white', font=fnt)

        img.save('quote3333.png')
        

    def download_file(self, mp3file):
        """Download file"""
        if os.path.isfile(mp3file):
            result = mp3file.split('/')
            formatter = '/'.join(result[:-1]) + '/' + result[-1].split('.')[0]
            
            print('counter' , formatter)
            
            
            info = mediainfo(mp3file)
            
            if len(info) > 0:            
                #print(info, len(info), 'aa')
                #format = self.output_path + format
                #print('aa test', format)
                seconds = float(info['duration'])            
                result = seconds / self.images_count
                plus_one = result
                command = "ffmpeg|-y|-r|1/{}|-start_number|1|-i|{}photo-%03d.jpg|-i|{}|-r|18|-pix_fmt|yuv420p|-c:a|aac|-s|320x240|{}.mp4".format(plus_one, self.image_path, mp3file, formatter)
                #command = "ffmpeg|-y|-r|1/{}|-start_number|1|-i|{}photo-%03d.jpg|-i|{}|-r|18|-c:a|aac|{}.mp4".format(plus_one, self.image_path, mp3file, format)
                print(command)
                completed = subprocess.run(command.split('|'))
                print('returncode:', completed)
                print(completed.returncode)
                if completed.returncode == 0:
                    print('Moving file {} .....'.format(mp3file))
                    shutil.move(mp3file, moved_mp3)
        else:
            print('No file found', mp3file)
        
            #else:
            #    print("* Thread: {} Bad URL: {}".format(self.name, url))


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, convert_list, running_from_path, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.running_from_path = running_from_path

        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue, running_from_path)
            t.setDaemon(True)
            t.start()

        # load the queue from the download dict
        for mp3file in self.convert_list:
            queue.put(mp3file)

        # wait for the queue to finish
        queue.join()

        return

parser = argparse.ArgumentParser()
parser.usage = "pydownload.py -o <OutputDirectory> -i <JSONinputfile> -f <url1,url2,url3>"
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--ifile')
parser.add_argument('-f', '--flist')

'''
def one(mp3s_count, threads):
    
    mp3s = [mp3 for mp3  in sorted(glob.glob(running_from_path + "*.mp3"), key=natural_keys)]
    
    #print(mp3s[:mp3s_count])
    
    images = [mp3 for mp3  in sorted(glob.glob(running_from_path + "images/*.jpg"), key=natural_keys)]
    convert_manager = ConvertManager(mp3s[:mp3s_count], len(images), running_from_path + 'images/', running_from_path, threads)
    convert_manager.begin_convert()
'''    
   

#def main(argv):
def thread_convert_mp3_to_mp4_with_text(file_in, threads):
    
    file_in = running_from_path + file_in
    files = [f.strip('\n') for f in open(file_in)]
    mp3s = [mp3 for mp3  in sorted(files, key=natural_keys)]
    #aa = mp3s
    #print(aa)
    #first = len(aa)

    #print(first)
    
    #one(first, threads)  
    
    convert_manager = ConvertManager(mp3s, running_from_path, threads)
    convert_manager.begin_convert()    


