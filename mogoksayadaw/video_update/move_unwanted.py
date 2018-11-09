
import glob
import shutil

files = [f.strip('\n') for f in open('must_work.txt')]

for f in files:
    print(f)
    new = 'edit/{}'.format(f)
    shutil.copyfile(f, new)    

'''
#counter = 1
for i in sorted(glob.glob('*.mp3')):
    print(i)
    cc = '{:03d}'.format(counter)
    print(cc)
    #new = 'edit/{:03d}.mp4'.format(counter)
    #shutil.copyfile(i, new)
    #counter += 1
'''