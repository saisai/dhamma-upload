import re 
import collections

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

test = [f.strip('\n') for f in open('no_time_id_title.txt')]

check_dup = []
for i in sorted(test, key=natural_keys):

    #print(i.split('|')[0])
    check_dup.append(i.split('|||')[0])
    
for key, val in dict(collections.Counter(check_dup).items()).items():
    print(key)
    if val > 1:
        print(key, val)

