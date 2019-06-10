#!/bin/bash
cat VIDEO_TS.VOB | ffmpeg -i - test.mp4
cat VTS_01_1.VOB | ffmpeg -i - 030.mp4
cat VTS_01_2.VOB | ffmpeg -i - 031.mp4
cat VTS_02_1.VOB | ffmpeg -i - 032.mp4
cat VTS_02_2.VOB | ffmpeg -i - 033.mp4
cat VTS_02_3.VOB | ffmpeg -i - 034.mp4
