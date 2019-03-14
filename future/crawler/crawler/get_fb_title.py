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


file = sys.argv[0]

pathname = os.path.dirname(file)

running_from_path = os.path.abspath(pathname) + '/'


class Converter(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, file_out, finished, driver, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.driver = driver
        self.file_out = file_out
        self.finished = finished
        

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
        if not os.path.isfile(self.finished):
            lines = []
        else:
            lines = [f.strip('\n').split('|')[1] for f in open(self.finished, 'r')]
        
        
        if mp3file.split('|')[1] in lines:
            pass
        else:       
        
            exec_path = r'%s' % self.driver
            
            opts = FirefoxOptions()
            opts.add_argument("--headless")
            driver = webdriver.Firefox(firefox_options=opts, executable_path=exec_path)
            #driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
            #driver = webdriver.Firefox(firefox_options=opts)
            driver.get(mp3file.split('|')[1])
            #print(driver.title)
            #print(driver)
            html = driver.page_source
            
            soup = BeautifulSoup(html, 'html.parser')
            
            
            
            with open(self.file_out, 'a') as f:
                print(mp3file)
                try:

                    f.write('{}|{}|{}'.format(mp3file.split('|')[0], mp3file.split('|')[1].split('/')[-2], soup.find('div', attrs={'class': '_5pbx userContent _3576'}).get_text() ))
                    f.write('\n')
                    f.flush()
                except AttributeError as err:
                    #f.write('{')
                    f.write('{}|{}|{}'.format(mp3file.split('|')[0], mp3file.split('|')[1].mp3file.split('/')[-2], 'NoneType'))
                    f.write('\n')
                    f.flush()        
                    # AttributeError: 'NoneType' object has no attribute 'get_text'
                    
            
                #print(soup.find('div', attrs={'class': '_5pbx userContent _3576'}).get_text())        
            
            driver.close()
            
            with open(self.finished, 'a') as fd:
                fd.write(mp3file)
                fd.write('\n')
                fd.flush()
        

        


class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, file_out, finished, driver, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.driver = driver
        self.file_out = file_out
        self.finished = finished
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(self.file_out, self.finished, self.driver, queue)
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
def get_fb_title(file_in, file_out, finished, driver):

    file_in = running_from_path + file_in
    file_out = running_from_path + file_out
    finished = running_from_path + finished
    driver = running_from_path + driver
    
    
    newmp3s = [f.strip('\n').replace('"', '') for f in open(file_in, 'r')]
    #print(newmp3s)
    #convert_manager = ConvertManager(file_out, finished, driver, reversed(newmp3s), 1)
    convert_manager = ConvertManager(file_out, finished, driver, newmp3s, 1)
    convert_manager.begin_convert()


def rearrange_urls(file_in, file_out):    

    file_in = running_from_path + file_in
    file_out = running_from_path + file_out
    
    newmp3s = [f.strip('\n').replace('"', '') for f in open(file_in, 'r')]
    
    
    with open(file_out, 'w') as f:
        count = 1        
        for line in reversed(newmp3s):
            counter = '{:03d}'.format(count)
            f.write('{}.mp4|{}'.format(counter, line))
            f.write('\n')
            f.flush()
            
            count += 1 
    
    
   

