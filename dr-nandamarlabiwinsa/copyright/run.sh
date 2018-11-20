ffmpeg -i 391.mp3 -ss 00:11:00 -codec copy -t 00:17:00 oout1.mp3
ffmpeg -i 391.mp3 -ss 00:34:00 -codec copy oout2.mp3
ffmpeg -i "concat:oout1.mp3|oout2.mp3" -c copy output3.mp3
