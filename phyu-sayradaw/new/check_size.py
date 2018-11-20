
import glob
import subprocess
import os 
for i in sorted(glob.glob('*.mp3')):
    if os.stat(i).st_size ==0:
        print(i, os.stat(i).st_size ==0 )

    #completed = subprocess.run(['file', i])
    #print(completed)

