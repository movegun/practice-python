from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

def stop(float):
    time.sleep(float)
    
#(1) 드라이버 준비
chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = 'https://www.instagram.com/'
driver.get(url)
my_keyword = "#봄"

#my_id = "wjddmlcks000"
#my_pw = "java1234"
my_id = "m0ve_gun"
my_pw = "wozm2006"
stop(2)
#(2) 자동 로그인


insta_id = driver.find_element(By.NAME,'username')
insta_pw = driver.find_element(By.NAME,'password')
insta_id.send_keys(my_id)
stop(5)
insta_pw.send_keys(my_pw)
stop(5)
insta_pw.send_keys(Keys.ENTER)
stop(5)
info_later = driver.find_element(By.CLASS_NAME,'sqdOP.yWX7d.y3zKF')
info_later.click()
stop(5)
info_later2 = driver.find_element(By.CLASS_NAME,'_a9--._a9_1')
info_later2.click()
stop(5)


search_box = driver.find_element(By.CLASS_NAME,"_aawh._aawj._aauy")
search_box.send_keys(my_keyword)
stop(3)
search_box.send_keys(Keys.ARROW_DOWN)
stop(0.1)
search_box.send_keys(Keys.ARROW_DOWN)
stop(0.1)
search_box.send_keys(Keys.ARROW_DOWN)
stop(0.1)
search_box.send_keys(Keys.ARROW_DOWN)
stop(0.1)
search_box.send_keys(Keys.ARROW_DOWN)
stop(0.1)
search_box.send_keys(Keys.ENTER)
stop(5)

#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
post = driver.find_element(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._a6hd")
post.click()
#print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
time.sleep(5)
post_tags=[]

section = "번째 게시물의 태그"
post_count = 1
for i in range(10):
    post_tags.append(str(post_count)+section)
    data = driver.find_element(By.CLASS_NAME,'_a9zs')
    including_tags = data.text

    tags_having_hash = re.findall('#[A-Za-z0-9가-힣]+',including_tags)
    tag = ''.join(tags_having_hash).replace("#"," ")
    tags = tag.split()
    
    for a_tag in tags:
        post_tags.append(a_tag)
        
    print(post_tags)
    post_body = driver.find_element(By.CLASS_NAME,'_9dls.js-focus-visible._aa4c')
    post_body.send_keys(Keys.ARROW_RIGHT)
    post_count=post_count+1
    stop(3)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib
from collections import Counter

matplotlib.rcParams['font.family'] = "Hancom Gothic Bold"

mask = Image.new("RGBA",(2555,2275), (255,255,255)) #(2555,2575)는 사진 크기, (255,255,255)는 색을의미
image = Image.open('C:/LDG/PyAdvanced/preData/love.png').convert("RGBA")
x,y = image.size
mask.paste(image,(0,0,x,y),image)
mask = np.array(mask)

counts = Counter(post_tags)
top_50_tags = counts.most_common(50)

wc = WordCloud(font_path='Hancom Gothic Bold', background_color="white", width=800, height=600,mask=mask,colormap='prism')
cloud = wc.generate_from_frequencies(dict(top_50_tags))
plt.figure(figsize = (10, 10))
plt.axis('off')
plt.imshow(cloud)
plt.show()
driver.close()