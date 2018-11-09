import os 
import shutil

remove_duplicate = 'remove_duplicate'
if not os.path.isdir(remove_duplicate):
    os.mkdir(remove_duplicate)    

lines = [f.strip('\n') for f in open('test.txt')]
#print(lines)

remove_duplicates = []
for line in lines:
    #print(line)
    #print(type(line.split('./')[1].split('.')[0]))
    remove_duplicates.append((int(line.split('./')[1].split('.')[0])))
    mp4_file = line.split('./')[1].split('.')[0] + '.mp4'
    if os.path.isfile(mp4_file):
        print('Moving file..')
        shutil.move(mp4_file,remove_duplicate + '/' + mp4_file)
        print(mp4_file)
    #get_num = line.split('


mm_lines = [f.strip('\n') for f in open('titles.txt')]

check_duplicates = 1
for line in mm_lines:
    if not check_duplicates in remove_duplicates:
        print(line)
        #print(check_duplicates)
    check_duplicates += 1

