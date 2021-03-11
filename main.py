from bs4 import BeautifulSoup
import requests
import html

req = requests.get('https://www.empireonline.com/movies/features/best-movies-2')

soup = BeautifulSoup(req.text, "html.parser")

link = []
text = []


allatags = soup.find_all(name="h3", class_="title")
for i in range(len(allatags)-1, -1, -1):
    if i == 99:
        film ="1) " + allatags[i].getText()
        with open("films.txt", "a") as a:
            a.write(f"{html.unescape(film)}")
    else:
        try:
            with open("films.txt", "a") as a:
                a.write("\n")
                a.write(f"{allatags[i].getText()}")
        except UnicodeEncodeError:
            pass
