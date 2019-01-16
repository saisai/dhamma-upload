#!/bin/bash
for i in `ls *.mp4`
do 
    echo $i 
    rsync -P --partial -avzzz $i -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.54:/data/data/com.termux/files/home/youtube/Dr-Candavara-bhivamsa/dhammadownload_video/
done 


/data/data/com.termux/files/home/youtube/Bhaddanta-Sirikancana-bhivamsa/dhammadownload_video


rsync -P --partial -avzzz 054.mp4 -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.54:/data/data/com.termux/files/home/youtube/Bhaddanta-Sirikancana-bhivamsa/dhammadownload_video/