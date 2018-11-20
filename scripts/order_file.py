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

files = [f.strip('\n') for f in open('no_time_id_title_test_today.txt', 'r')]

'''    
for mp4 in sorted(files, key=natural_keys):
    print(mp4)
'''

with open('final_results.txt', 'w') as f:
    for mp4 in sorted(files, key=natural_keys):
        f.write('{}\n'.format(mp4))    

