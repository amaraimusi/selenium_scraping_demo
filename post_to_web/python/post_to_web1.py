


import requests

# 送信データ
neko_name = "ボーシ猫"
neko_age = "0.5"
sendData = {'neko_name': neko_name, 'neko_age': neko_age}
   
images = {}
for i, f in enumerate(["imori.jpg", "tamamusi.jpg"]):
    tiw = open(f, "rb") # io.TextIOWrapper
    images[f] = tiw.read()
    
url = "http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php"
res = requests.post(url, data=sendData, files=images)
print(res.text)



# import requests
# url = "http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php"
#    
# # 送信データ
# neko_name = "ボーシ猫"
# neko_age = "0.5"
# sendData = {'neko_name': neko_name, 'neko_age': neko_age}
#   
# image = "imori.jpg"
# data = open(image, 'rb')
# file = {'file': data}
#   
# res = requests.post(url, data=sendData, files=file)
# print(res.text)



# import requests
# url = "http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php"
#   
# # 以下のAPIキーはダミー
# apikey = "APIKEY1234"
# apiid = "4107"
# payload = {'apikey': apikey, 'id': apiid}
#  
# image = "imori.jpg"
# data = open(image, 'rb')
# file = {'file': data}
#  
# res = requests.post(url, params=payload, files=file)
# print(res.text)





# import json
# import urllib.parse
# import urllib.request
# import requests
#   
# images = {}
# for i, f in enumerate(["imori.jpg", "tamamusi.jpg"]):
#     f = open(f, "rb")
#     print(f)
#     images[str(i)] = f.read()
#    
# url = "http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php"
# res = requests.post(url, files=images)
# print(res.text)





    
    
# import json
# import urllib.parse
# import urllib.request
# import requests
# 
# f = open("imori.jpg", "rb")
# reqbody = f.read()
# f.close()
#  
# url = "http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php"
# req = urllib.request.Request(
#     url,
#     reqbody,
#     method="POST",
#     headers={"Content-Type": "application/octet-stream"},
# )
#  
# with urllib.request.urlopen(req) as res:
#     html = res.read().decode("utf-8")
#     print(html)
# 
# print('OK')


# import urllib.request, urllib.parse
# data = {
#     "neko_name": "帽子猫",
#     "age": 0,
#     "memo": "弱弱しい猫ちゃんです。"
# }
# # ここでエンコードして文字→バイトにする！
# data = urllib.parse.urlencode(data).encode("utf-8")
# with urllib.request.urlopen("http://localhost/selenium_scraping_demo/post_to_web/web/post_to_web_page1.php", data=data) as res:
#    html = res.read().decode("utf-8")
#    print(html)