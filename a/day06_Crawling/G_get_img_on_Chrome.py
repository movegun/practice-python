from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib.request
import time

chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'
driver.get(url)

my_keyword="런커배스"
el_photo_search = driver.find_element("name","q")
el_photo_search.send_keys(my_keyword)
el_photo_search.send_keys(Keys.ENTER) # Enter 대신 Return = shift+enter 옛날 문화임

el_imgs = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')
el_img0 = el_imgs[0]
el_img0.click()

time.sleep(1)

el_img0_big = driver.find_element(By.CSS_SELECTOR,'.n3VNCb.KAlRDb')
el_img0_url = el_img0_big.get_attribute("src")
print("-----------------------------------------------------------------")
#print(el_img0_url)

import os

if not os.path.exists("download"):
    os.makedirs("download")

urllib.request.urlretrieve(el_img0_url,'download/BigBass.png')

if os.path.exists('download/BigBass.png'):
    driver.close()
    print("Driver.close 댐Driver.close 댐Driver.close 댐Driver.close 댐")