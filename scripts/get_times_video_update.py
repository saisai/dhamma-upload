import datetime
from pydub.utils import mediainfo
import glob
import re 

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

fmt = 1
for mp4 in sorted(glob.glob('*.mp3'), key=natural_keys):
    data = mediainfo(mp4)
    #print(int(float(data['duration'])))
    #print(data['duration'])
    mp3 = '{:03d}.mp3'.format(fmt)
    #print(mp3)
    #print(mp4, mp3, str(datetime.timedelta(seconds=int(float(data['duration'])))))
    print(mp3, str(datetime.timedelta(seconds=int(float(data['duration'])))))
    #print(data)
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    #if int(float(data['duration'])) >= 4200:
        #print(mp4)
        #print(type(int(float(data['duration']))))
        #print(int(float(data['duration'])))
        #print(data['duration'])
    fmt += 1
