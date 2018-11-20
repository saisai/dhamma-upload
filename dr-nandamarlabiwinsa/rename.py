import glob
import shutil
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

counter = 1    
for mp3 in sorted(glob.glob("*.mp3"), key=natural_keys):
    print(mp3)
    ff = "edit/{:03d}.mp3".format(counter)
    shutil.copyfile(mp3, ff)
    print(ff)
    counter += 1
