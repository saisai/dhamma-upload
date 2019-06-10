#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 040.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 041.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 042.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 043.mp4
mv VTS_01_4.VOB dd/


