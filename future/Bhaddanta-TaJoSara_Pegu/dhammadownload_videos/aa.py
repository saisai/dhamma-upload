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

# To prevent download dialog
#profile = webdriver.FirefoxProfile()
#profile.set_preference('browser.download.folderList', 2) # custom location
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.download.dir', '/tmp')
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
'''
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", r"/e/dhamma-upload/future/Bhaddanta-TaJoSara_Pegu/dhammadownload_videos/")
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
profile.set_preference("browser.download.useDownloadDir", True);
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf");
profile.set_preference("pdfjs.disabled", True);
#profile.update_preferences()
'''
profile = webdriver.FirefoxProfile()
	
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('app.update.auto', False)
profile.set_preference('app.update.enabled', False)
profile.set_preference('app.update.silent', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
profile.set_preference('xpinstall.signatures.required', False)

'''
options.set_preference("browser.download.folderList", 2);
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", r"/e/dhamma-upload/future/Bhaddanta-TaJoSara_Pegu/dhammadownload_videos/");
options.set_preference("browser.download.useDownloadDir", True);
options.set_preference("browser. download. lastDir", r"/e/dhamma-upload/future/Bhaddanta-TaJoSara_Pegu/dhammadownload_videos/");
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf");
options.set_preference("pdfjs.disabled", True); #  // disable the built-in PDF viewer
'''
#opts = FirefoxOptions()
options = FirefoxOptions();
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path=r'/e/geckodriver/geckodriver.exe')

#browser = webdriver.Firefox(profile)

#print(dir(options))
#print(options.preferences)

browser.get("https://app.box.com/s/5u3ziopcpdsdjhf184q2vjyzz5my84di?fbclid=IwAR12oCoIjFduXOAZfGV0Vq0H0QWqsTPoogkk2ckT0QVeV9KOwFmccUflZ1U")
browser.find_element_by_xpath("//button/span/span").click()

#browser.find_element_by_id('exportpt').click()
#browser.find_element_by_id('exporthlgt').click()
#driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click()
#browser.find_elements_by_xpath("//button[@title='Download']").click()

#aa = browser.find_element_by_name('Download').click()
#print(type(aa))
#print(aa)