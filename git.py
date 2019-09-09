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
        
        
        
        
# https://shapeshed.com/unix-cut/
# https://gitguide.readthedocs.io/en/latest/gitguide/
# https://itnext.io/become-a-git-pro-in-just-one-blog-a-thorough-guide-to-git-architecture-and-command-line-interface-93fbe9bdb395
# https://gist.github.com/mzabriskie/6631607
# https://coderwall.com/p/grmruq/git-status-on-all-repos-in-folder
# http://queirozf.com/entries/python-3-subprocess-examples