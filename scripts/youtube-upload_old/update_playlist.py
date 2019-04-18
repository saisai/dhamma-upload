#!/usr/bin/env python
# coding=utf-8
import os

'''
ids = [a.strip('\n') for a in open('youtube_id.txt', 'r')]
titles = [title.strip('\n') for title in open('youtube_title.txt', 'r')]

playlist_id = "PLpC7LHUjztF5N3K_IBFQfjj92fIVMdQqF"

for aa_id, title in zip(ids, titles):
    desc="""ေက်းဇူးေတာ္ရွင္အဂၢမဟာပ႑ိတ မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား
{}
source from https://www.thitsarparamisociety.com""".format(title)
    print(aa_id, title, desc)
    
    os.system('{} --video_id="{}" --playlist_id="{}" '.format('python2 youtube_upload/playlist_updates.py', \
                aa_id, playlist_id))
'''   
             
#titles = [title.strip('\n') for title in open('final_results.txt', 'r')]
titles = [title.strip('\n') for title in open('update_playlist.txt', 'r')]

playlist_id = "PLANgBzSjRA6OTvXADncglqKu-jyCyDOoo"
for title in titles:
    print(title.split('|||')[0])
    aa_id = title.split('|||')[0]
    
    os.system('{} --video_id="{}" --playlist_id="{}" '.format('python youtube_upload/playlist_updates.py', \
                aa_id, playlist_id))
    