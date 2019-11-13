import os
import os.path

import inspect
from pathlib import Path


def _get_input(name):
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / name
    
def read_line(name="input.txt"):
    with open(_get_input(name)) as f:
        return next(f).strip("\n")


def read_lines(name="input.txt"):
    with open(_get_input(name)) as f:
        return [l for l in (l.strip("\n") for l in f) if l]
        
        
	    

# To remove the NoneType from the file
duration = [f.strip('\n') for f in open('duration.txt')]

finished = [f.strip('\n') for f in open('finished.txt')]

#print(duration)

new_duration = [f for f in duration if f.split('|')[2] == 'NoneType']
edited_duration = [f for f in duration if f.split('|')[2] != 'NoneType']

#print(new_duration)

#print(set(finished) - set(new_duration))


for get_duration in edited_duration:
    with open('duration_edited.txt', 'a') as f:
        f.write(get_duration)
        f.write('\n')


seen_duration = set()
seen_finished = {}
for link in new_duration:
    for cmp_link in finished:
        #print(link.split('|')[1] in cmp_link.split('|')[1])
        if link.split('|')[1] in cmp_link.split('|')[1]:
            print(link)
            print(cmp_link)
            with open('redo.txt', 'a') as f:
                seen_duration.add(cmp_link)
                f.write(cmp_link)
                f.write('\n')
                
for cmp_link in finished:
    
    if cmp_link not in seen_duration:        
        with open('finished_edited.txt', 'a') as f:
            seen_duration.add(cmp_link)
            f.write(cmp_link)
            f.write('\n')                

'''
else:
            #if cmp_link in seen_duration or cmp_link not in seen_finished:
            if cmp_link not in seen_finished.keys() and cmp_link in seen_duration:
                with open('finished_edited.txt', 'a') as f:
                    f.write(cmp_link)
                    f.write('\n')
                    seen_finished.update({cmp_link:1})        
'''

