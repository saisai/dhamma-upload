import socket

try:
    import httplib
except ImportError:
    import http.client as httplib

import googleapiclient.errors
import apiclient.http
import httplib2

from . import lib

RETRIABLE_EXCEPTIONS = [
    socket.error, IOError, httplib2.HttpLib2Error, httplib.NotConnected,
    httplib.IncompleteRead, httplib.ImproperConnectionState,
    httplib.CannotSendRequest, httplib.CannotSendHeader,
    httplib.ResponseNotReady, httplib.BadStatusLine,
]
'''
def _upload_to_request(request, progress_callback):
    """Upload a video to a Youtube request. Return video ID."""
    while 1:
        status, response = request.next_chunk()
        if status and progress_callback:
            progress_callback(status.total_size, status.resumable_progress)
        if response:
            if "id" in response:
                return response['id']
            else:
                raise KeyError("Expected field 'id' not found in response")

def upload(resource, path, body, chunksize=4*1024*1024, 
        progress_callback=None, max_retries=10):
    """Upload video to Youtube. Return video ID."""
    body_keys = ",".join(body.keys())
    media = apiclient.http.MediaFileUpload(path, chunksize=chunksize, 
        resumable=True, mimetype="application/octet-stream")
    request = resource.videos().insert(part=body_keys, body=body, media_body=media)
    upload_fun = lambda: _upload_to_request(request, progress_callback)
    return lib.retriable_exceptions(upload_fun, 
        RETRIABLE_EXCEPTIONS, max_retries=max_retries)
'''      
def update_video(youtube, args):
  # Call the API's videos.list method to retrieve the video resource.
  videos_list_response = youtube.videos().list(
    id=args.video_id,
    part='snippet'
  ).execute()

  # If the response does not contain an array of 'items' then the video was
  # not found.
  if not videos_list_response['items']:
    print('Video "%s" was not found.' % args.video_id)
    sys.exit(1)

  # Since the request specified a video ID, the response only contains one
  # video resource. This code extracts the snippet from that resource.
  videos_list_snippet = videos_list_response['items'][0]['snippet']

  # Set video title, description, default language if specified in args.
  if args.title:
    videos_list_snippet['title'] = args.title
  if args.description:
    videos_list_snippet['description'] = args.description

  # Preserve any tags already associated with the video. If the video does
  # not have any tags, create a new array. Append the provided tag to the
  # list of tags associated with the video.
  if 'tags' not in  videos_list_snippet:
    videos_list_snippet['tags'] = []
  if args.tags:
    videos_list_snippet['tags'] = args.tags.split(',')
  elif args.add_tag:
    videos_list_snippet['tags'].append(args.add_tag)

  print(videos_list_snippet);

  # Update the video resource by calling the videos.update() method.
  videos_update_response = youtube.videos().update(
    part='snippet',
    body=dict(
      snippet=videos_list_snippet,
      id=args.video_id
    )).execute()

  print('The updated video metadata is:\n' +
        'Title: ' + videos_update_response['snippet']['title'] + '\n')
  if videos_update_response['snippet']['description']:
    print(('Description: ' +
           videos_update_response['snippet']['description'] + '\n'))
  if videos_update_response['snippet']['tags']:
    print(('Tags: ' + ','.join(videos_update_response['snippet']['tags']) + '\n'))        
