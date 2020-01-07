import sys
import datetime
from pydub.utils import mediainfo
import glob

print(sys.argv[1])
minutes = int(sys.argv[1]) * 60
print(type(minutes))
print(minutes)
#print(sys.argv[2])
for mp4 in sorted(glob.glob('*.mp4')):
    data = mediainfo(mp4)
    #print(data)
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    if int(float(data['duration'])) < minutes:     # 5 minutes 5 * 60
    #if int(float(data['duration'])) < 600:     # 10 minutes 10 * 60
        print(mp4,' => ',int(float(data['duration'])))
        #print(type(int(float(data['duration']))))
        #print(int(float(data['duration'])))
        #print(data['duration'])

