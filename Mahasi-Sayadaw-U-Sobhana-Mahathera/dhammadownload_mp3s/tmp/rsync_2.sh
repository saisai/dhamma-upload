#sshpass -p snp rsync -avzzz -p {001..030}.mp4 -e 'ssh -p 8022' snp@192.168.1.49:/data/data/com.termux/files/home/storage/external-1/youtube/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/
# /data/data/com.termux/files/home/storage/downloads/dhama
sshpass -p snp rsync -avzzz -p *.mp3 -e 'ssh -p 8022' snp@192.168.1.49:/data/data/com.termux/files/home/storage/downloads/dhama/

