
titles = [f.strip('\n\n\n') for f in open('new_titles.txt', 'r') if len(f) > 2]
#print(titles)
print(len(titles))
'''
for tt in titles:
    print(tt)
'''

links = [f.strip('\n') for f in open('new_links.txt', 'r') if len(f) > 2]
#print(links)
print(len(links))

"""
with open('titles_links.txt', 'w') as f:
    count = 438
    for link, title in zip(links, titles):
        counter = '{:03d}'.format(count)
        f.write('{}.mp3|{}|{}\n'.format(counter, link, title))
        count += 1
"""   
    

"""

    
    for key in soup.find_all('a'):
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
"""
"""        
with open('file.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get('href')))

with open('titles.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get_text()))        
"""