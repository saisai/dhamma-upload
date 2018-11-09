import os
import shutil

files = [f.strip('\n') for f in open('convert.txt')]

for ff in files:
    if os.path.exists(ff):
        print(ff)
        dest = 'edit/' + ff
        shutil.move(ff, dest)
        #os.remove(ff)

