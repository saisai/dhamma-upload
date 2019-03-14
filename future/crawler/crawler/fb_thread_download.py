#!/usr/bin/env python
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


file = sys.argv[0]

pathname = os.path.dirname(file)

running_from_path = os.path.abspath(pathname) + '/'


class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, output_path, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.output_path = output_path
        

    def run(self):
        while True:
            # gets the url from the queue
            mp3file = self.queue.get()
            print(type(mp3file))
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, line):
        """Download file"""
        print(line)
        #format_count = line.split(',')[0].split('/')[-2]
        format_count = line.split('|')[0]
        
        #if not os.path.isfile(format_count + '.mp4'):    
        if not os.path.isfile(format_count):    
            print(format_count)
            
            format_count = line.split('|')[0].split('.')[0]
            line= line.split('|')[1]
            command = 'youtube-dl|-c|-o|{}{}.%(ext)s|{}'.format(self.output_path, format_count, line)
            print(command.split('|'))
            completed = subprocess.run(command.split('|'))
            print('returncode:', completed)            
            
            '''
            format_count = line.split(',')[0].split('/')[-2]
            line= line.split(',')[0].replace('"', '')
            command = 'youtube-dl|-c|-o|{}{}.%(ext)s|{}'.format(self.output_path, format_count, line)
            print(command.split('|'))
            completed = subprocess.run(command.split('|'))
            print('returncode:', completed)
            '''
 


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, output_path, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.output_path = output_path
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(self.output_path, queue)
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

#def main(argv):
def download_fb(file_in, threads):

    file_in = running_from_path + file_in
    
    mp3s = [f.strip('\n') for f in open(file_in)]
    
    #convert_manager = ConvertManager(running_from_path, reversed(mp3s), threads)
    convert_manager = ConvertManager(running_from_path, mp3s, threads)
    convert_manager.begin_convert()
    
   

#if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    #main()
    #  python filedownload.py -o ./tmp -i test.json
