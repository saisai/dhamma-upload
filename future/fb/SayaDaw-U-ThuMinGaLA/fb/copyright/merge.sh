#ffmpeg -i 100.mp4 -ss 00:00:00 -t 0:06:00  -c copy 100_out_1.mp4
#ffmpeg -i 100.mp4 -ss 00:10:30 -c copy 100_out_2.mp4
#ffmpeg -f concat -i 100.txt -vcodec copy -acodec copy 100_out.mp4
ffmpeg -i 468.mp4 -ss 00:06:00 -c copy 468_out.mp4  
ffmpeg -i 631.mp4 -ss 00:07:00 -c copy 631_out.mp4  
