#!/usr/bin/env python
# coding=utf-8

import os
import signal
import sys 
import tty, termios
import time
import subprocess

remote_username = 'u0_a95'
remote_hostname = '192.168.1.38'
escaped_remote = '/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/'
cmd = "/usr/bin/rsync -P --partial -avzzz {150..250}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
print(cmd)


try:
    while True:
        process = subprocess.Popen(cmd,shell=True).wait()
        print('Running in process', process.pid)
        
    #process.wait(timeout=10)
#except subprocess.TimeoutExpired:
except KeyboardInterrupt as err:
    print('Timed out - killing', process.pid)
    process.kill()
    
# https://stackoverflow.com/questions/34556811/running-rsync-from-python-subprocess-in-windows
# https://ryanveach.com/233/calling-rsync-with-pythons-subprocess-module/    

'''
try:
    print('Running in process', process.pid)
    #process.wait(timeout=10)
#except subprocess.TimeoutExpired:
except KeyboardInterrupt as err:
    print('Timed out - killing', process.pid)
    process.kill()
'''
'''
try:
    while True:
        print('hello')
        os.system("rsync -P --partial -avzzz {031..032}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
        os.system("rsync -P --partial -avzzz {031..032}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
        time.sleep(1)
except KeyboardInterrupt:
    os.killpg(0, signal.SIGKILL) 
'''
'''
try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
        
def keypress():
    global char
    char = getch()
    return char 
while True:
    print(keypress())
'''   

'''
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  
'''
'''
try:
    while True:
        os.system("rsync -P --partial -avzzz {070..080}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
except KeyboardInterrupt as err:
    print(err)
    os.killpg(0, signal.SIGKILL)   
    sys.exit()
'''  
    
'''
running = True
while running:
    print(running)
    #global running
    if running:
        
        try:
            #os.system("rsync -P --partial -avzzz {060..080}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
            os.system("rsync -P --partial -avzzz {070..080}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
        except KeyboardInterrupt as err:
            print('keyborad')
            
            running = False
            print(err)
            os.killpg(0, signal.SIGKILL)
        #finally:
            #running = False
            #break
    else:
        break
'''