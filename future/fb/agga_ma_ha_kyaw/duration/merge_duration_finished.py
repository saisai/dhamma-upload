
duration = [f.strip('\n') for f in open('duration.txt')]

finished = [f.strip('\n') for f in open('finished.txt')]

#print(duration)
#print(finished)

for du, fi in zip(duration, finished):
    #print(du, fi)
    #print(fi.split('|')[-1].split('/')[-1])
    get_video_id = fi.split('|')[-1].split('/')[-1]
    #print(' '.join(du.split('|')).replace('videos', get_video_id))
    print( ' '.join(du.split('|')).replace('videos', get_video_id).replace(' ', '|') )

