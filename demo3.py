

# Selenium4の基本
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs 
from time import sleep
 
DRIVER_PATH = 'lib\\chromedriver.exe'
 
# ドライバー指定でChromeブラウザを開く
chrome_service = fs.Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
 

driver.get('https://youtu.be/Gwkx8DIWxsc') # Webサイトのページにアクセス
print(driver.title) # 現在のページタイトルを取得する
print(driver.current_url) #現在ページのURLを取得する

sleep(5) #5秒スリープ　非推奨な方法　WebDriverWaitを使う方法が良いようだ。

search_box = driver.find_element(By.NAME, 'search_query') #検索テキストボックス要素を取得
search_box.send_keys("ナスのペットボトル実験")#検索テキストボックス要素にキーワードを入力
sleep(2)

search_btn = driver.find_element(By.ID, 'search-icon-legacy') # 検索ボタン要素を取得
search_btn.send_keys(Keys.RETURN) # 検索ボタン要素にてEnterキーボタンの押下イベントを発動

sleep(5)

# タグを指定して要素リストを取得する
textElms = driver.find_elements(By.TAG_NAME, 'yt-formatted-string')
for e in textElms:
    print(e.text) # 要素のテキストを取得(inner html）

print('Success!')

# ブラウザを閉じる
driver.quit()
