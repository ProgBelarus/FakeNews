from bs4 import BeautifulSoup
import requests
import datetime
from app.catalog.models import Publication, Book

def get_articles_url_for_page(page_num):
    BASE_URL = 'https://infostormer.com/page/'
    url_for_date = BASE_URL + str(page_num) + '/?s'
    resp = requests.get(url_for_date)
    soup = BeautifulSoup(resp.text, 'lxml')
    article_url_tags = soup.find_all("h3", {"class": "entry-title"})

    articles_url = []
    for article_url_tag in article_url_tags:
        article_url = article_url_tag.find("a").attrs["href"]
        articles_url.append(article_url)
    return articles_url


def parse_article(article_url):
    resp = requests.get(article_url)
    soup = BeautifulSoup(resp.text, 'lxml')
    title_tag = soup.find("h1", {"class": "entry-title"})
    article_text = "".join(soup.find("div", {"class": "td-post-content"}).findAll(text=True))
    date = soup.find("time", {"class": "entry-date"}).text

    return {"title": title_tag.text,
            "subtitle": "",
            "text": article_text,
            "url": article_url,
            "publisher": "infostormer.com",
            "date": date}

def articles_for_page(page_num):
    articles_url = get_articles_url_for_page(page_num)
    articles = [parse_article(article_url) for article_url in articles_url]

    return articles

def add_articles_for_page_to_database(page_num):
    articles = articles_for_page(page_num)

    if not Publication.query.filter_by(name = 'infostormer.com').first():
        Publication.create_publication(name = 'infostormer.com')

    for article in articles:
        if not Book.query.filter_by(title = article["title"], subtitle = article["subtitle"], text = article["text"]).first():
            Book.create_article(title = article["title"],
                                subtitle = article["subtitle"],
                                text = article["text"],
                                url = article["url"],
                                pub_date = article["date"],
                                pub_id = Publication.query.filter_by(name = article["publisher"]).first().id
                                )

if __name__ == "__main__":
    date = datetime.datetime(2019, 8, 20)
    articles = articles_for_date(date)
    for parsed_article in articles:
        print("Article:")
        print("Title:\n", parsed_article["title"])
        print("Subtitle:\n", parsed_article["subtitle"])
        print("Text:\n", parsed_article["text"])