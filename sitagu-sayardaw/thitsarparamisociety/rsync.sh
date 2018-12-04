#!/bin/bash
#rsync -avzzz -P {600..1034}.mp3 -e 'ssh -i /cygdrive/d/sms_copy/ssh_keygen/this' user@192.168.1.123:/home/user/mahasi/ahshinottama/
#rsync -avzzz -P *.mp3 -e 'ssh -i /cygdrive/d/sms_copy/ssh_keygen/this' user@192.168.1.123:/home/user/mahasi/ahshinottama/
#rsync -avzzz -P user@192.168.1.123:/home/user/mahasi/ahshinottama/{610..700}.mp4 .
rsync -avzzz -P user@192.168.1.123:/home/user/mahasi/ahshinottama/*mp4 .
