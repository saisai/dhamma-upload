#!/bin/bash
cat VTS_01_1.VOB | ffmpeg -i - 001.mp4
cat VTS_01_2.VOB | ffmpeg -i - 002.mp4
cat VTS_01_3.VOB | ffmpeg -i - 003.mp4
cat VTS_01_4.VOB | ffmpeg -i - 004.mp4
cat VTS_02_1.VOB | ffmpeg -i - 005.mp4
