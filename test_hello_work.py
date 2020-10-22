import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='lib\\chromedriver.exe')
driver.get('https://www.hellowork.mhlw.go.jp/')
time.sleep(3)

elm = driver.find_element_by_link_text('求人情報検索')
elm.click()

elm = driver.find_element_by_name("nenreiInput") 
# elm.clear()
elm.send_keys('40')
time.sleep(3)
# 
elm = driver.find_element_by_id("ID_searchBtn") 
elm.click()

