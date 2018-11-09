#!/usr/bin/env python
# coding=utf-8

import subprocess

#with open('dl.txt', 'r') as f:
#    print(f.readlines())

lines = [line.rstrip('\n') for line in open('dl.txt')]

count = 5
for line in lines:
    print(line)
    format_count = '{:03}'.format(count)
    command = 'youtube-dl|-o|{}.%(ext)s|-x|--audio-format|mp3|{}'.format(format_count, line)
    print(command)
    completed = subprocess.run(command.split('|'))
    print('returncode:', completed)
    count += 1


