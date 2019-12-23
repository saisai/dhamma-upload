#!/data/data/com.termux/files/usr/bin/env python
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



from .helper import natural_keys


#file = sys.argv[0]
#pathname = os.path.dirname(file)
#running_from_path = os.path.abspath(pathname) + '/'
#print('aa',running_from_path)

#full_path = os.path.realpath(__file__)
#path, filename = os.path.split(full_path)
#os.chdir(path)


    

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
    # self.running_from_path, self.remote_username, self.remote_pass, self.remote_hostname, self.remote_port, self.escaped_remote, queue
    def __init__(self, running_from_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, queue):

        Thread.__init__(self, name=binascii.hexlify(os.urandom(16)))
        self.queue = queue
        self.running_from_path = running_from_path
        self.remote_username = remote_username
        self.remote_pass = remote_pass
        self.remote_hostname = remote_hostname
        self.remote_port = remote_port
        self.escaped_remote = escaped_remote        

    def run(self):
        while True:
            # gets the url from the queue
            getObj = self.queue.get()
            print('getObj', getObj)
            #if os.path.isfile(getObj):                
                                
                # download the file
                #print("* Thread {} - processing URL".format(self.name))
            self.download_file(getObj, self.remote_username, self.remote_pass, self.remote_hostname, self.remote_port, self.escaped_remote)
                # send a signal to the queue that the job is done
            self.queue.task_done()
                
    def download_file(self, copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote):
        print('copied_file', copied_file)
        #if os.path.isfile(copied_file):
        cmd = "sshpass -p %s /usr/bin/rsync -P --partial -avzzz -e 'ssh -p %s' %s@%s:'%s' '%s'" % (remote_pass, remote_port, remote_username, remote_hostname, copied_file, self.running_from_path)
        print(cmd)
        result = 1 
        while result != 0:
            result = subprocess.Popen(cmd,shell=True).wait()
            #text = result.communicate()[0]
            #returncode = result.returncode
        
            print(result)
            
            #if result == 0:
                #if os.path.isfile(copied_file):
                #print('Moving file...', copied_file)
                    #shutil.move(copied_file, '%sfinished/' % (self.running_from_path))                
            
class ConvertManager():
    """Spawns downoader threads and manages URL downloads queue"""
    # mp3s, running_from_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, mp3s, threads
    def __init__(self, running_from_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        self.remote_username = remote_username
        self.remote_pass = remote_pass
        self.remote_hostname = remote_hostname
        self.remote_port = remote_port
        self.escaped_remote = escaped_remote
        self.running_from_path = running_from_path
        

    def begin_convert(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """
        print("convert")
        queue = Queue()
        #queue = PriorityQueue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Converter(self.running_from_path, self.remote_username, self.remote_pass, self.remote_hostname, self.remote_port, self.escaped_remote, queue)
            t.setDaemon(True)
            t.start()


        for key in self.convert_list:
            #print(int(mp3.split('|')[0].split('.')[0]))
            #queue.put(Job((int(mp3.split('|')[0].split('.')[0])), mp3))            
            #queue.put(Job(int(key['id']),  key['description'], key['title'], key['playlist']))    
            print(key)
            queue.put(key)            

        # wait for the queue to finish
        queue.join()

        return

parser = argparse.ArgumentParser()
parser.usage = "pydownload.py -o <OutputDirectory> -i <JSONinputfile> -f <url1,url2,url3>"
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--ifile')
parser.add_argument('-f', '--flist')


#def thread_upload_remote(file_in, threads):
def thread_download_remote_local(copied_file, local_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, threads):
    # https://stackoverflow.com/questions/41718637/unable-to-connect-to-remote-host-using-paramiko
    import paramiko
    proxy = None
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=remote_hostname,username=remote_username,password=remote_pass, sock=proxy)
    #client.connect(remote_hostname, username=remote_username, key_filename="/cygdrive/e/dhamma-upload/future/fb/bokyaung/2/tt/hello")
    stdin, stdout, stderr = client.exec_command('%s %s%s' % ('ls', escaped_remote,copied_file))
    #print(type(stdout))
    
    copied_file = []
    for line in stdout:
        #print('... ' + line.strip('\n'))
        print(line.strip('\n'))
        copied_file.append(line.strip('\n'))
    client.close()
    
    
    print(copied_file)
    #print(running_from_path)
    #copied_file = escaped_remote + copied_file
    print(copied_file)
    
    #print(glob.glob(copied_file))
    
    #mp3s = [data for data in sorted(glob.glob(copied_file), key=natural_keys)]
    mp3s = copied_file
    
    print("aa", mp3s)

    #convert_manager = ConvertManager(running_from_path, mp3s, threads)
    convert_manager = ConvertManager(local_path, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote, mp3s, threads)
    convert_manager.begin_convert()      
    