
# Selenium4のalertダイアログ制御 | アラート待機、アラートテキスト取得
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs 
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
DRIVER_PATH = 'C:\\Users\\user\\git\\selenium_scraping_demo\\lib\\chromedriver.exe'
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.implicitly_wait(10) # 暗黙的待機時間(秒)。要素が見つかるまでの最大待機時間

driver.get('https://amaraimusi.sakura.ne.jp/selenium_scraping_demo/a001/alert_is_present/demo.html') # Webサイトのページにアクセス

elm1 = driver.find_element(By.ID, 'test1')
print(elm1.text)

alert = WebDriverWait(driver, 15).until(EC.alert_is_present()) # アラートが表示されるまで待機（この例では最大15秒まで待機）
alert_text = alert.text # alertのテキストを取得
print(alert_text)
alert.accept() # alertのボタンをクリック
sleep(1) # alert_is_presentだけでは不十分。１秒だけスリープする必要がある。

elm1 = driver.find_element(By.ID, 'test1')
print(elm1.text)

elm1 = driver.find_element(By.ID, 'test2')
print(elm1.get_attribute('src'))

print('Success!')

driver.quit() # ブラウザを閉じる
