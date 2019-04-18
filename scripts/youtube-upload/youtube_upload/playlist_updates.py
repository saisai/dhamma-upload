#!/usr/bin/env python


import os
import sys
#from io import open

import googleapiclient.errors
import oauth2client
from googleapiclient.errors import HttpError

from . import auth
from . import lib


debug = lib.debug


# modified start         
def get_youtube_handler():
    """Return the API Youtube object."""
    options = {}
    home = os.path.expanduser("~")
    default_credentials = os.path.join(home, ".youtube-upload-credentials.json")
    #client_secrets = options.client_secrets or os.path.join(home, ".client_secrets.json")
    #credentials = options.credentials_file or default_credentials
    client_secrets = os.path.join(home, ".client_secrets.json")
    credentials = default_credentials    
    debug("Using client secrets: {0}".format(client_secrets))
    debug("Using credentials file: {0}".format(credentials))
    #get_code_callback = (auth.browser.get_code
        #if options.auth_browser else auth.console.get_code)
    get_code_callback = auth.browser.get_code
    return auth.get_resource(client_secrets, credentials,
        get_code_callback=get_code_callback)

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage   
        
def add_video_to_existing_playlist(youtube, playlist_id, video_id):
    """Add video to playlist (by identifier) and return the playlist ID."""
    lib.debug("Adding video to playlist: {0}".format(playlist_id))
    return youtube.playlistItems().insert(part="snippet", body={
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": video_id,
            }
        }
    }).execute()
        
def add_video_to_playlist(youtube, args, privacy="public"):
    """Add video to playlist (by title) and return the full response."""
    video_id = args['video_id']
    playlist_id = args['playlist_id']
    
    print(video_id)
    #print(type(args))
    
    if playlist_id:
        return add_video_to_existing_playlist(youtube, playlist_id, video_id)
    else:
        lib.debug("Error adding video to playlist")         
	      
  


def main(args):
    #print(args)
    
    args = args
    #print(args)
    youtube = get_youtube_handler()
    
    try:
        if youtube:
            add_video_to_playlist(youtube, args)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
        print('Tag "%s" was added to video id "%s".' % (args.add_tag, args.video_id))
    

def run():
    titles = [title.strip('\n') for title in open('update_playlist.txt', 'r')]
    
    playlist_id = "PLANgBzSjRA6PD-hnW8--eK61w5GTtH_8e"
    
    for title in titles:
        #print(title.split('|||')[0])
        aa_id = title.split('|||')[0]
        
        new_test = {'video_id':aa_id,
                'playlist_id':playlist_id
            }
        main(
        new_test
        
        )

# modified end        
