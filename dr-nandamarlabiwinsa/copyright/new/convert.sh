
if  [ ! $1 ]; then
  threads=1
  echo "aa"
else
  threads=$1
fi

echo $threads
python thread_convert_mp3_to_mp4.py $threads
