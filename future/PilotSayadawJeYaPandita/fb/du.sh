#ffmpeg -i 111.mp4 -ss 00:05:00 -codec copy 111_out.mp4
#ffmpeg -i 162.mp4 -ss 00:05:30 -codec copy 162_out.mp4
#ffmpeg -i 193.mp4 -ss 00:05:00 -codec copy 193_out.mp4 
#ffmpeg -i 424.mp4 -ss 00:04:30 -codec copy 424_out.mp4 
#ffmpeg -i 466.mp4 -ss 00:05:30 -codec copy 466_out.mp4 
#ffmpeg -i 512.mp4 -ss 00:06:10 -codec copy 512_out.mp4 
ffmpeg -i 882.mp4 -ss 00:05:01 -codec copy 882_out.mp4
ffmpeg -i 851.mp4 -ss 00:00:00 -t 1:56:00  -c copy 851_out.mp4