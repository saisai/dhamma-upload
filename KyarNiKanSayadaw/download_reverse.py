
import os
import subprocess
"""
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
"""

lines = [line.strip('\n') for line in open('file.txt', 'r')]
#print(lines)
print(len(lines))
count = len(lines)

for line in reversed(lines):
    
    dest = '{:03}.mp3'.format(count)
    command = "wget|-c|-O|{}|{}".format(dest, line)
    print(command)
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    count -= 1
