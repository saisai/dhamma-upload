#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 035.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 036.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 037.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 038.mp4
mv VTS_01_4.VOB dd/
cat VTS_01_5.VOB | ffmpeg -i - 039.mp4
mv VTS_01_5.VOB dd/
