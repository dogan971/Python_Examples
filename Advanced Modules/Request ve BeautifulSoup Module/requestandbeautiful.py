from bs4 import BeautifulSoup
import requests
# Site Belirledik
url = "https://developer.mozilla.org/en-US/" 
# Veriyi Çektik
response = requests.get(url)
# print(response)
# content ile  response içindeki veriyi aldık
html_icerigi = response.content
# soup değişkenine soup aracılıyla onu daha iyi bir halde attık
soup = BeautifulSoup(html_icerigi,"html.parser")
# ve son olarak prettify ile onu en iyi hale getirip veriyi düzgün bir biçimde yazdırdık
# print(soup.prettify())

# print(soup.find_all("a")) html_iceriginin içindeki bütün a etiketlerini aldı

# for i in soup.find_all("a"):
#     print(i)
#     print("***********************************")

# iyice filtrelemek istersek 
# for i in soup.find_all("a"): # a nın içindeki hrefleri çektik sadece
#     print(i.get("href"))
#     print("*************************************")

# for i in soup.find_all("a"): # a nın içindeki textleri çektik sadece
#     print(i.text)
#     print("*************************************")

# belirli bi class ı istiyoruz
for i in soup.find_all("div",{"class":"article-tile"}):
    print(i)  
    print("***********************************")