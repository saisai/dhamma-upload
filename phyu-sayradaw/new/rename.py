
import glob
import shutil

counter = 105
for i in sorted(glob.glob('*.mp4')):
    print(i)
    new = 'edit/{:03d}.mp4'.format(counter)
    shutil.copyfile(i, new)
    counter += 1
