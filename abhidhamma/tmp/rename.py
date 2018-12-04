import os

files = [f.strip('\n') for f in open('links.txt', 'r') if len(f) > 2]

folder = 'edit'
count = 503
for f in files:
    print(f.split('/')[-1])
    src = f.split('/')[-1]
    dest = '{:03}.mp4'.format(count)
    print(dest)
    os.rename(src, dest)
    count += 1
