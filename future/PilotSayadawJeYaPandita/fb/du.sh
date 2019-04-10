#ffmpeg -i 111.mp4 -ss 00:05:00 -codec copy 111_out.mp4
#ffmpeg -i 162.mp4 -ss 00:05:30 -codec copy 162_out.mp4
#ffmpeg -i 193.mp4 -ss 00:05:00 -codec copy 193_out.mp4 
#ffmpeg -i 424.mp4 -ss 00:04:30 -codec copy 424_out.mp4 
#ffmpeg -i 466.mp4 -ss 00:05:30 -codec copy 466_out.mp4 
#ffmpeg -i 512.mp4 -ss 00:06:10 -codec copy 512_out.mp4 
#ffmpeg -i 882.mp4 -ss 00:05:01 -codec copy 882_out.mp4
#ffmpeg -i 851.mp4 -ss 00:00:00 -t 1:45:00  -c copy 851_out.mp4


ffmpeg -i 1169.mp4 -ss 00:00:00 -t 0:06:00  -c copy 1169_out_1.mp4
ffmpeg -i 1169.mp4 -ss 00:08:00 -c copy 1169_out_2.mp4
ffmpeg -i "concat:1169_out_1.mp4|1169_out_2.mp4" -c copy 1169_out.mp4
mv -v 1169_out_1.mp4 de
mv -v 1169_out_2.mp4 de

ffmpeg -i 1166.mp4 -ss 00:00:00 -t 0:05:00  -c copy 1166_out_1.mp4
ffmpeg -i 1166.mp4 -ss 00:06:30 -c copy 1166_out_2.mp4
ffmpeg -i "concat:1166_out_1.mp4|1166_out_2.mp4" -c copy 1166_out.mp4
mv -v 1166_out_1.mp4 de
mv -v 1166_out_2.mp4 de

ffmpeg -i 1102.mp4 -ss 00:00:00 -t 0:05:00  -c copy 1102_out_1.mp4
ffmpeg -i 1102.mp4 -ss 00:07:05 -c copy 1102_out_2.mp4
ffmpeg -i "concat:1102_out_1.mp4|1102_out_2.mp4" -c copy 1102_out.mp4
mv -v 1102_out_1.mp4 de
mv -v 1102_out_2.mp4 de

# https://trac.ffmpeg.org/wiki/Concatenate
# https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg