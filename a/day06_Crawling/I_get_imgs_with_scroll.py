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

import time
#스크롤을 내리면서 크롤링
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() #결과 더보기 버튼 
        except:
            break
    last_height = new_height

el_imgs = driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')

import os

def create_directory(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("{} 라는 디렉토리 생성 실패".format(dir))

create_directory("down")
count = 1
for el_img in el_imgs:
    try:
        el_img.click()
        time.sleep(1)
        el_img_big = driver.find_element(By.CSS_SELECTOR,'.n3VNCb.KAlRDb')
        el_img_url = el_img_big.get_attribute("src")
        urllib.request.urlretrieve(el_img_url,"down/"+str(count)+".jpg")
        count = count+1
    except: # 다운로드 안되면 보안? 블로그막아둠 ? 등등
        pass

driver.close()