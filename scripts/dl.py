import subprocess

videos = [f.strip('\n') for f in open('new_dl.txt')]
files = [f.strip('\n') for f in open('file.txt')]
#print(videos)
#print(files)

for ff in files:
    if ff.split('||')[0].split('.')[0] in videos:
        print(ff.split('||')[0].split('.')[0])
        print(ff.split('||')[0])
        
        print(ff.split('||')[1])
        dest = ff.split('||')[0]
        line = ff.split('||')[1]
        command = "wget|--no-check-certificate|-O|{}|{}".format(dest, line)
        print(command)
        completed = subprocess.run(command.split('|'))
        print('returncode:', completed)        
        

