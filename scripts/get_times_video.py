import datetime
from pydub.utils import mediainfo
import glob

for mp4 in sorted(glob.glob('*.mp3')):
    data = mediainfo(mp4)
    #print(data)
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    if int(float(data['duration'])) >= 4200:
        print(mp4)
        #print(type(int(float(data['duration']))))
        #print(int(float(data['duration'])))
        #print(data['duration'])

