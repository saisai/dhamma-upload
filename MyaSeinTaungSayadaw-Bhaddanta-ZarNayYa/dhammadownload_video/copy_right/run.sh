#!/bin/bash

function one()
{
ffmpeg -i 536.mp4 -ss 00:06:00 -codec copy edit/536.mp4
ffmpeg -i 570.mp4 -ss 00:06:00 -codec copy edit/570.mp4
ffmpeg -i 569.mp4 -ss 00:07:00 -codec copy edit/569.mp4
ffmpeg -i 568.mp4 -ss 00:08:00 -codec copy edit/568.mp4
ffmpeg -i 561.mp4 -ss 00:15:00 -codec copy edit/561.mp4
ffmpeg -i 560.mp4 -ss 00:11:30 -codec copy edit/560.mp4
ffmpeg -i 558.mp4 -ss 00:06:00 -codec copy edit/558.mp4
ffmpeg -i 550.mp4 -ss 00:08:30 -codec copy edit/550.mp4
ffmpeg -i 543.mp4 -ss 00:07:00 -codec copy edit/543.mp4
ffmpeg -i 540.mp4 -ss 00:09:00 -codec copy edit/540.mp4
ffmpeg -i 538.mp4 -ss 00:07:30 -codec copy edit/538.mp4
ffmpeg -i 567.mp4 -ss 00:14:50 -codec copy edit/567.mp4
ffmpeg -i 557.mp4 -c copy -ss 00:21:00 -to 1:07:00 edit/557.mp4
}

ffmpeg -i 503.mp4 -ss 00:05:20 -codec copy edit/503.mp4
ffmpeg -i 501.mp4 -ss 00:02:30 -codec copy edit/501.mp4
ffmpeg -i 495.mp4 -ss 00:14:30 -codec copy edit/495.mp4
ffmpeg -i 493.mp4 -ss 00:26:00 -codec copy edit/493.mp4
ffmpeg -i 455.mp4 -ss 00:13:20 -codec copy edit/455.mp4
ffmpeg -i 452.mp4 -ss 00:03:00 -codec copy edit/452.mp4
ffmpeg -i 432.mp4 -ss 00:07:00 -codec copy edit/432.mp4
ffmpeg -i 427.mp4 -ss 00:06:00 -codec copy edit/427.mp4
ffmpeg -i 415.mp4 -ss 00:06:20 -codec copy edit/415.mp4
ffmpeg -i 392.mp4 -ss 00:05:00 -codec copy edit/392.mp4
ffmpeg -i 504.mp4 -ss 00:13:00 -codec copy edit/504.mp4
