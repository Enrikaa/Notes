import requests
from bs4 import BeautifulSoup as bs4


class Post:
    def __init__(self, date, title, textUrl, imgUrl):
        self.date = date
        self.title = title
        self.textUrl = textUrl
        self.imgUrl = imgUrl


def getNews(Post):
    posts = []
    url = "https://www.post.lt/lt/naujienos?field_category_target_id=All&page=0"

    page = requests.get(url)
    soup = bs4(page.text, "lxml")

    posts = []

    for i in soup.findAll(
        "div", class_="card card-border card-margin card-news mh-item"
    ):

        for name in i.findAll("p"):
            a = name.getText()

        for name in i.findAll("h5"):
            b = name.getText()

        for name in i.findAll("a", href=True, text=True):
            c = "https://www.post.lt" + name["href"]
            break

        for name in i.findAll("img"):
            d = "https://www.post.lt" + name["src"]

        posts.append(Post(a, b, c, d))
    return posts