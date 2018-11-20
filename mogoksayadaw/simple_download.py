
import os
import subprocess
"""
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
"""

lines = [line.strip('\n') for line in open('file.txt', 'r')]
#print(lines)
#count = 1

for line in lines:
    filename = line.split('||')[0]
    url = line.split('||')[1]
    #dest = '{:03}.mp3'.format(count)
    command = "wget|-c|-O|{}|{}".format(filename, url)
    print(command)
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    #count += 1
