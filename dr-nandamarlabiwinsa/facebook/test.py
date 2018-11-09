from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
from selenium.webdriver import FirefoxOptions
import requests
import sys
import os
import time
from threading import Thread
from queue import Queue
import argparse
import binascii
import json


import subprocess
import datetime

import shutil

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
mp3file="https://www.facebook.com/1183243185031861/videos/712532012432970/"
driver.get(mp3file)

html = driver.page_source
#print(html)
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('div', attrs={'class': '_5pbx userContent _3576'}).get_text())

