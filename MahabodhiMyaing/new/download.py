
import os
import subprocess

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

lines = [line.strip('\n') for line in open('file.txt', 'r')]
#print(lines)
count = 1

for line in lines:
    
    dest = '{:03}.mp3'.format(count)
    command = "wget|-c|-O|{}|{}".format(dest, line)
    print(command)
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    count += 1
