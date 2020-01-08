#!/usr/bin/env python
# coding=utf-8
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
from selenium.webdriver import FirefoxOptions

driver = '../geckodriver'

#1293.mp4|https://www.facebook.com/bhikkhusumana/videos/2453665218254850/
#link = 'https://www.facebook.com/bhikkhusumana/videos/2453665218254850/'
#link = 'https://www.facebook.com/bhikkhusumana/videos/2744538512333578/'
link = 'https://m.facebook.com/story.php?story_fbid=2744538512333578&id=467655660084925'
exec_path = r'%s' %  driver

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts, executable_path=exec_path)
#driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
#driver = webdriver.Firefox(firefox_options=opts)
#driver.get(mp3file.split('|')[1])
#replace = mp3file.split('|')[1].replace("www", "m", 1) 
driver.get(link)
#print(driver.title)
#print(driver)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')


print(soup.title.get_text())
#print(soup.find('div', attrs = {'class': 'story_body_container'}))



