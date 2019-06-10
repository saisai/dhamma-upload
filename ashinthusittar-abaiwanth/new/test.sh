for a in [0-2]*.mp4; do
   echo $a
    mv $a `printf %03d.%s ${a%.*} ${a##*.}`
done
