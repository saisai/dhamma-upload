#rsync -P -avzzz 250.mp4 -e 'ssh -p 8022 -i /d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/
#rsync -P -avzzz {241..338}.mp4 -e 'ssh -p 8022 -i /cygdrive/d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/
#rsync -P -avzzz raw_json_title.txt -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/sitagu-sayardaw/
rsync -P -avzzz thread_download.py -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.54:/data/data/com.termux/files/home/youtube/Bhaddanta-Tilokarbhivamsa/dhammadownload/
rsync -P -avzzz *.txt -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.54:/data/data/com.termux/files/home/youtube/Bhaddanta-Tilokarbhivamsa/dhammadownload/


#for i in `ls -1 *.mp4 | sort -n`
#do
    #echo $i;
    #rsync -P -avzzz $i -e 'ssh -p 8022 -i /cygdrive/d/jcy/sms_copy/ssh_keygen/this' u0_a95@192.168.1.54:/data/data/com.termux/files/home/youtube/sitagu-sayardaw/dhammadownload_video/    
#done
