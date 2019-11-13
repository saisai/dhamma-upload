#!/bin/bash

# https://www.google.com/search?ei=ozzKXcO4N56VwgOotryQAQ&q=bash+get+current+directory&oq=bash+get+c&gs_l=psy-ab.3.0.0i67j0l9.114517.116451..117508...0.4..0.102.918.9j1......0....1..gws-wiz.......0i71.KAidSp1uVaQ
# https://www.cyberciti.biz/faq/howto-check-if-a-directory-exists-in-a-bash-shellscript/
# https://www.cyberciti.biz/faq/check-if-a-directory-exists-in-linux-or-unix-shell/

dir=`pwd`
echo $dir
if [ -d $dir"/edit" ] 
then
    echo "Directory /path/to/dir exists." 
    
else
    echo "Error: Directory /path/to/dir does not exists."
    mkdir $dir"/edit"
fi
#ffmpeg -i 517.mp4 -vf "transpose=2" 517_out.mp4
#ffmpeg -i 584.mp4 -vf "transpose=2" 584_out.mp4
#ffmpeg -i 600.mp4 -vf "transpose=2" 600_out.mp4
#ffmpeg -i 602.mp4 -vf "transpose=2" 602_out.mp4
#ffmpeg -i 630.mp4 -vf "transpose=2" 630_out.mp4
#ffmpeg -i 705.mp4 -vf "transpose=2" edit/705.mp4
