#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
from selenium.webdriver import FirefoxOptions

exec_path = "geckodriver"

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts, executable_path=exec_path)
#driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
#driver = webdriver.Firefox(firefox_options=opts)
#driver.get("https://m.facebook.com/257435104635888/videos/468476757360061/")
driver.get("https://m.facebook.com/257435104635888/videos/601796416866420/")
#print(driver.title)
#print(driver)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
print(soup)
#print(soup.find('div', attrs={"class": "story_body_container"}).find('p').get_text())
#print(soup.find('div', attrs={"data-sigil": "feed-story-share-attachment"}))
#print(soup.find('meta', attrs={'name': 'description'}))
#print(soup.find('p'))
#print('text\n')
#print(soup.find('p').get_text())
