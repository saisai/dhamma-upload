#!/bin/bash

cat VTS_01_1.VOB | ffmpeg -i - 055.mp4
mv VTS_01_1.VOB dd/
cat VTS_01_2.VOB | ffmpeg -i - 056.mp4
mv VTS_01_2.VOB dd/
cat VTS_01_3.VOB | ffmpeg -i - 057.mp4
mv VTS_01_3.VOB dd/




