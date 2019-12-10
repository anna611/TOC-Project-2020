import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Firefox()
browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=1")
soup = BeautifulSoup(browser.page_source)
browser.execute_script("window.scrollTo(0,500)")
imgs = soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if img['src'].endswith('.JPG') or img['src'].endswith('.jpg'):
            print("https://asms.coa.gov.tw/Amlapp"+img['src'][2:])
browser.close()