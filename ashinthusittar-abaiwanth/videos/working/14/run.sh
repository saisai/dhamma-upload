#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 044.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 045.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 046.mp4
mv VTS_01_3.VOB dd/



