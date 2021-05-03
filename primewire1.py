# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:15:46 2021

@author: Lenovo
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.options
import time
import os
from selenium.webdriver.chrome.options import Options

f=open('links.txt','w')
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(PATH,options=options)
driver.get("https://www.primewire.li/movies")
time.sleep(120)
list_1=[]
for i in range(1,1600):
    driver.get("https://www.primewire.li/?page="+str(i)+"&type=movie")
    data1=driver.find_elements_by_class_name("index_item")
    for i in data1:
        data2= i.find_element_by_tag_name("a")
        list_1.append(data2.get_attribute("href"))
        f.write(data2.get_attribute("href"))
        f.write('\n')
f.close()