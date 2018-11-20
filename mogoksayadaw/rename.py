
import glob
import shutil

counter = 1
for i in sorted(glob.glob('*.mp3')):
    print(i)
    cc = '{:03d}'.format(counter)
    print(cc)
    #new = 'edit/{:03d}.mp4'.format(counter)
    #shutil.copyfile(i, new)
    counter += 1
