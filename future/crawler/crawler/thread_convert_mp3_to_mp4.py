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

file = sys.argv[0]

pathname = os.path.dirname(file)

running_from_path = os.path.abspath(pathname) + '/'

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

moved_mp3 = running_from_path + 'moved_mp3'

if not os.path.isdir(moved_mp3):
    os.mkdir(moved_mp3)
    
    
#threads = int(sys.argv[1])
#print(threads)


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, queue, images_count, image_path):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.images_count = images_count
        self.image_path = image_path
        

    def run(self):
        while True:
            # gets the url from the queue
            mp3file = self.queue.get()
            print(mp3file)
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, mp3file):
        """Download file"""
        if os.path.isfile(mp3file):
            
            #t_start = time.clock()
            #t_elapsed = time.clock() - t_start
            
            #print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

            format = mp3file.split('.')[0]
            print('counter' , format)
            info = mediainfo(mp3file)
            
            if len(info) > 0:            
                print(info, len(info), 'aa')
                seconds = float(info['duration'])            
                result = seconds / self.images_count
                plus_one = result
                command = "ffmpeg|-y|-r|1/{}|-start_number|1|-i|{}photo-%03d.jpg|-i|{}|-r|18|-pix_fmt|yuv420p|-c:a|aac|-s|320x240|{}{}.mp4".format(plus_one, self.image_path, mp3file, running_from_path, format)
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
    def __init__(self, convert_list, images_count, image_path, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.images_count = images_count
        self.image_path = image_path
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue, self.images_count, self.image_path)
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


def one(mp3s_count, threads):
    
    mp3s = [mp3 for mp3  in sorted(glob.glob(running_from_path + "*.mp3"), key=natural_keys)]
    
    #print(mp3s[:mp3s_count])
    
    images = [mp3 for mp3  in sorted(glob.glob(running_from_path + "images/*.jpg"), key=natural_keys)]
    convert_manager = ConvertManager(mp3s[:mp3s_count], len(images), running_from_path + 'images/', threads)
    convert_manager.begin_convert()
    
   

#def main(argv):
def thread_convert_mp3_to_mp4(threads):

    mp3s = [mp3 for mp3  in sorted(glob.glob(running_from_path+"*.mp3"), key=natural_keys)]
    aa = mp3s
    #print(aa)
    first = len(aa)
     


    print(first)
    
    one(first, threads)
    
    

    
    
    
   

#if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    #main()
    #  python filedownload.py -o ./tmp -i test.json
