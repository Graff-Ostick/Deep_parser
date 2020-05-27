from bs4 import BeautifulSoup as bs
import lxml
import requests
import json

#url_card = input("Please write url your shop card")
url_card = "https://aliexpress.ru/item/32806278955.html?spm=a2g0s.9042311.0.0.1dcf33ed6WOHxN"
#req = requests.Session().get(url_card)
url_card = requests.get(url_card)
html = bs(url_card.content, "html.parser")
csrf = html.select("script")
csrf = str(csrf[-3])
start = csrf.find("data:")+6
end = csrf.find("csrfToken")
csrf = csrf[start:end]
csrf = csrf.rstrip()[:-1]
js = json.loads(csrf)

print(js.get("priceModule").get("formatedPrice"))
#print(js.get("formatedAmount"))
#-------------------login----------------

"""url_login = "https://login.aliexpress.ru/"
sesion = requests.Session()
#r_get = requests.get(url_login)
#r_get = bs(r_get.content, 'html.parser')
data = {
    fm-login-id:"rusya1998shebak@gmail.com",
    fm-login-password:"1q2w3e4rR"
}
r_post = requests.post(url_login,params=data)
#r_post = bs(r_post.content,"html.parser")
print(r_post)

#csrf = csrf_bs.select('input',{'id':'UA_InputId'})
"""
