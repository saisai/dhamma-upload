#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 063.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 064.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 065.mp4
mv VTS_01_3.VOB dd/
cat VTS_01_4.VOB | ffmpeg -i - 066.mp4
mv VTS_01_4.VOB dd/





