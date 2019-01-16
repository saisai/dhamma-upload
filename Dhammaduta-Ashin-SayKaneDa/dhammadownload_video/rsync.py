#!/usr/bin/env python
# coding=utf-8

import subprocess
#result = subprocess.Popen("rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/storage/external-1/youtube/Dhammaduta-Ashin-SayKaneDa/dhammadownload_video/")
remote_username = 'u0_a95'
remote_hostname = '192.168.1.38'
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/youtube/Dhammaduta-Ashin-SayKaneDa/dhammadownload_video/'
cmd = "/usr/bin/rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
result = 1 
while result != 0:
    result = subprocess.Popen(cmd,shell=True).wait()
    #text = result.communicate()[0]
    #returncode = result.returncode

    print(result)
'''
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
'''    