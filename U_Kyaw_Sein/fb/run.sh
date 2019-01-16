#!/bin/bash
while true; do rsync -P --partial -avzzz *.mp4 -e 'ssh -p 8022 -i /d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.38:/data/data/com.termux/files/home/storage/downloads/youtube/U_Kyaw_Sein/ ; done
