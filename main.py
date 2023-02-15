import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "lxml")

movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in movies]

index = len(movies_list) - 1

while index >= 0:
    movie = movies_list[index]
    with open("All-time-top-100-movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{movie}\n")
    index -= 1







