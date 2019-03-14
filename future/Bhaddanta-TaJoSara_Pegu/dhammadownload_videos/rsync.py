#!/usr/bin/env python
# coding=utf-8

# The script will run until pressing clrl + c

import subprocess
import shutil 
import os

remote_username = 'u0_a97'
remote_hostname = '192.168.1.39'
escaped_remote = '/data/data/com.termux/files/home/storage/external-1/youtube/Bhaddanta-TaJoSara_Pegu/'

#data = [f.strip('\n').split('|')[0] for f in open('new_urltext_upload.txt', 'r') if os.path.isfile('%s.mp4' % (f.strip('\n').split('|')[0],))]

#print(data)
#print(len(data))


if not os.path.isdir('finished'):
    os.mkdir('finished')
   
'''
for i in range(0, 30):
    
    print(i)
    print(data[i])
    
    if os.path.isfile(data[i]+'.mp4'):
        print('Moving file...', data[i]+'.mp4')
        shutil.move(data[i]+'.mp4', 'finished/')    
'''

for i in range(1, 30):
    
    mp4 = '{:03d}.mp4'.format(i)
    
    
    if os.path.isfile(mp4):
        cmd = "sshpass -p snp /usr/bin/rsync -P --partial -avzzz %s -e 'ssh -p 8022' %s@%s:'%s'" % (mp4, remote_username, remote_hostname, escaped_remote)

        result = 1 
        while result != 0:
            result = subprocess.Popen(cmd,shell=True).wait()
            #text = result.communicate()[0]
            #returncode = result.returncode

        
            print(result)

            if os.path.isfile(mp4):
                print('Moving file...', mp4)
                shutil.move(mp4, 'finished/')
    


'''
cmd = "sshpass -p snp /usr/bin/rsync -P --partial -avzzz {201..603}.mp4 -e 'ssh -p 8022' %s@%s:'%s'" % (remote_username, remote_hostname, escaped_remote)

result = 1 
while result != 0:
    result = subprocess.Popen(cmd,shell=True).wait()
    #text = result.communicate()[0]
    #returncode = result.returncode

    print(result)
'''
