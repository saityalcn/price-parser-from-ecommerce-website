import requests
from bs4 import BeautifulSoup

# webscarping

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'


html = requests.get(url).content
header = requests.get(url).headers
print(header)
domainStartingIndex = header.get('Set-Cookie').find('Domain=.')
domainEndingIndex = header.get('Set-Cookie').find(".com")
domain = header.get('Set-Cookie')
print(domain[domainStartingIndex+8:domainEndingIndex+4])
soup = BeautifulSoup(html, "html.parser")

list1 = soup.find_all("li", {"class": "column"}, limit=9)

for li in list1:
    name = li.div.a.h3.text.strip()    
    link = li.div.a.get("href")
    name = "a"
    oldprice = li.find("div", {"class":"proDetail"}).find_all("span")[0].text.strip().strip('TL')
    newprice = li.find("div", {"class":"proDetail"}).find_all("span")[1].text.strip().strip("TL")
    print(f"{name}  ||  {oldprice} {newprice}")





