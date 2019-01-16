
#import processes
import os 
import sys
import subprocess
import signal
files = [f.strip('\n') for f in open('titles_links.txt')]


for f in reversed(files):
    try:
        #command = "wget|-c|--no-check-certificate|-O|{}|{}".format(filename, url)
        #print(command)
        #completed = subprocess.run(command.split('|'))
        #line = "rsync -avzzz -P -e 'ssh -p 8022 -i /d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/dhammadownload_video/{} .".format(f.split('|')[0])
        #os.system(line)
        #print(f)
        line = "rsync|-avzzz|-P|-e|{}|u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/dhammadownload_video/{}|.".format('ssh -p 8022 -i /d/jcy/folder/ssh_keygen/this', f.split('|')[0])
        print(line.split('|'))
        completed = subprocess.run(line.split('|'))
    except KeyboardInterrupt as err:
        print(err)
        os.killpg(0, signal.SIGKILL)
        #os.kill(completed.pid, signal.SIGINT)
        #sys.exit(0)
