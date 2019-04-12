import os

files = [f.strip('\n') for f in open('new_1_15.txt')]

for ff in files:
    if os.path.exists(ff):
        print(ff)
        os.remove(ff)

