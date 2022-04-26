import time
from bs4 import BeautifulSoup
import requests


def get_data_from_site():
    url = "https://www.doviz.com/" 
    response = requests.get(url)
    html_content = response.content
    return html_content 
while True:
    soup = BeautifulSoup(get_data_from_site(),"html.parser")
    name_list = []
    value_list = [] 
    for i in soup.find_all("div",{"class":"item"}):
        for i in soup.find_all("span",{"class":"name"}):
            name_list.append(i.text)
        for i in soup.find_all("span",{"class":"value"}):
             value_list.append(i.text)
    for i in zip(name_list,value_list):
        print(i)
        print("***************************************************")
    time.sleep(15)
    