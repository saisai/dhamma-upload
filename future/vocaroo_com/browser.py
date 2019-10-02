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



print(os.getcwd())
#print(sys.argv[1])

data = [f.strip('\n') for f in open('links.txt')]
for f in data:
    print(f)
    result = f.split('|')
    print(result[1].split('/')[4])
    url = 'https://s0.vocaroo.com/media/download_temp/Vocaroo_{}.mp3'.format(result[1].split('/')[4])
    #print(url)
    command = "wget|-c|--no-check-certificate|-O|{}|{}".format(result[0], url)
    completed = subprocess.run(command.split('|'))
    print(completed)
    time.sleep(1)

#command = "wget|-c|--no-check-certificate|-O|{}|{}".format('a.pdf', sys.argv[1])
#command = "wget|-c|--no-check-certificate|-O|{}|{}".format('001.mp3', 'https://s0.vocaroo.com/media/download_temp/Vocaroo_s0B9t7mJumew.mp3')


#print(command.split('|'))

#completed = subprocess.run(command.split('|'))
#print(completed)

'''

profile = webdriver.FirefoxProfile()

profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('app.update.auto', False)
profile.set_preference('app.update.enabled', False)
profile.set_preference('app.update.silent', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf,application/octet-stream,application/vnd.ms-excel')
profile.set_preference('xpinstall.signatures.required', False)
profile.set_preference("pdfjs.disabled", True)


options = FirefoxOptions();
prefs = {'download.default_directory': os.getcwd()}

options.add_argument("--headless")
#browser = webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path=r'/e/geckodriver/geckodriver.exe')
browser = webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path=r'/home/walen/shared/pdf_to_images/geckodriver')

#browser = webdriver.Firefox(profile)

#print(dir(options))
#print(options.preferences)

#browser.get("https://app.box.com/s/5u3ziopcpdsdjhf184q2vjyzz5my84di?fbclid=IwAR12oCoIjFduXOAZfGV0Vq0H0QWqsTPoogkk2ckT0QVeV9KOwFmccUflZ1U")

browser.get(sys.argv[1])
#browser.find_element_by_xpath("//button/span/span").click()

print('finished one')
tester = True
while tester:
    print('while')
    for fname in os.listdir(os.getcwd()):
        print(fname)
        if fname.endswith('.pdf') and os.stat(fname).st_size != 0:
            print(fname) 
            print('size ', os.stat(fname).st_size)
            tester = False 
            print('moving file', fname)
            os.system('%s "%s" %s' % ('mv', fname, 'a.pdf' ))
            #tester = False 
        else:
            time.sleep(1)
        
browser.close()
'''