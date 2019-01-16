#!/bin/bash
ffmpeg -i 005.mp4 -ss 00:05:00 -codec copy edit/005.mp4
ffmpeg -i 009.mp4 -ss 00:04:00 -codec copy edit/009.mp4
