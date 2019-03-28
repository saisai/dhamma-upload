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
    
def date_difference(first_date, second_date):
    # https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
    from datetime import date 
    #print(type(first_date))
    
    first_date = first_date.split(',')
    second_date = second_date.split(',')
    
    #first_date = 
    first_date =  date(int(first_date[0]), int(first_date[1]), int(first_date[2]) ) # year, month, day
    second_date =  date(int(second_date[0]), int(second_date[1]), int(second_date[2]) ) # year, month, day
    #second_date =  date(int(second_date)) # year, month, day
    delta = second_date - first_date
    return delta
    
def get_percent():
    cmd = "df -h | grep media_rw | awk '{print $5}'"
    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode()
    print(output.split('%')[0])
    return int(output.split('%')[0])
    # https://stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes
    # https://www.programcreek.com/python/example/78/subprocess.PIPE
    # subprocess.check_output("df -h | grep Avail | awk '{print $2}'", shell=True).decode('utf-8')
    # https://docs.python.org/3/library/subprocess.html

    
    
       
    
    
    