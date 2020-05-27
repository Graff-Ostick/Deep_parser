from bs4 import BeautifulSoup as bs
import requests

url = "https://login.aliexpress.ru/express/buyer_login_ae.htm"


req = requests.get(url)
session = requests.Session().get(url)
cooki = session.cookies.get_dict()

data = dict(req.headers)

#for i in range(len(data)):
#    print(data[i])

#--------key value of cookies
for key,val in data.items():
    print(key,val)
