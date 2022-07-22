from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = 'https://ko-kr.facebook.com/'
driver.get(url)

el_email = driver.find_element("id","email")
el_password = driver.find_element("id","pass")

my_fb_id =""
my_fb_password = ""
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
print(el_email)

el_email.send_keys(my_fb_id)
el_password.send_keys(my_fb_password)
#el_password.send_keys(Keys.ENTER)
