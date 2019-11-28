import os
import datetime
from pydub.utils import mediainfo
import glob

# https://bbs.archlinux.org/viewtopic.php?id=77634
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

total = 0
for mp4 in sorted(glob.glob('*.mp4')):
    data = mediainfo(mp4)
    result = str(datetime.timedelta(seconds=int(float(data['duration'])))).split(':')
    if int(result[0]) == 0 and int(result[1]) <= 10:
        print('{} {}'.format(mp4, str(datetime.timedelta(seconds=int(float(data['duration']))))))
        print('Deleting file ', mp4)
        os.remove(mp4)
        total += 1

if total > 0:

    print('Total ', total)

