#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 051.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 052.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 053.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 054.mp4
mv VTS_01_4.VOB dd/



