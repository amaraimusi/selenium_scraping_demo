# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
# print('demo1')
# #driver = webdriver.Chrome()
# #DRIVER_PATH = 'C:\\Users\\user\\python3_8\\chromedriver_win32\\chromedriver.exe'
# DRIVER_PATH = 'lib\\chromedriver.exe'
# #driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#
# driver = webdriver.Chrome()
# driver.get(DRIVER_PATH)
#
# driver.get('https://www.google.com/')
#
#
# time.sleep(5)
# search_box = driver.find_element_by_name("q")
# search_box.send_keys('うなぎ犬')
# search_box.submit()
#
# elm = WebDriverWait(driver, 10).until(
#     driver.quit()
# )


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs 
 
DRIVER_PATH = 'lib\\chromedriver.exe'
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=DRIVER_PATH)
browser = webdriver.Chrome(service=chrome_service)
 
# Googleアクセス
browser.get('https://www.google.com/')

elm = browser.find_element(By.NAME, 'q')

# 「Selenium」と入力して、「Enter」を押す
elm.send_keys('犬を捕まえる' + Keys.RETURN)
 
# ブラウザを閉じる
# browser.quit()
