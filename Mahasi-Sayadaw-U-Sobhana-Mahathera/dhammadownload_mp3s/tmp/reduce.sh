#MUSIC="FULL PATH TO YOUR MUSIC FOLDER"
MUSIC="/home/snp/Desktop/dhamma-upload/Mahasi-Sayadaw-U-Sobhana-Mahathera/dhammadownload_mp3s/tmp"
BITRATE=160k
find "${MUSIC}" -name "*.mp3" -execdir echo "{}" \; -exec mv "{}" "{}.mp3" \; -exec ffmpeg -y -loglevel "error" -i "{}.mp3" -acodec libmp3lame  -ab $BITRATE "{}" \; -exec rm "{}.mp3" \;
