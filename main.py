import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(URL)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
gallary_data = soup.find(class_="gallery")
titles_data = gallary_data.findAll(class_="title")
titles = []
with open("movies.txt", "w") as movies_file:
    for title in reversed(titles_data):
        movies_file.write(f"{title.string}\n")
