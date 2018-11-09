import shutil
import glob

count = 2344
for key in sorted(glob.glob('*.mp3')):
    print(key)
    
    counter = 'edit/{:03}.mp3'.format(count)
    
    print(key, counter)
    shutil.copyfile(key, counter)
    count += 1
    
