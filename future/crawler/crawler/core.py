
from bs4 import BeautifulSoup as bs4

'''
param -> get_url.txt
'''
def get_html_mp4(param):
    text = open(param, 'r').read()

    soup = bs4(text, 'html.parser')

    count = 1
    with open('titles_links.txt', 'w') as fd:

        for key in soup.find_all('a'):
            if '.mp4' in key.get('href'):
                counter = '{:03d}'.format(count)
                fd.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split())))

            count += 1
            
'''
param -> get_url.txt
'''
def get_html_mp3(param):
    text = open(param, 'r').read()

    soup = bs4(text, 'html.parser')

    count = 1
    with open('titles_links.txt', 'w') as fd:

        for key in soup.find_all('a'):
            if '.mp3' in key.get('href'):
                counter = '{:03d}'.format(count)
                fd.write('{}.mp3|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split())))

            count += 1            



