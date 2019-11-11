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

    def __init__(self, queue, folder):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.folder = folder
        

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


    def download_file(self, mp3file):
        """Download file"""

            
        #t_start = time.clock()
        #t_elapsed = time.clock() - t_start
        #perf_counter
        #t_start = time.perf_counter()
        #t_elapsed = time.perf_counter() - t_start        
        #print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

        filename = (mp3file.split('|')[0])
        url = (mp3file.split('|')[1])
        

        
        command = "wget|-c|--no-check-certificate|-O|{}|{}".format(self.folder+filename, url)
        print(command)
        completed = subprocess.run(command.split('|'))
        print('returncode:', completed)
        


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, folder, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.folder = folder
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue, self.folder)
            t.setDaemon(True)
            t.start()

        # load the queue from the download dict
        for mp3file in self.convert_list:
            queue.put(mp3file)

        # wait for the queue to finish
        queue.join()

        return


def thread_download(file_in, threads=1):

    file_in = running_from_path + file_in
    
    mp3s = [f.strip('\n') for f in open(file_in, encoding='utf8')]

    convert_manager = ConvertManager(running_from_path, mp3s, threads)
    convert_manager.begin_convert()
    
   


