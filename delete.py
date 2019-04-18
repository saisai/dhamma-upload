#!/usr/bin/env python
# coding=utf-8
import subprocess
import os
 
## call date command ##
p = subprocess.Popen("find . -name 'raw_json_title.txt'", stdout=subprocess.PIPE, shell=True)
 
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
## or None, if no data should be sent to the child.
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
#print("Command output : ", output)
for data in output.decode('utf-8').split():
    if r'/future/' not in data:
        print(data)
        os.remove(data)

print("\nCommand exit status/return code :", p_status)

# https://www.cyberciti.biz/faq/python-run-external-command-and-get-output/