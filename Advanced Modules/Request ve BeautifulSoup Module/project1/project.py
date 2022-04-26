import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,'html.parser')

a = float(input("Enter the rating: "))

headers = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class","ratingColumn imdbRating"})

for header,rating in zip(headers,ratings):
    header = header.text
    rating = rating.text
    header = header.strip()
    header = header.replace("\n"," ")
    rating = rating.strip()
    rating = rating.replace("\n"," ")
    if(float(rating) > a):
        print(f"Film Name --> {header} Film Rating --> {rating}")