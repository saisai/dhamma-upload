
ids = [f.strip('\n') for f in open('convert.txt')]
#print(ids)

titles = [f.strip('\n') for f in open('no_time_id_title.txt')]
#print(titles)

for data in titles:
    if data.split('|||')[0]+'.mp3' in ids:
        print(data.split('|||')[2])
