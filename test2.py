import time
from selenium import webdriver

#DRIVER_PATH = 'lib\\chromedriver.exe'
driver = webdriver.Chrome(executable_path='lib\\chromedriver.exe')
driver.get('http://localhost/selenium_scraping_demo/web_app_test/test1.php')
time.sleep(3)
#elm = driver.find_element_by_partial_link_text('iki')
#elm.click()
#elm = driver.find_element_by_name("neko_name") 


# elm = driver.find_element_by_id("btn1") 
# elm.click()
# time.sleep(1)
# elm = driver.find_element_by_id("btn2") 
# elm.click()

#elm = driver.find_element_by_tag_name("input") 
#elm = driver.find_element_by_class_name("neko_class") 
#elm = driver.find_element_by_css_selector('input.neko_class')
#elm = driver.find_element_by_css_selector('div[data-id="101"] > input')
# elm = driver.find_element_by_css_selector('input.neko_class#neko1[name="neko_name"]')
# 
# 
# 
# #elm = driver.find_element_by_id("neko1") 
# #elm = driver.find_element_by_xpath("//input")
# elm.clear()
# elm.send_keys('クロ猫7')

elms = driver.find_elements_by_css_selector('#plant_list li')
for elm in elms:
    print(elm.text)

# elm.submit()

time.sleep(5)
driver.quit()
