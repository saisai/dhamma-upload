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
print(sys.argv[1])

profile = webdriver.FirefoxProfile()


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
browser.find_element_by_xpath("//button/span/span").click()

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
