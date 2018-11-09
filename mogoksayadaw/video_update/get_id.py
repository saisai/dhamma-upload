import re 

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


mp3s = [f.strip('\n') for f in open('must_work_2.txt', 'r')]
files = [f.strip('\n') for f in open('new_file_test.txt', 'r')]

cc = 1
counter = 1
for ff in files:
    if str(counter) in mp3s:
        print(cc)
        print(counter)
        print(ff.split('|||')[0])
        
        
        cc += 1
        
    counter += 1
    

