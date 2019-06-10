#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 058.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 059.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 060.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 061.mp4
mv VTS_01_4.VOB dd/
cat VTS_01_5.VOB | ffmpeg -i - 062.mp4
mv VTS_01_5.VOB dd/




