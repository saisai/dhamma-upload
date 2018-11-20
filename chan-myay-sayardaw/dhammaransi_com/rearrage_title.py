import re 

titles = [f.strip('\n') for f in open('titles_links_retired.txt')]
#print(titles)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text) ]


count = 1018

for title in sorted(titles, key=natural_keys):
    #print(title)
    print('{}.mp3|{}|{}'.format(count, title.split('|')[1], title.split('|')[2]))
    count += 1
