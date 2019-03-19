#!/data/data/com.termux/files/usr/bin/env python

import os
import datetime

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

def get_code():
    """
    :rtype List
    """
    if os.path.isfile('/usr/bin/youtube-upload') == True:
        result = os.popen( "ps -aef | grep -i '/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )
    elif os.path.isfile('/data/data/com.termux/files/usr/bin/youtube-upload') == True:
        result = os.popen( "ps -aef | grep -i '/data/data/com.termux/files/usr/bin/youtube-upload' | awk '{ print $3 }'" ).read().strip().split( '\n' )

    return result

if __name__ == '__main__':
    if len(get_code()) <= 2:


        folders = [f.strip('\n') for f in open('cronrun.txt', 'r') if len(f) > 2]
        #print(folders)

        
        for result in folders:
            print(result)
            os.system('%s %s' % ('python', result))
        
