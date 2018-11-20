import os

files = [f.strip('\n') for f in open('delete.txt', 'r')]
for f in files:
    if os.path.exists(f):
        print(f)
        os.remove(f)

#print(files)
