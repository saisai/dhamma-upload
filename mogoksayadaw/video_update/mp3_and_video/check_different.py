import datetime
import glob 
import re 

from pydub.utils import mediainfo

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
    

#minutes =   [f.strip('\n') for f in open('new_file_test.txt', 'r')]
mp4s = sorted(glob.glob("*.mp4"), key=natural_keys)
mp3s = sorted(glob.glob("*.mp3"), key=natural_keys)

with open('different.txt', 'w') as ff:
    
    for mp3, mp4 in zip(mp3s, mp4s):
        
        '''
        f = mm.split('|||')[1]
        data = f.split(':')
        if len(data) > 2:
            online_duration = datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds
            #print(online_duration)
        else:
            online_duration = datetime.timedelta(hours=0, minutes=int(data[0]), seconds=int(data[1])).seconds
            #print(online_duration)
        '''
        local_mp4 = mediainfo(mp4)
        local_duration_mp4 = int(float(local_mp4['duration']))        
        
        local = mediainfo(mp3)
        local_duration = int(float(local['duration']))
        print('{} {} {} {} {}'.format(mp4, mp3, local_duration, local_duration_mp4 , local_duration-local_duration_mp4))
        #ff.write('{} {} {} {}\n'.format(mp3, local_duration, online_duration , local_duration-online_duration))
        #ff.flush()
        
        if local_duration-local_duration_mp4 < -2:
            print('{} {} {} {} {}'.format(mp4, mp3, local_duration, local_duration_mp4 , local_duration-local_duration_mp4))
            ff.write('{} {} {} {} {}\n'.format(mp4, mp3, local_duration, local_duration_mp4 , local_duration-local_duration_mp4))
            ff.flush()
        elif local_duration-local_duration_mp4 > 2:
            print('{} {} {} {} {}'.format(mp4, mp3, local_duration, local_duration_mp4 , local_duration-local_duration_mp4))
            ff.write('{} {} {} {} {}\n'.format(mp4, mp3, local_duration, local_duration_mp4 , local_duration-local_duration_mp4))
            ff.flush()

"""
count = 1
for result in minutes:
    f = result.split('|||')[1]
    data = f.split(':')
    if len(data) > 2:
        if datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds > 4500:
            print(result.split('|||')[0])
"""
            

