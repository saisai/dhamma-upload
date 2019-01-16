#!/bin/bash 
RC=1
while [[ $RC -ne 0 ]]
do 
    #rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/storage/downloads/youtube/Dhammaduta-Ashin-SayKaneDa/dhammadownload_video/
    rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/storage/external-1/youtube/Dhammaduta-Ashin-SayKaneDa/dhammadownload_video/
    RC=$?
    if [[ $RC == 20 ]]; then
        echo $RC
        break
    fi 
done
