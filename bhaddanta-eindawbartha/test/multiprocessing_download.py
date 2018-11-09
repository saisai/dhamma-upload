#!/usr/bin/env python
# coding=utf-8
import sys
import os
import time
from threading import Thread
from multiprocessing import Process
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


    
    
#threads = int(sys.argv[1])
#print(threads)
images = 3

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
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

def worker(arg):
    print(arg.description)
    
queue = PriorityQueue()
queue.put(Job(3, "Low"))
queue.put(Job(2, "Mid"))
queue.put(Job(1, "Important"))


if __name__ == '__main__':
    
    while not queue.empty():
        p = Process(target=worker, args=(queue.get(),))
        p.start()
        p.join()
        #print(queue.get())