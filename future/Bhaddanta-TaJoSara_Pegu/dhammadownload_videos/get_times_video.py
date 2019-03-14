import datetime
from pydub.utils import mediainfo
import glob

# https://bbs.archlinux.org/viewtopic.php?id=77634
# https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds

def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)
    
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
    
    

for mp4 in sorted(glob.glob('*.mp4')):
    data = mediainfo(mp4) # data['duration'] seconds
    print(humanize_time(int(float(data['duration']))))
    print('{} {}'.format(mp4, str(datetime.timedelta(seconds=int(float(data['duration']))))))
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    #if int(float(data['duration'])) >= 4500:
        #print(mp4)
        #print(type(int(float(data['duration']))))
        #print(int(float(data['duration'])))
        #print(data['duration'])

