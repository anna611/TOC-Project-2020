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
import os
#find img url(a = 1-> dog,a = 2 -> cat)
def crawler_img(i,a):
    print(a)
    if a == 1:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("–window-size=1024,1024")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=1")
        browser.execute_script('window.scrollTo(0,300);')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        browser.execute_script("window.scrollTo(0,{0});".format(300*i))
        soup = BeautifulSoup(browser.page_source, "html.parser")
        doc = soup.find('li',id = str(i+1))
        imgs = doc.find('img')
        if 'src' in imgs.attrs:
            if imgs['src'].endswith('.JPG') or imgs['src'].endswith('.jpg') or imgs['src'].endswith('.png'):
                return("https://asms.coa.gov.tw/Amlapp"+imgs['src'][2:])
    if a == 2:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("–window-size=1024,1024")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=2")
        browser.execute_script('window.scrollTo(0,300);')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        browser.execute_script("window.scrollTo(0,{0});".format(300*i))
        soup = BeautifulSoup(browser.page_source, "html.parser")
        doc = soup.find('li',id = str(i+1))
        imgs = doc.find('img')
        if 'src' in imgs.attrs:
            if imgs['src'].endswith('.JPG') or imgs['src'].endswith('.jpg') or imgs['src'].endswith('.png'):
                return("https://asms.coa.gov.tw/Amlapp"+imgs['src'][2:])
    browser.close()         
#find information url(a = 1-> dog,a = 2 -> cat)
def crawler_url(i,a):
    if a == 1:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("–window-size=1024,1024")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=1")
        browser.execute_script('window.scrollTo(0,300);')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        browser.execute_script("window.scrollTo(0,{0});".format(300*i))
        soup = BeautifulSoup(browser.page_source, "html.parser")
        doc = soup.find('li',id = str(i+1))
        ta = doc.find('a')
        return("https://asms.coa.gov.tw/Amlapp/APP/"+ta['href'])  

    if a == 2:    
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("–window-size=1024,1024")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=2")
        browser.execute_script('window.scrollTo(0,300);')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        browser.execute_script("window.scrollTo(0,{0});".format(300*i))
        soup = BeautifulSoup(browser.page_source, "html.parser")
        doc = soup.find('li',id = str(i+1))
        ta = doc.find('a')
        return("https://asms.coa.gov.tw/Amlapp/APP/"+ta['href']) 
    browser.close()