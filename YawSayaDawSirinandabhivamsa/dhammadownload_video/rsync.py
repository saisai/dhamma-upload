#!/usr/bin/env python
# coding=utf-8

# The script will run until pressing clrl + c

import subprocess

remote_username = 'u0_a97'
remote_hostname = '192.168.1.35'
escaped_remote = '/data/data/com.termux/files/home/youtube/YawSayaDawSirinandabhivamsa/'

#cmd = "sshpass -p snp /usr/bin/rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
cmd = "sshpass -p snp /usr/bin/rsync -P --partial -avzzz raw_json_title.txt -e 'ssh -p 8022' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)

result = 1 
while result != 0:
    result = subprocess.Popen(cmd,shell=True).wait()
    #text = result.communicate()[0]
    #returncode = result.returncode

    print(result)
