import time
from selenium import webdriver

#DRIVER_PATH = 'lib\\chromedriver.exe'
driver = webdriver.Chrome(executable_path='lib\\chromedriver.exe')
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('赤猫')
search_box.submit()
time.sleep(5)
driver.quit()
