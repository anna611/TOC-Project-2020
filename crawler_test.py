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
   
browser = webdriver.Chrome(./chromedriver)
browser.get("https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Adopt&AnimalType=1")
browser.execute_script('window.scrollTo(0,300);')
soup = BeautifulSoup(browser.page_source, "html.parser")
def craweler_id(i,text):
    browser.execute_script("window.scrollTo(0,{0});".format(300*i))
    soup = BeautifulSoup(browser.page_source, "html.parser")
    doc = soup.find('li',id = str(i))
    if str(doc).find('性別：</dt><dd>'+text) != -1:
        return 1
def craweler_img(i):
    imgs = doc.find('img')
    if 'src' in imgs.attrs:
        if imgs['src'].endswith('.JPG') or imgs['src'].endswith('.jpg') or imgs['src'].endswith('.png'):
            return("https://asms.coa.gov.tw/Amlapp"+imgs['src'][2:])

def craweler_url(i):
    browser.execute_script("window.scrollTo(0,{0});".format(300*i))
    soup = BeautifulSoup(browser.page_source, "html.parser")
    doc = soup.find('li',id = str(i))
    a = doc.find('a')
    return("https://asms.coa.gov.tw/Amlapp/APP/"+a['href'])       
    
browser.close()