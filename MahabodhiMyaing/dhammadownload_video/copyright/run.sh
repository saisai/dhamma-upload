#!/bin/bash
ffmpeg -i 050.mp4 -c copy -ss 00:00:00 -to 01:11:00 edit/050.mp4
ffmpeg -i 049.mp4 -ss 00:09:10 -codec copy edit/049.mp4
ffmpeg -i 048.mp4 -c copy -ss 00:00:00 -to 02:18:00 edit/048.mp4
ffmpeg -i 047.mp4 -c copy -ss 00:00:00 -to 00:45:00 edit/047.mp4
ffmpeg -i 044.mp4 -ss 00:20:00 -codec copy edit/044.mp4
ffmpeg -i 035.mp4 -ss 00:07:00 -codec copy edit/035.mp4
ffmpeg -i 031.mp4 -ss 00:07:00 -codec copy edit/031.mp4
ffmpeg -i 002.mp4 -ss 00:12:00 -codec copy edit/002.mp4
ffmpeg -i 003.mp4 -c copy -ss 00:00:00 -to 00:45:00 edit/003.mp4
