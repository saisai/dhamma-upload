#!/usr/bin/env python
# coding=utf-8

import os
import signal
import sys 


try:
    #os.system("rsync -P --partial -avzzz {060..080}.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
    os.system("rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/youtube/Mrauk-U-Sayadaw-WarYaMainda/dhammadownload_video/")
except KeyboardInterrupt as err:
    print(err)
    os.killpg(0, signal.SIGKILL)
    #sys.exit()
