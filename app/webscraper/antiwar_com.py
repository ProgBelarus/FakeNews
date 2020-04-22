from bs4 import BeautifulSoup
import requests
import datetime
import os

def get_articles(date):
    website_name = os.path.basename(__file__).replace("_", ".")[:-3]
    BASE_URL = 'http://news.antiwar.com/'
    url_for_date = BASE_URL + str(date.year) + '/' + '{:02}'.format(date.month) + '/' + '{:02}'.format(date.day)
    resp = requests.get(url_for_date, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'lxml')
    article_url_tags = soup.find_all("h2", {"class": "front-entry-title"})

    articles = []
    for article_url_tag in article_url_tags:
        article_url = article_url_tag.find("a").attrs["href"]
        resp = requests.get(article_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, 'lxml')
        title_tag = soup.find("h1", {"class": "entry-title"})
        subtitle_tag = soup.find("span", {"class": "pagesub"})
        if subtitle_tag:
            subtitle = subtitle_tag.text
        else:
            subtitle = ""
        article_tag = soup.find("div", {"class": "entry-content"}).find("p")

        articles.append({
                        "title": title_tag.text,
                        "subtitle": subtitle,
                        "text": article_tag.decode_contents(),
                        "url": article_url,
                        "publisher": website_name,
                        "date": date
                        })
    return articles

def grouping():
    return "by_date"

if __name__ == "__main__":
    date = datetime.datetime(2019, 8, 20)
    articles = get_articles(date)
    for parsed_article in articles:
        print("Article:")
        print("Title:\n", parsed_article["title"])
        print("Subtitle:\n", parsed_article["subtitle"])
        print("Text:\n", parsed_article["text"])