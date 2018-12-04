#!/bin/bash
ffmpeg -i 228.mp3 -ss 00:00:00 -codec copy -t 00:52:20 edit/228.mp3
ffmpeg -i 312.mp3 -ss 00:06:00 -codec copy edit/312.mp3
