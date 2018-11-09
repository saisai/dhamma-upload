import functools

from threading import Thread, Semaphore
import re
import binascii
import os
import subprocess
"""
sema = threading.Semaphore()
def count():
    sema.acquire()
    print("Start")
    for i in range(1, 4):
        print(i)
    sema.release()
"""    
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
        self.sema = Semaphore()
        

    def run(self):
        self.sema.acquire()

        print('hello')
        mp3files = self.queue
        print(type(mp3files), mp3files, 'aa')
        print(type(mp3files))   
        for mp3file in mp3files:
            self.download_file(mp3file)
        self.sema.release()
        """
        while True:           
        
            # gets the url from the queue
            mp3file = self.queue
            print(type(mp3file), mp3file, 'aa')
            print(type(mp3file))
            # download the file
            print("* Thread {} - processing URL".format(self.name))
            Converter.count += self.download_file(mp3file)
            
            # send a signal to the queue that the job is done
            print(Converter.count, 'asdf')
            #self.queue.task_done()
        """    
            
        
        
    def download_file(self, mp3file):
        """Download file"""
        #if os.path.isfile(mp3file):
            
        
        
        #print("* Thread: {} Download {} in {} seconds.".format(self.name, mp3file, str(t_elapsed)))   

        filename = (mp3file.split('|')[0])
        url = (mp3file.split('|')[1])
        #command = 'wget -c -O {} {}'.format(filename, url)
        #os.system(command)       
        
        
        command = 'wget|--no-check-certificate|-c|-O|{}|{}'.format(filename, url)
        print(command)
        completed = subprocess.run(command.split('|'))
        
        """
        print('returncode:', completed)
        print(completed.returncode)
        if completed.returncode != 0:
            os.killpg(0, signal.SIGKILL)  
        else:
            return 1    
        """
    
hosts = [f.strip('\n') for f in open('titles_links.txt')]

hosts = sorted(hosts, key=natural_keys) 
test = False 
count = len(hosts)
aa = 0
bb = 2



while count > -1:
    print(count)
    print(hosts[aa:bb]) 
    
    t = Converter(hosts[aa:bb])
    #t.setDaemon(True)
    t.start()
    
    count -= bb 
    aa = bb
    bb += 2

"""
import threading

sema = threading.Semaphore()
def count():
    sema.acquire()
    print("Start")
    for i in range(1, 4):
        print(i)
    sema.release()
    
thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)
thread1.start()
thread2.start()
"""