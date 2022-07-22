from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib.request

chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'
driver.get(url)

my_keyword="런커배스"
el_photo_search = driver.find_element("name","q")
el_photo_search.send_keys(my_keyword)
el_photo_search.send_keys(Keys.ENTER) # Enter 대신 Return = shift+enter 옛날 문화임
el_imgs = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')

import os
import time

def create_directory(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("{} 라는 디렉토리 생성 실패".format(dir))

create_directory("downloads")
count = 1
for el_img in el_imgs:
    try:
        el_img.click()
        time.sleep(3)
        el_img_big = driver.find_element(By.CSS_SELECTOR,'.n3VNCb.KAlRDb')
        el_img_url = el_img_big.get_attribute("src")
        urllib.request.urlretrieve(el_img_url,"downloads/"+str(count)+".jpg")
        count = count+1
    except: # 다운로드 안되면 보안? 블로그막아둠 ? 등등
        pass

driver.close()