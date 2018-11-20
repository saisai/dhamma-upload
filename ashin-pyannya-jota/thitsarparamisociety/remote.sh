#rsync -P -avzzz 250.mp4 -e 'ssh -p 8022 -i /d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/
#rsync -P -avzzz {241..338}.mp4 -e 'ssh -p 8022 -i /cygdrive/d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ahshinottama/
rsync -P -avzzz *.mp4 -e 'ssh -p 8022 -i /cygdrive/d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ashin-pyannya-jota/
rsync -P -avzzz raw_json_title.txt -e 'ssh -p 8022 -i /cygdrive/d/jcy/folder/ssh_keygen/this' u0_a95@192.168.1.41:/data/data/com.termux/files/home/youtube/ashin-pyannya-jota/
