#!/usr/bin/env python
# coding=utf-8

# The script will run until pressing clrl + c

import subprocess

remote_username = 'walen'
remote_hostname = '192.168.1.123'
escaped_remote = '/home/walen/mahasi/tmp/second/'
#cmd = "/usr/bin/rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
cmd = "sshpass -p walen /usr/bin/rsync -P --partial -avzzz *.mp3 -e 'ssh -p 22' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
#cmd = "/usr/bin/rsync -P --partial -avzzz *.txt -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)
result = 1 
while result != 0:
    result = subprocess.Popen(cmd,shell=True).wait()
    #text = result.communicate()[0]
    #returncode = result.returncode

    print(result)
