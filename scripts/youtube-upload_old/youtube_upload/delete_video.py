#!/usr/bin/python

# This code sample creates a private playlist in the authorizing user's
# YouTube channel.
# Usage:
#   python playlist_updates.py --title=<TITLE> --description=<DESCRIPTION>

import argparse
import os
import sys 

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

import lib
import auth

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    
CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
    
def get_youtube_handler(options=None):
    """Return the API Youtube object."""
    home = os.path.expanduser("~")
    default_client_secrets = lib.get_first_existing_filename(
        [sys.prefix, os.path.join(sys.prefix, "local")],
        "share/youtube_upload/client_secrets.json")  
    default_credentials = os.path.join(home, ".youtube-upload-credentials.json")
    client_secrets = default_client_secrets or \
        os.path.join(home, ".client_secrets.json")
    credentials = default_credentials
    lib.debug("Using client secrets: {0}".format(client_secrets))
    lib.debug("Using credentials file: {0}".format(credentials))
    get_code_callback = (auth.browser.get_code 
        if options==None else auth.console.get_code)
    return auth.get_resource(client_secrets, credentials,
        get_code_callback=get_code_callback)

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage    

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            if value:
                good_kwargs[key] = value
    return good_kwargs
  
#def delete_video_to_existing(youtube, playlist_id, video_id):
def delete_video_to_existing(youtube, **kwargs):
    """Add video to playlist (by identifier) and return the playlist ID."""
    #lib.debug("Adding video to playlist: {0}".format(playlist_id))
    #return youtube.playlistItems().insert(part="snippet", body={
    '''
    return youtube.videos().delete(part="snippet", body={
        "snippet": {
            "resourceId": {
                "kind": "youtube#video",
                "videoId": video_id,
            }
        }
    }).execute()
    '''
    kwargs = remove_empty_kwargs(**kwargs)

    response = youtube.videos().delete(
        **kwargs
      ).execute()
    return print_response(response)
    
def print_response(response):
    print(response)
    
    
'''
def delete_video(youtube, args, privacy="public"):
    """Add video to playlist (by title) and return the full response."""
    video_id = args.video_id
    #playlist_id = args.playlist_id
    if video_id:
        return delete_video_to_existing(youtube, video_id)
        #return delete_video_to_existing(youtube, playlist_id, video_id)
    else:
        lib.debug("Error adding video to playlist")         
'''
  
if __name__ == '__main__':
           
  parser = argparse.ArgumentParser()
  parser.add_argument('--video_id', help='ID of video to update.',
    required=True)  
  #parser.add_argument('--playlist_id', help='Playlist of the video.')

  args = parser.parse_args()
  youtube = get_youtube_handler()

  try:
    if youtube:
      delete_video_to_existing(youtube, id=args.video_id)
  except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    print('Tag "%s" was added to video id "%s".' % (args.add_tag, args.video_id))
    
 
