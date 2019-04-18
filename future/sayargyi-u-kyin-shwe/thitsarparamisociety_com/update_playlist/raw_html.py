#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup

# get playlist from youtube

html = open('playlist_org.txt').read()


      
soup = BeautifulSoup(html, 'html.parser')
'''
for data in soup.find_all('ytd-playlist-video-renderer'):
    #print(data.find('yt-formatted-string'))
    #print(data.find('a', attrs={'id':'thumbnail','class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'}).get('href'))
    try:
    
        a_result = data.find('a', attrs={'id':'thumbnail','class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'}).get('href')
        id = a_result.split('&')[0].split('=')[1]
        time = data.find('span', attrs={'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).get_text().strip()
        title = data.find('span', attrs={'id': 'video-title'}).get_text().strip()
        print('{}|||{}|||{}\n'.format(id, time, title))
        #f.write('{}|||{}|||{}\n'.format(id, time, title))
    except AttributeError as err:
        print(err, 'err')
'''

with open('new_file_test_today.txt', 'w') as f:
    for data in soup.find_all('ytd-playlist-video-renderer'):
        #print(data.find('yt-formatted-string'))
        #print(data.find('a', attrs={'id':'thumbnail','class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'}).get('href'))
        try:
            
            a_result = data.find('a', attrs={'id':'thumbnail','class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'}).get('href')
            id = a_result.split('&')[0].split('=')[1]
            time = data.find('span', attrs={'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).get_text().strip()
            title = data.find('span', attrs={'id': 'video-title'}).get_text().strip()
            f.write('{}|||{}|||{}\n'.format(id, time, title))
        except AttributeError as err:
            print(err, 'err')

