#!/usr/bin/env python
# coding=utf-8
import os
ids = [a.strip('\n') for a in open('youtube_id.txt', 'r')]
titles = [title.strip('\n') for title in open('youtube_title.txt', 'r')]

playlist = "မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား"
for aa_id, title in zip(ids, titles):
    desc="""ေက်းဇူးေတာ္ရွင္အဂၢမဟာပ႑ိတ မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား
{}
source from https://www.thitsarparamisociety.com""".format(title)
    print(aa_id, title, desc)
    
    os.system('{} --video_id="{}" --title="{}" --description="{}" '.format('python2 youtube_upload/update_video_org.py', \
                aa_id, title, desc))