#!/usr/bin/env python
# coding=utf-8
import os
import sys
import subprocess
import signal

line = "rsync|-avzzz|-P|-e|{}|u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/dhammadownload_video/finished/{} .".format('ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this', '536.mp4')
print(line.split('|'))
completed = subprocess.run(line.split('|'))
