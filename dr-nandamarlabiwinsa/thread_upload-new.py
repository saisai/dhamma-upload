#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
from threading import Thread, Event
from queue import Queue, PriorityQueue
import argparse
import binascii
import json
import re 
import functools

import glob
from pydub.utils import mediainfo
import subprocess
import datetime
import os
import shutil
import signal


full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

@functools.total_ordering
class Job:

    def __init__(self, priority, description, title, playlist):
        self.priority = priority
        self.description = description
        self.title = title
        self.playlist = playlist
        #print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue

    def run(self):
        while True:
            # gets the url from the queue
            getObj = self.queue.get()
            mp3file = str('{:03}'.format(getObj.priority)) + '.mp4'
            description = getObj.description
            title = getObj.title
            playlist = getObj.playlist            
            
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file, description, title, playlist)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, mp3file, description, title, playlist):
        """Download file"""
        if os.path.isfile(mp3file):
        
            print(mp3file, 'uploading...')           
            
            if 0 == os.system('{} --title="{}" --description="{}" --playlist="{}" {}'.format('youtube-upload', \
                title, description, playlist, mp3file)):
                print("Yes")
                print("Moving file...", mp3file)
                shutil.move(mp3file, 'finished/')
            else:
                os.killpg(0, signal.SIGKILL)         
                
            os.killpg(0, signal.SIGKILL)    
            
        else:
            print('No file found', mp3file)
        
            #else:
            #    print("* Thread: {} Bad URL: {}".format(self.name, url))


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        #queue = Queue()
        queue = PriorityQueue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue)
            t.setDaemon(True)
            t.start()


        for key in self.convert_list:
            #print(int(mp3.split('|')[0].split('.')[0]))
            #queue.put(Job((int(mp3.split('|')[0].split('.')[0])), mp3))            
            queue.put(Job(int(key['id']),  key['description'], key['title'], key['playlist']))            

        # wait for the queue to finish
        queue.join()

        return

parser = argparse.ArgumentParser()
parser.usage = "pydownload.py -o <OutputDirectory> -i <JSONinputfile> -f <url1,url2,url3>"
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--ifile')
parser.add_argument('-f', '--flist')

#def main(argv):
def main(threads):
    
    #mp3s = [f.strip('\n') for f in open('titles_links.txt')]
    
    mp3s = []
    with open("raw_json_title.txt") as json_file:
        data = json.load(json_file)
        mp3s = json.loads(data)    

    
    convert_manager = ConvertManager(mp3s, threads)
    convert_manager.begin_convert()
    
parser = argparse.ArgumentParser(add_help=True, description="youtube upload script") 
parser.add_argument('--test', '-t', action='store_true', help='testing')
parser.add_argument('--upload', '-u', action='store_true', help='upload ')
parser.add_argument('--threads', '-td', type=int, help='How many threads you want to upload')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')

args = parser.parse_args()    

#threads = int(sys.argv[1])
#print(threads)

if __name__ == "__main__": 
    upload_file_ext = 'mp4'
    if args.test:
        
        mp3s = []
        with open("raw_json_title.txt") as json_file:
            data = json.load(json_file)
            mp3s = json.loads(data)
        
        for key in mp3s:
            file = '{}.{}'.format(key['id'], upload_file_ext)
            if os.path.isfile(file):
            
                title =  key['title']             
                print('{} --title="{}" --description="{}" --playlist="{}" {}.{}'.format('youtube-upload', \
                    title, key['description'], key['playlist'], key['id'], upload_file_ext))            
                
            else:
                print('No file found to be uploaded', file)            
        
    elif args.upload and args.threads:
        print(parser.parse_args())
        print(args.threads)
        main(args.threads)
    else:
        parser.print_help()        
    #  python filedownload.py -o ./tmp -i test.json
