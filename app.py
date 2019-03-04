import requests
from bs4 import BeautifulSoup
import pprint
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

item_list = []
price_list = []
url = "http://www.coupang.com/np/categories/176860?page=1"
result = requests.get(url, headers=headers)
soup_obj = BeautifulSoup(result.content, "html.parser")

div = soup_obj.findAll("div", {"class": "name"})

strong = soup_obj.findAll("strong", {"class": "price-value"})


for li in div:
    # print(div[li].text)
    item_list.append(li.text)

for li in strong:
    price_list.append(li.text)

for li in range(len(price_list)):
    print("item" + ": " + item_list[li] + "," + "price" + ": " + price_list[li])
