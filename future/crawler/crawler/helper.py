import os
import sys
import collections
import json
import shutil
import subprocess


# Change path unix to window
# \e\dhamma-upload\future\PilotSayadawJeYaPandita\fb
# E:\dhamma-upload\future\PilotSayadawJeYaPandita\fb\
# https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python/8220141

def change_unix_to_window(param):
    #print(param)
    #print(param.split('/')[1:])
    result = param.split('/')[1:]
    no_drive = param.split('/')[2:]
    #print('\\'.join(no_drive))
    no_drive_result = '\\'.join(no_drive)
    drive = result[0].upper() + ':\\'
    final_path = drive + no_drive_result
    return final_path
    
    
    