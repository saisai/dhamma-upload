#!/usr/bin/env python
# coding=utf-8

import subprocess

#with open('dl.txt', 'r') as f:
#    print(f.readlines())

#lines = [line.rstrip('\n') for line in open('dl.txt')]

format_count = '218588348615440'
line= 'https://www.facebook.com/WinNaingKyawfromYangon/videos/218588348615440'
command = 'youtube-dl|-o|{}.%(ext)s|{}'.format(format_count, line)
print(command)
completed = subprocess.run(command.split('|'))
print('returncode:', completed)


