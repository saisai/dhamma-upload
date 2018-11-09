#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
from threading import Thread
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

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)


    
    
threads = int(sys.argv[1])
print(threads)
images = 3

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
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
            mp3file = self.queue.get()
            print(type(mp3file), mp3file.description, 'aa')
            print(type(mp3file))
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, mp3file):
        """Download file"""
        #if os.path.isfile(mp3file):
            
        t_start = time.clock()
        t_elapsed = time.clock() - t_start
        
        print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

        filename = (mp3file.description.split('|')[0])
        url = (mp3file.description.split('|')[1])
        command = 'wget -c -O {} {}'.format(filename, url)
        os.system(command)        
        """
        command = 'wget|-c|-O|{}|"{}"'.format(filename, url)
        print(command)
        completed = subprocess.run(command.split('|'))
        print('returncode:', completed)
        print(completed.returncode)
        """ 
        #else:
            #print('No file found', mp3file)
        
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

        # load the queue from the download dict
        #for mp3file in self.convert_list:
            #queue.put(mp3file)
        
        for mp3 in self.convert_list:
            #print(int(mp3.split('|')[0].split('.')[0]))
            queue.put(Job((int(mp3.split('|')[0].split('.')[0])), mp3))            

        # wait for the queue to finish
        queue.join()

        return

parser = argparse.ArgumentParser()
parser.usage = "pydownload.py -o <OutputDirectory> -i <JSONinputfile> -f <url1,url2,url3>"
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--ifile')
parser.add_argument('-f', '--flist')

#def main(argv):
def main():
    
    mp3s = [f.strip('\n') for f in open('titles_links.txt')]
    """
    q = PriorityQueue()
    for mp3 in mp3s:
        print(int(mp3.split('|')[0].split('.')[0]))
        q.put(Job((int(mp3.split('|')[0].split('.')[0])), mp3))
    """    
    convert_manager = ConvertManager(mp3s, threads)
    convert_manager.begin_convert()
    
   

if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    main()
    #  python filedownload.py -o ./tmp -i test.json
