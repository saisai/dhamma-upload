#!/data/data/com.termux/files/usr/bin/env python

import os

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

        #os.system('python /data/data/com.termux/files/home/youtube/abhidhamma/thread_upload-old.py -u -td 1')
        


        

