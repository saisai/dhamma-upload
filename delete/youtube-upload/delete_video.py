#!/usr/bin/env python
# coding=utf-8
import os
ids = [a.strip('\n') for a in open('delete_ids.txt', 'r')]


#playlist_id = "PLpC7LHUjztF5N3K_IBFQfjj92fIVMdQqF"
for video_id in ids:    
    os.system('{} --video_id="{}" '.format('python2 youtube_upload/delete_video.py', \
                video_id))