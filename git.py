#!/usr/bin/env python
# coding=utf-8

import subprocess
def runls():
    
    try:
        byteOutput = subprocess.check_output(['git', 'status', '-s'])
        return byteOutput.decode('UTF-8').rstrip()
    except subprocess.CalledProcessError as e:
        print("Error in ls -a:\n", e.output)
        return None

excluded_folders = [
                'future/crawler/crawler/__pycache__/',
                ]        
        
result = runls()      
bb = result.strip('\n').replace('??', '')
for f in bb.split('\n'):
    if f.strip() not in excluded_folders:
        print(f.strip())
        cp = subprocess.run(["git", "add", "%s" % (f.strip(), )])
        print(cp)
        
        
        
        
#print(type(result.split()))

#command = "$ for f in $(git status -s | cut -d '?' -f 3); do if; done"
#command = "git status -s | cut -d '?' -f 3"
#command = "git|status|-s|test|cut|-d|\"?\"|-f|3"
#command = "git|status|-s"

#modified_result = command.split('|')
#print(modified_result)
#modified_result[3]= '|'
#print(' '.join(modified_result))
#aa =' '.join(modified_result)
#print(aa)
#result = subprocess.run(modified_result)
#process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
#process = subprocess.Popen(aa, stdout=subprocess.PIPE)
#out, err = process.communicate()
#print(out)

#print(result.encode('utf-8'))


'''
from subprocess import Popen, PIPE
output = Popen(command,stdout=PIPE)
response = output.communicate()
print response
'''