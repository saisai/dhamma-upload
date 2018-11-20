import os 
import shutil
files =[f.strip('\n') for f in open('all_files.txt', 'r')]

# remove file 25 by each time
# and every time to remove file
# increase by 25
# first time 25
# second time 50 and so on.


count = 1
for f in files:
    if count <=  495:
        #print(f)
        #print(len(f))
        #src = '{}.mp4'.format(''.join(f))
        src = '{}.mp4'.format(f.strip())
        #print(src)
        if os.path.exists(src):
            #print(f)
            #print(len(f))
            print(src)
            dest = 'finished_by_hand/' + src
            #os.rename(src, dest)
            print('moving file' + src)
            shutil.move(src, dest)
            print(count)

    count += 1
