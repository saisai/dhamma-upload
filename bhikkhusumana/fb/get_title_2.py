#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
from selenium.webdriver import FirefoxOptions
import requests
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json


import subprocess
import datetime

import shutil

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

moved_mp3 = 'moved_mp3'

#if not os.path.isdir(moved_mp3):
#    os.mkdir(moved_mp3)
    
#images = 23

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm

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

    def __init__(self, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        

    def run(self):
        while True:
            # gets the url from the queue
            mp3file = self.queue.get()
            # download the file
            #print("* Thread {} - processing URL".format(self.name))
            self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()


    def download_file(self, mp3file):
        """Get title from url"""
        
        #files = [f.strip('\n') for f in open('new_urltext_upload.txt', 'r')]    
        #print(files)
        #print(mp3file)
        
        
        
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=opts, executable_path=r'/e/geckodriver/geckodriver.exe')
        #driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
        #driver = webdriver.Firefox(firefox_options=opts)
        driver.get(mp3file)
        #print(driver.title)
        #print(driver)
        html = driver.page_source
        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        
        
        
        with open('new_urltext_upload.txt', 'a') as f:
            print(mp3file)
            try:

                f.write('{}|{}'.format(mp3file.split('/')[-2], soup.find('div', attrs={'class': '_5pbx userContent _3576'}).get_text() ))
                f.write('\n')
                f.flush()
            except AttributeError as err:
                #f.write('{')
                f.write('{}|{}'.format(mp3file.split('/')[-2], 'NoneType'))
                f.write('\n')
                f.flush()        
                # AttributeError: 'NoneType' object has no attribute 'get_text'
                
        
            #print(soup.find('div', attrs={'class': '_5pbx userContent _3576'}).get_text())        
        
        driver.close()        
        

        


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(queue)
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
def main():
    
    
    newmp3s = [f.strip('\n').replace('"', '') for f in open('links.txt', 'r')]
    #print(newmp3s)
    convert_manager = ConvertManager(reversed(newmp3s), 1)
    convert_manager.begin_convert()
    
   

if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    main()
    #  python filedownload.py -o ./tmp -i test.json