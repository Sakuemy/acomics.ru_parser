import requests
from bs4 import BeautifulSoup

url0 = "https://acomics.ru/~coma" # заменить на свое
print(url0)
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "cookie": "__utma=42127285.2002132981.1658240299.1658240299.1658240299.1; __utmc=42127285; __utmz=42127285.1658240299.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); _ym_uid=1658240299211699538; _ym_d=1658240299; _ym_isad=1; ageRestrict=17"
    }
req = requests.get(url0 + '1', headers=headers)
src = req.text
soup = BeautifulSoup(src, "lxml")

obj_next = soup.find("nav", {"class": "issue"}).find("a", {"href": "#"})

item_max = obj_next.text.split("/")
maxs = int(item_max[1])
i = 1
while i <= maxs:
    i_s = str(i)
    url = url0 + i_s
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    soup = BeautifulSoup(src, "lxml")
    obj = soup.find(id ="mainImage")
    item_href = "https://acomics.ru" + obj.get("src")
    p = requests.get(item_href)
    out = open("in\\" + i_s + ".jpg", "wb")
    out.write(p.content)
    out.close()
    print("Image " + i_s + " save OK")
    i = i + 1
print("All image save!")
