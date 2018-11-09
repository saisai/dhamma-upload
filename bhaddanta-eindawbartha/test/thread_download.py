#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
import threading
#from threading import Thread, Event, Lock 
from queue import Queue, PriorityQueue
import argparse
import binascii
import json
import re 
import functools

import glob
from pydub.utils import mediainfo
#import subprocess
import datetime
import os
import shutil
import signal
import shlex
from subprocess import Popen, PIPE

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    #args = shlex.split(cmd)
    args = cmd.split('|')
    #print(args, 'asdf')
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err
    
    
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

class Converter(threading.Thread):
    """Downloader class - read queue and downloads each file in succession"""
    #lock = Lock()
    #count = 0
    def __init__(self, queue):

        threading.Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        
        #self.count = 0
        
        

    def run(self):
    
        
        
        while True:           
        #global count
        
        
        # gets the url from the queue
            mp3file = self.queue.get()
            print(type(mp3file), mp3file.description, 'aa')
            print(type(mp3file))
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            
            # send a signal to the queue that the job is done
            #print(Converter.count, 'asdf')
            self.queue.task_done()
            
            
        
        
    def download_file(self, mp3file):
        """Download file"""
        #if os.path.isfile(mp3file):
            
        t_start = time.clock()
        t_elapsed = time.clock() - t_start
        
        print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

        filename = (mp3file.description.split('|')[0])
        url = (mp3file.description.split('|')[1])
        #command = 'wget -c -O {} {}'.format(filename, url)
        #os.system(command)       
        
        
        command = 'wget|--no-check-certificate|-c|-O|{}|{}'.format(filename, url)
        print(command)
        #completed = subprocess.run(command.split('|'))
        #PARAMETER = '--no-check-certificate'
        #subprocess.call(['wget', '-O', OUTPUT, JIRA_URL, PARAMETER])
        exitcode, out, err = get_exitcode_stdout_stderr(command)
        print('exitcode', exitcode)
        print('output', out)
        print('error', err)
        #print('returncode:', completed)
        #print(completed.returncode)
        #if exitcode != 0:
            #os.killpg(0, signal.SIGKILL)  
            
        if exitcode == 0:            
            print("Yes")
            print("Moving file...")
            #shutil.move(mp3file, 'finished/')
        elif exitcode == 3:
            print(threading.get_ident(), 'current_thread_id...')
            print('Killing current thread_id', threading.get_ident())
            #signal.pthread_kill(threading.get_ident(), signal.SIGKILL)
            signal.pthread_kill(threading.get_ident(), signal.SIGKILL)
            #os.killpg(threading.get_ident(), signal.SIGKILL)
        elif exitcode == 8:
            print(threading.get_ident(), 'current_thread_id...')
            print('Killing current thread_id', threading.get_ident())
            #signal.pthread_kill(threading.get_ident(), signal.SIGKILL)
            signal.pthread_kill(threading.get_ident(), signal.SIGKILL)
            #os.killpg(threading.get_ident(), signal.SIGKILL)        
        #else:
            #os.killpg(0, signal.SIGKILL)            
        
            #os._exit(1)
            
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
