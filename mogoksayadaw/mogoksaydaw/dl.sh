#!/bin/bash

#youtube-dl --extract-audio --audio-format mp3 -o "%(playlist_index)s-%(title)s.%(ext)s" https://www.youtube.com/playlist?list=PLkAlGChAwhhzgGvAE3bSxho2ML5h5NK2h
youtube-dl --playlist-start 120 -c --extract-audio --audio-format mp3 -o "%(playlist_index)s.%(ext)s" https://www.youtube.com/playlist?list=PLkAlGChAwhhzgGvAE3bSxho2ML5h5NK2h
