import time
from selenium import webdriver

print('demo1')
#driver = webdriver.Chrome()
#DRIVER_PATH = 'C:\\Users\\user\\python3_8\\chromedriver_win32\\chromedriver.exe'
DRIVER_PATH = 'lib\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('Hello World')
search_box.submit()
time.sleep(5)
driver.quit()
