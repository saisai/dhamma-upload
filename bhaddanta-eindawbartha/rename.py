import os
import glob
import shutil

edit = 'edit'

if not os.path.isdir(edit):
    os.mkdir(edit)

counter = 1
for key in sorted(glob.glob('*.mp4')):
    #print(key)
    #print(counter)
    counter_format = '{:03d}'.format(counter)
    moved_file = str(counter_format) + '.mp4'
    #if os.path.isfile(moved_file):
    print(moved_file)
    #shutil.move(key, edit + '/' + moved_file)
    
    counter += 1
