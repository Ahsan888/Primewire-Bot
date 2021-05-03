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


PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(PATH,options=options)


href_output =[]
f= open("links4.txt", "w")
l = open("links.txt", 'r')
driver.get("https://www.google.com/")

count2=0
for line in l:
    try:
        count2=count2+1
        driver.get(line)

        data = driver.find_element_by_class_name("actual_tab")
        data2 = data.find_elements_by_class_name("version-host")
        data3 = data.find_elements_by_class_name("propper-link")
        title = driver.find_element_by_class_name("titles")
        title1 = title.text

        #print(title1)
        year = driver.find_element_by_class_name("movie_info")
        year1 = driver.find_elements_by_tag_name("tr")
        data5 = year1[2].text
        data6=data5[-4:]
        #print(data5[-4:])
    except:
        time.sleep(120)
        count2 = count2 + 1
        driver.get(line)

        data = driver.find_element_by_class_name("actual_tab")
        data2 = data.find_elements_by_class_name("version-host")
        data3 = data.find_elements_by_class_name("propper-link")
        title = driver.find_element_by_class_name("titles")
        title1 = title.text

        #print(title1)
        year = driver.find_element_by_class_name("movie_info")
        year1 = driver.find_elements_by_tag_name("tr")
        data5 = year1[2].text
        data6 = data5[-4:]
        #print(data5[-4:])


    list1 = []
    a = 1
    for i in data2:


        #print(i.text)
        if i.text == "streamtape.com":
            try:
                #print(title1)
                #print(i.text)
                list1.append(data3[data2.index(i)-1].get_attribute("href"))
                list1.append(title1)
                list1.append(data6)
                #print(data3[data2.index(i) - 1].get_attribute("href"))
                driver.get(data3[data2.index(i) - 1].get_attribute("href"))
                time.sleep(2)
                f.write(driver.current_url)
                f.write(":")
                f.write(title1)
                f.write(":")
                f.write(data6)
                f.write('\n')
                a=2
                driver.get(line)
                break
            except:
                pass

    if a == 1:
        #print(a)
        for i in data2:
            if i.text == "mixdrop.co":
                #print(i.text)

                try:
                    list1.append(data3[data2.index(i)].get_attribute("href"))
                    #print(data3[data2.index(i) - 1].get_attribute("href"))
                    driver.get(data3[data2.index(i) - 1].get_attribute("href"))
                    time.sleep(2)
                    f.write(driver.current_url)
                    f.write(":")

                    f.write(title1)
                    f.write(":")
                    f.write(data6)
                    f.write('\n')
                    driver.get(line)
                    break

                except:

                    pass
            else:
                pass



        else:

            pass

f.close()