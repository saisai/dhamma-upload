#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 047.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 048.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 049.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 050.mp4
mv VTS_01_4.VOB dd/



