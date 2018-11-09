import os
import glob
import shutil

edit = 'edit'

if not os.path.isdir(edit):
    os.mkdir(edit)

counter = 101
for key in sorted(glob.glob('*.mp4')):
    print(key)
    print(counter)
    moved_file = str(counter) + '.mp4'
    #if os.path.isfile(moved_file):
    print(moved_file)
    shutil.move(key, edit + '/' + moved_file)
    
    counter += 1
