#!/usr/bin/env python
# coding=utf-8
import os

if __name__ == '__main__':
    
    #Allows you to a relative import from the parent folder
    import os.path, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))    
    
    from youtube_upload import playlist_updates        
    playlist_updates.run()

    