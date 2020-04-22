from bs4 import BeautifulSoup
import requests
import datetime
import os

def get_articles(page_num):
    website_name = os.path.basename(__file__).replace("_", ".")[:-3]
    archive_url = 'https://' + website_name + '/page/' + str(page_num) + '/?s'
    resp = requests.get(archive_url)
    soup = BeautifulSoup(resp.text, 'lxml')
    article_url_tags = soup.find_all("div", {"class": "frontpage-archive-text"})

    articles = []
    for article_url_tag in article_url_tags:
        article_url = article_url_tag.find("h2").find("a").attrs["href"]
        resp = requests.get(article_url)
        soup = BeautifulSoup(resp.text, 'lxml')
        title_tag = soup.find("h1", {"class": "headline"})
        paragraphs = soup.find("div", {"id": "content-area"}).findAll("p")
        article_text = ""
        for paragraph in paragraphs:
            article_text += "".join('<p>' + paragraph.decode_contents() + '</p>')
        date = soup.find("span", {"class": "archive-byline"}).text[:10]
        datetime_object = datetime.datetime.strptime(date, '%m.%d.%Y')

        articles.append({
                        "title": title_tag.text,
                        "subtitle": "",
                        "text": article_text,
                        "url": article_url,
                        "publisher": website_name,
                        "date": datetime_object
                         })
    return articles

def grouping():
    return "by_page"

if __name__ == "__main__":
    print("module test")