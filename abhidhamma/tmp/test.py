files = [f.strip('\n') for f in open('links.txt', 'r') if len(f) > 2]
text = [f.strip('\n') for f in open('text.txt', 'r') if len(f) > 2]


count = 503

with open('titles_links.txt', 'w') as f:
    for ff, tt in zip(files, text):
        print(ff)
        f.write('{:03d}.mp4|{}|{}\n'.format(count, ff, tt))
        count += 1