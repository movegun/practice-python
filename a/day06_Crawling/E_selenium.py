from selenium import webdriver


chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
url = 'http://google.com'

driver.get(url)
driver.find_element