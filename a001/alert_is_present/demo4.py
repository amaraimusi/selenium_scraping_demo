
# Selenium4の基本2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs 
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def document_initialised(driver):
    return driver.execute_script("return initialised")
 
DRIVER_PATH = 'lib\\chromedriver.exe'
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)

driver.implicitly_wait(10) # 暗黙的待機時間(秒)。要素が見つかるまでの最大待機時間
wait = WebDriverWait(driver, 10)
 

driver.get('https://youtu.be/Gwkx8DIWxsc') # Webサイトのページにアクセス
print(driver.title) # 現在のページタイトルを取得する
print(driver.current_url) #現在ページのURLを取得する
#driver.back() # ブラウザバック
#driver.forward() # ブラウザの次へボタン
#driver.refresh() # ブラウザを更新（ブラウザのリロード）


WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'search_query')))

search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys("ナスのペットボトル実験")
#sleep(5)
search_btn = driver.find_element(By.ID, 'search-icon-legacy')
search_btn.send_keys(Keys.RETURN)

#sleep(5)
driver.implicitly_wait(10)
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'yt-formatted-string')))
textElms = driver.find_elements(By.TAG_NAME, 'yt-formatted-string')
for e in textElms:
    print(e.text)


#search_box.send_keys(Keys.RETURN)

#elm = driver.find_element(By.NAME, 'q')

# 「Selenium」と入力して、「Enter」を押す
#elm.send_keys('ねこを捕まえる' + Keys.RETURN)

# driver.navigate("file:///race_condition.html")
# WebDriverWait(driver).until(document_initialised)
# el = driver.find_element(By.TAG_NAME, "p")
# assert el.text == "Hello from JavaScript!"

print('Success!')
# ブラウザを閉じる
#driver.quit()
