
deletes = [str(f.strip('\n')) for f in open('delete.txt', 'r')]
#print(deletes)

files = [f.strip('\n') for f in open('titles_links.txt', 'r')]

with open('new.txt', 'w') as out:
    count = 2344
    for f in files:
        if f.split('|')[0] not in deletes:
            print('{}.mp3|{}|{}\n'.format(count, f.split('|')[1], f.split('|')[2]))
            out.write('{}.mp3|{}|{}\n'.format(count, f.split('|')[1], f.split('|')[2]))
            count += 1
    #else:

    

    #count += 1
