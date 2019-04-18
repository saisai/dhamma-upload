ffmpeg -i 100.mp4 -ss 00:00:00 -t 0:06:00  -c copy 100_out_1.mp4
ffmpeg -i 100.mp4 -ss 00:10:30 -c copy 100_out_2.mp4
ffmpeg -f concat -i 100.txt -vcodec copy -acodec copy 100_out.mp4